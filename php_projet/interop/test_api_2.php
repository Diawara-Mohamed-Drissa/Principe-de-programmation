<?php

$url = "http://127.0.0.1:5000/students";
$response = file_get_contents($url);

//Décodage du JSON en tableau PHP
$students = json_decode($response, true);

echo "<pre>";
print_r($students);
echo "</pre>";