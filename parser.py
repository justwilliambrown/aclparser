#Written by Padfoot. Leave this line here. Python3
# To calculate the score, multiply the kills by 10, then subtract from that deaths * 4
from parse import *
import mysql.connector
import math

#Variable Stuff
record = True
stats = {}
game_stats = {}
game_count = 1
killmsg = ["busted", "picked off", "peppered", "sprayed", "punctured", "shredded", "slashed", "splattered", "headshot", "gibbed"]
ID = 0

#Setting up db
cnx = mysql.connector.connect(user='access', database='ac_stats', password='0123')
pointer = cnx.cursor()


def kill_count(name, method, tk):
    if record == True:
        global game_stats
        global stats
        multiplier = 1
        if name not in stats:
            stats[name] = dict(kills = 0, deaths = 0, flags = 0, returns = 0, headshots = 0, ratio = 0, score = 0)
        if name not in game_stats:
            game_stats[name] = dict(kills = 0, deaths = 0, flags = 0, returns = 0, headshots = 0, ratio = 0, score = 0)
        if method in ("slashed", "headshot"):
            multiplier += 1
        if tk == True:
            multiplier = -1
        game_stats[name]['kills'] += multiplier
        stats[name]['kills'] += multiplier
        #Check to see if it was a headshot.
        if method == "headshot":
            game_stats[name]['headshots'] += 1
            stats[name]['headshots'] += 1
        #Update the ratio
        if game_stats[name]["deaths"] == 0:
            stats[name]["ratio"] = '%.2f' % (stats[name]["kills"] / (stats[name]["deaths"] + 1))
            game_stats[name]["ratio"] = '%.2f' % (game_stats[name]["kills"] / (game_stats[name]["deaths"] + 1))
        else:
            stats[name]["ratio"] = stats[name]["kills"] / (stats[name]["deaths"])
            game_stats[name]["ratio"] = '%.2f' % (game_stats[name]["kills"] / (game_stats[name]["deaths"]))
        #Set his score
        stats[name]["score"] = (stats[name]["kills"] * 10) - (stats[name]["deaths"] * 4)
        game_stats[name]["score"] = (game_stats[name]["kills"] * 10) - (game_stats[name]["deaths"] * 4)

def death_count(killed):
    if record == True:
        #print(killed, "was recognised as killed")
        global game_stats
        global stats
        if killed not in game_stats:
            game_stats[killed] = dict(kills = 0, deaths = 0, flags = 0, returns = 0, headshots = 0, ratio = 0, score = 0)
        game_stats[killed]["deaths"] += 1
        if killed not in stats:
            stats[killed] = dict(kills = 0, deaths = 0, flags = 0, returns = 0, headshots = 0, ratio = 0, score = 0)
        stats[killed]["deaths"] += 1
        # Update the ratio
        if game_stats[killed]["deaths"] == 0:
            stats[killed]["ratio"] = '%.2f' %(stats[killed]["kills"] / (stats[killed]["deaths"] + 1))
            game_stats[killed]["ratio"] = '%.2f' % (game_stats[killed]["kills"] / (game_stats[killed]["deaths"] + 1))
        else:
            stats[killed]["ratio"] = '%.2f' % (stats[killed]["kills"] / (stats[killed]["deaths"]))
            game_stats[killed]["ratio"] = '%.2f' % (game_stats[killed]["kills"] / (game_stats[killed]["deaths"]))
        #Update the score
        stats[killed]["score"] = (stats[killed]["kills"] * 10) - (stats[killed]["deaths"] * 4)
        game_stats[killed]["score"] = (game_stats[killed]["kills"] * 10) - (game_stats[killed]["deaths"] * 4)
        #print(game_stats)

def flag_count(data):
    if record == True:
        #print("Got to here")
        scorer = data[1]
        if scorer not in game_stats:
            game_stats[scorer] = dict(kills = 0, deaths = 0, flags = 0, returns = 0, headshots = 0)
        if scorer not in stats:
            stats[scorer] = dict(kills = 0, deaths = 0, flags = 0, returns = 0, headshots = 0)
        stats[scorer]['flags'] += 1
        game_stats[scorer]['flags'] += 1
        #print(game_stats)

def flag_returns(returner):
    if record == True:
        if returner not in game_stats:
            game_stats[returner] = dict(kills = 0, deaths = 0, flags = 0, returns = 0, headshots = 0)
        if returner not in stats:
            stats[returner] = dict(kills = 0, deaths = 0, flags = 0, returns = 0, headshots = 0)
        #game_stats[returner]['returns'] += 1

def output(p, game_stats):
    global game_count
    global ID
    game_stats['map'] = p['map']
    game_stats["mode"] = p["mode"]
    #print(game_info)
    #print(game_stats, '\n')


    query = ("Insert Into %s %s "
            "values %s")
    #Setup the mode and the map with the gamenum
    pointer.execute(query % ('game_info', 'map', p['map']))
    pointer.execute(query % ('game_info', 'mode', p['mode']))

    for i in game_stats:
        if i in ['map', 'mode', 'gamenum']:
            #pointer.execute(query, i, i[l]
            pass
        else:
            game_stats[i]["gamenum"] = game_count
            game_stats[i]['ID'] = ID
            ID += 1

            pointer.execute(query % ('games', 'name', i))
            for l in game_stats[i]:
                    #pointer.execute(query, (i, l))
                    pointer.execute(query % ('games', l, game_stats[i][l]))
    game_count += 1
    #print("---------------------------------------------------------------------")
while True:
    try:
        a = input()
    except EOFError:
        break
    #print(a)
    data = a.split(' ')
    # Strip the timestamps
    try:
        del data[:3]
    except IndexError:
        continue
    #print(data)

    #Find the information from the map start bit.
    # Game start: deathmatch on ac_douze, 1 players, 8 minutes, mastermode 0, (map rev 19/5707, official, 'getmap' not prepared)
    if len(data) > 3 and data[1] == "start:" and data[0] == "Game":
        i = (" ".join(data))
        p = parse("Game start: {mode} on {map}, {clients} players, {map_time} minutes, mastermode {mastermode}, (map rev {map_rev}, {map_type}, 'getmap' {getmap})", i)
        # Here we should clear the stats, just in case the last game did not terminate fully
        game_stats = {}
    #Find information from the map_finish bit.
    # Game status: one shot, one kill on ac_metl2, game finished, open, 5 clients
    if len(data) > 4 and data[1] == "status:" and data[0] == "Game" and data[-4] == "finished,":
        b = " ".join(data)
        #print("The finish is:", b)
        p = parse("Game status: {mode} on {map}, game finished, {mastermode}, {clients} clients", b)
        #Clear game_stats from previous game.
        #print(p)
        #print(game_stats)
        #print(len(game_stats))
        output(p, game_stats)
        game_stats = {}

    #This decides if it is a score with a flag or not
    #[2.122.234.74] Maximum scored with the flag for CLA, new score 2
    if len(data) == 11 and data[2:6] == ['scored', 'with', "the", "flag"]:
        #print("Someone scored")
        flag_count(data)
    if len(data) == 5 and data[2:5] == ['returned', 'the', 'flag']:
        returner = data[1]
        #print("Someone Returned")
        flag_returns(returner)

    #This makes sure that people saying this doesn't trip up the code.
    #if len(data) not in (4, 5, 6) or data[2] not in killmsg and "".join(data[2:4]) not in killmsg:
    #   print(data[2:4])
    #   print("Shit is breaking here")
    #   print(data)
    #   continue
    #Assigning values to variables
    # [181.1.189.198] ibanews1 shredded DREAM_RUNNER
    # [75.100.46.55] ErectGandalf picked off R4G3|BangBang
    # [162.250.90.131] Ctwist shredded their teammate ibanews1
    # [162.250.90.131] Ctwist picked off their teammate ibanews1
    if len(data) in (4, 5, 6, 7):
        if data[2] in killmsg:
            name = data[1]
            method = data[2]
            if data[3:5] == ['their', 'teammate']:
                killed = data[5]
                tk = True
            else:
                killed = data[3]
                tk = False
            kill_count(name, method, tk)
            death_count(killed)

        if " ".join(data[2:4]) in killmsg:
            name = data[1]
            method = " ".join(data[2:4])
            if data[4:6] == ['their', 'teammate']:
                killed = data[-1]
                tk = True
            else:
                tk = False
                killed = data[4]
            kill_count(name, method, tk)
            death_count(killed)
#print("These are the final stats")
#print(stats)
