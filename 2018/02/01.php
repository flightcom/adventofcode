<?php

$input = file_get_contents(basename(__FILE__, '.php') . '.txt');
$input = explode("\n", $input);

$value = 0;

$candidates_2 = 0;
$candidates_3 = 0;

foreach ($input as $k => $word) {
    $repeats = [];
    $input_as_array = str_split($word);
    foreach ($input_as_array as $j => $char) {
        if (in_array($char, array_keys($repeats))) {
            $repeats[$char]++;
        } else {
            $repeats[$char] = 1;
        }
    }
    $fitered_array_2 = in_array(2, array_values($repeats));
    $fitered_array_3 = in_array(3, array_values($repeats));

    $candidates_2 += $fitered_array_2;
    $candidates_3 += $fitered_array_3;
}

echo "$candidates_2 $candidates_3\n";

$answer = $candidates_2 * $candidates_3;

echo $answer;

echo "\n";
