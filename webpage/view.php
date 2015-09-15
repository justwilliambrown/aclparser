<?php
echo "<html>";
echo "<head><title> AssaultCube Logging </title></head>";
echo "<body>";
echo "<link rel=shortcut icon href=/stats/favicon.ico />";
echo "<center>";
echo "Take a survey on the application <a href=https://www.surveymonkey.com/r/YNHMM2R>here</a>";
echo "<br>";
echo "<img src='title.png' align=center>";
echo "<br>";
echo "<br>";
echo "<br>";
//connect to the SQL server
$connection = mysql_connect('localhost', 'access', '0123'); //The Blank string is the password
mysql_select_db('ac_stats');

$game_id = 1;

// echo "<form method=post>";
// echo  "Game Number:<br>";
// echo  "<input type=integer name=game>";
// echo "<input type=submit value=Submit>";
// echo "</form>";

$game_id = $_GET["game"];

//Print the basic information about the game
$gmquery = "SELECT * FROM game_info WHERE ID=$game_id";
$res = mysql_query($gmquery);
while($grow = mysql_fetch_array($res)){
echo "This was a game of " . $grow['mode'] . " on map " . $grow['map'];
echo "<br>";
}
echo "<br>";

$query = "SELECT * FROM games WHERE gamenum=$game_id";

$result = mysql_query($query);

//Turning tables
//echo "<table>"; // start a table tag in the HTML
//while($row = mysql_fetch_array($result)){   //Creates a loop to loop through results
//echo "<tr><td>" . $row['name'] . "</td><td>" . $row['headshots'] . "</td><td>" . $row['kills'] . "</td><td>" . $row['deaths'] . "</td><td>" . $row['ratio'] . "</td><td>" . $row['score'] . "</td><td>" . $row['flags'] . "</td><td>" . $row['returns'] . "</td></tr>";  //$row['index'] the index here is a field name
//}
//echo "</table>"; //Close the table in HTML

echo "<table border=3 bordercolor='green'>";
echo "<tr><td> Name </td><td> Headshots </td><td> Kills </td><td> Deaths </td><td> Ratio </td><td> Score </td><td> Flags </td><td>Returns</td></tr>";
while($row = mysql_fetch_array($result)){   //Creates a loop to loop through results
echo "<tr><td>" . $row['name'] . "</td><td>" . $row['headshots'] . "</td><td>" . $row['kills'] . "</td><td>" . $row['deaths'] . "</td><td>" . $row['ratio'] . "</td>
<td>" . $row['score'] . "</td><td>" . $row['flags'] . "</td><td>" . $row['returns'] . "</td></tr>";
}
echo "</table>";
mysql_close(); //Make sure to close out the database connection
echo "</center>";
?>
