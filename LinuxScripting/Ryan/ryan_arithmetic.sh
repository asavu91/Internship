#!/bin/bash

#Create a simple script which will take two command line arguments and then sums them together 
#write a script which will use RANDOM
#Write a Bash script which will print tomorrows date

echo "Insert the first number"

read f_number

echo "Insert second number"

read s_number

echo "Insert your age."

read age


future_age=$((( $RANDOM % 20 ) + $age ))
date=$( date --date="tomorrow" )

echo "Tomorrow, $date, you will have $future_age years old."

echo "The sum of the inserted numbers are: $( expr $f_number + $s_number )"
