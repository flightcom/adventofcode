<?php

# SETUP
if (file_exists(basename(__FILE__, '.php') . '.txt')) {
    $input_file = basename(__FILE__, '.php') . '.txt';
} else {
    $input_file = '01.txt';
}

$input = file_get_contents($input_file);
// $input = explode("\n", $input);

# SOLUTION GOES HERE
$result = [];

$alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];

$original_chars = str_split($input);

foreach ($alphabet as $letter) {
    $result[$letter] = null;

    $chars = $original_chars;

    // filter array
    $chars = array_filter($chars, function ($char) use ($letter) {
        return $char !== $letter && $char !== strtoupper($letter);
    });

    $to_be_processed = true;

    // #1 step loop
    while ($to_be_processed) {
        $to_be_processed = false;
    
        for ($i = 0; $i < count($chars); $i++) {
            if ($i < count($chars) - 1
                && ((ctype_upper($chars[$i]) && ctype_lower($chars[$i+1]))
                || (ctype_lower($chars[$i]) && ctype_upper($chars[$i+1])))
                && strtolower($chars[$i]) === strtolower($chars[$i+1])
            ) {
                $to_be_processed = true;
                unset($chars[$i]);
                unset($chars[$i+1]);
                $chars = array_values($chars);
            }
        }
    }
    $result[$letter] = count($chars);
}

$result = min($result);

# OUTPUT RESULT
echo $result . "\n";
