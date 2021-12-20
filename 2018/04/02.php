<?php

# SETUP
if (file_exists(basename(__FILE__, '.php') . '.txt')) {
    $input_file = basename(__FILE__, '.php') . '.txt';
} else {
    $input_file = '01.txt';
}

$input = file_get_contents($input_file);
$input = explode("\n", $input);

$result = [];

# ORGANISE INPUT
sort($input);

$current_guard = null;
$minToStart = null;
$minToStop = null;

foreach ($input as $entry) {
    $time = trim(explode(']', $entry)[0]);
    $action = trim(explode(']', $entry)[1]);
    $min = (int) explode(':', $time)[1];
    if ($action === 'wakes up') {
        $minToStop = $min;
        for ($m = $minToStart; $m < $minToStop; $m++) {
            if (!in_array($m, array_keys($result))) {
                $result[$m] = [];
            } else {
                array_push($result[$m], $current_guard);
            }
        }
    } elseif ($action === 'falls asleep') {
        $minToStart = $min;
    } else {
        $matches = [];
        preg_match('/#(\d+)/', $action, $matches);
        $current_guard = $matches[0];
    }
}

$sum = [];
$count = [];

# COUNT GUARDS MIN ASLEEP
foreach ($result as $m => $values) {
    $sum[$m] = count($values);
}

# GET MOST PRESENT GUARD
foreach ($result as $m => $values) {
    $c = array_count_values($values);
    $val = array_search(max($c), $c);
    $count[$m] = $val;
}

arsort($sum);

var_export($sum) . chr(10);
var_export($count) . chr(10);
