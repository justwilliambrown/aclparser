<?php
$link = mysql_connect('localhost', 'access', '0123');
if (!$link) {
    die('Could not connect: ' . mysql_error());
}
echo 'Connected successfully';
mysql_close($link);
?>
