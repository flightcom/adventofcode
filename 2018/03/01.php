<?php

$input = file_get_contents(basename(__FILE__, '.php') . '.txt');
$input = explode("\n", $input);

$fabric = [];

# Setup the original overlapping array
for ($i = 0; $i < 1000; $i++) {
    for ($j = 0; $j < 1000; $j++) {
        $fabric[$i][$j] = 0;
    }
}

foreach ($input as $key => $val) {
    $split = trim(explode('@', $val)[1]);
    $position = trim(explode(':', $split)[0]);
    $dimensions = trim(explode(':', $split)[1]);
    $pos_left = trim(explode(',', $position)[0]);
    $pos_top = trim(explode(',', $position)[1]);
    $dim_width = trim(explode('x', $dimensions)[0]);
    $dim_height = trim(explode('x', $dimensions)[1]);

    for ($x = $pos_left; $x < $pos_left + $dim_width; $x++) {
        for ($y = $pos_top; $y < $pos_top + $dim_height; $y++) {
            $fabric[$x][$y]++;
        }
    }
}

$result = [];

# Linearize array
foreach ($fabric as $value) {
    $result = array_merge($result, $value);
}

# Remove values 0 or 1
$result = array_filter($result, function ($value) {
    return $value > 1;
});

echo count($result);

echo "\n";
