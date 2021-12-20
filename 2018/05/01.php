<?php

# SETUP
if (file_exists(basename(__FILE__, '.php') . '.txt')) {
    $input_file = basename(__FILE__, '.php') . '.txt';
} else {
    $input_file = '01.txt';
}

$input = file_get_contents($input_file);
// $input = explode("\n", $input);


$result = null;

# SOLUTION GOES HERE

$to_be_processed = true;
$chars = str_split($input);

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


$result = count($chars);

# OUTPUT RESULT
echo $result . "\n";
