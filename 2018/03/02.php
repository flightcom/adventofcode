<?php

$input = file_get_contents(basename(__FILE__, '.php') . '.txt');
$input = explode("\n", $input);

$fabric = [];
$sizes = [];

# Setup the original overlapping array
for ($i = 0; $i < 1000; $i++) {
    for ($j = 0; $j < 1000; $j++) {
        $fabric[$i][$j] = 0;
    }
}

foreach ($input as $key => $val) {
    $split = trim(explode('@', $val)[1]);
    $id = trim(explode('@', $val)[0]);
    $position = trim(explode(':', $split)[0]);
    $dimensions = trim(explode(':', $split)[1]);
    $pos_left = (int) trim(explode(',', $position)[0]);
    $pos_top = (int) trim(explode(',', $position)[1]);
    $dim_width = (int) trim(explode('x', $dimensions)[0]);
    $dim_height = (int) trim(explode('x', $dimensions)[1]);

    $sizes[$id] = $dim_width * $dim_height;

    for ($x = $pos_left; $x < $pos_left + $dim_width; $x++) {
        for ($y = $pos_top; $y < $pos_top + $dim_height; $y++) {
            if ($fabric[$x][$y] === 0) {
                $fabric[$x][$y] = $id;
            } elseif (substr($fabric[$x][$y], 0, 1) === '#') {
                $fabric[$x][$y] = 2;
            } else {
                $fabric[$x][$y]++;
            }
        }
    }
}

$result = [];

# Linearize array
foreach ($fabric as $value) {
    $result = array_merge($result, $value);
}

# Find ID
$count = [];
foreach ($result as $value) {
    if (substr($value, 0, 1) === '#') {
        $id = $value;
        if (in_array($id, array_keys($count))) {
            $count[$id]++;
        } else {
            $count[$id] = 1;
        }
    }
}

# Compare with claim size
foreach ($count as $id => $value) {
    if ($value === $sizes[$id]) {
        echo "FOUND ! \n";
        echo $id;
    }
}

echo "\n";
