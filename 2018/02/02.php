<?php

$input = file_get_contents(basename(__FILE__, '.php') . '.txt');
$input = explode("\n", $input);

foreach ($input as $key => $val) {
    $diff = [];
    $current_word = $input[$key];
    $array_filtered = array_filter($input, function ($inp, $index) use ($key) {
        return $index !== $key;
    }, ARRAY_FILTER_USE_BOTH);
    foreach ($array_filtered as $key2 => $val2) {
        $lev_dist = levenshtein($current_word, $val2);
        if ($lev_dist === 1) {
            echo "FOUND ! \n";
            echo "$current_word\n";
            echo "$val2\n";
        }
    }
}


echo "\n";
