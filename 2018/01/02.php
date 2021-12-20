<?php

$input = file_get_contents(basename(__FILE__, '.php') . '.txt');
$input = explode("\n", $input);

$value = 0;
$value_history = [];

$duplicate = null;
$iteration = 0;

while (!$duplicate) {
    echo "Iteration " . ++$iteration . chr(10);
    foreach ($input as $key => $val) {
        if (!in_array($value, $value_history)) {
            array_push($value_history, $value);
        } else {
            $duplicate = $value;
            break;
        }
        $value += (int) $val;
    }
}


echo $duplicate;

echo "\n";
