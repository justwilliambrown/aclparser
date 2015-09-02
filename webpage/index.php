<?php
echo "<html>";
echo "<head><title> AssaultCube Logging </title></head>";
echo "<body>";
echo "<link rel=shortcut icon href=/stats/favicon.ico />";

//connect to the SQL server
$connection = mysql_connect('localhost', 'access', '0123'); //The Blank string is the password
mysql_select_db('ac_stats');

$game_id = 1;

echo "<form action=view.php method=post>";
echo  "Game Number:<br>";
echo  "<input type=integer name=game>";
echo "<input type=submit value=Submit>";
echo "</form>";

//Print the basic information about the game
// $gmquery = "SELECT * FROM game_info";
// $res = mysql_query($gmquery);
// while($grow = mysql_fetch_array($res)){
// echo "This was a game of " . $grow['mode'] . " on map " . $grow['map'];
// echo "<br>";
// }

mysql_close(); //Make sure to close out the database connection
?>
