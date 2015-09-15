<?php
echo "<html>";
echo "<head><title> AssaultCube Logging </title></head>";
echo "<body>";
echo "<link rel=shortcut icon href=/stats/favicon.ico />";
echo "<center>";
echo "<img src='title.png'>";
echo "<br>";
echo "Take a survey on the application <a href=https://www.surveymonkey.com/r/YNHMM2R>here</a>";
echo "<br>";
echo "<br>";
echo "<br>";
//connect to the SQL server
$connection = mysql_connect('localhost', 'access', '0123'); //The Blank string is the password
mysql_select_db('ac_stats');

$game_id = 1;

// echo "<form action=view.php method=get>";
// echo  "Game Number:<br>";
// echo  "<input type=integer name=game>";
// echo "<input type=submit value=Submit>";
// echo "</form>";

//TODO Implement a search

//Print the basic information about the game
$gmquery = "SELECT * FROM game_info";
$res = mysql_query($gmquery);
while($grow = mysql_fetch_array($res)){
  echo "<a href=view.php?game=" . $grow["ID"] . ">";
  echo "A game of " . $grow['mode'] . " on map " . $grow['map'];
  echo "</a>";
  echo "<br>";
}
echo "</center>";

mysql_close(); //Make sure to close out the database connection
?>
