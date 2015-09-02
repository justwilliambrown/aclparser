<?php
//connect to the SQL server
$connection = mysql_connect('localhost', 'access', '0123'); //The Blank string is the password
mysql_select_db('ac_stats');

$game_id = 1;

//$query = "SELECT name, headshots, kills, deaths, ratio, score, flags, returns FROM games WHERE gamenum = $game_id";
$query = "SELECT * FROM games";

$result = mysql_query($query);

//Turning tables
//echo "<table>"; // start a table tag in the HTML
//while($row = mysql_fetch_array($result)){   //Creates a loop to loop through results
//echo "<tr><td>" . $row['name'] . "</td><td>" . $row['headshots'] . "</td><td>" . $row['kills'] . "</td><td>" . $row['deaths'] . "</td><td>" . $row['ratio'] . "</td><td>" . $row['score'] . "</td><td>" . $row['flags'] . "</td><td>" . $row['returns'] . "</td></tr>";  //$row['index'] the index here is a field name
//}
//echo "</table>"; //Close the table in HTML

echo "<table border=3 bordercolor='green'>";
echo "<tr><td> Name </td><td> Kills </td><td> Deaths </td><td> Ratio </td></tr>";
while($row = mysql_fetch_array($result)){   //Creates a loop to loop through results
echo "<tr><td>" . $row['name'] . "</td><td>" . $row['kills'] . "</td><td>" . $row['deaths'] . "</td><td>" . $row['ratio'] . "</td></tr>";  //$row['index'] the index here is a field name
}
echo "</table>";
mysql_close(); //Make sure to close out the database connection
?>
