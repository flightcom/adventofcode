<?php

$input = file_get_contents(basename(__FILE__, '.php') . '.txt');
$input = explode("\n", $input);

$value = 0;

foreach ($input as $key => $val) {
    $value += (int) $val;
}

echo $value;

echo "\n";
