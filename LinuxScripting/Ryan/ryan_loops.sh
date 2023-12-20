#!/bin/bash

#Create a simple script which will print the numbers 1 - 10 (each on a separate line) and whether they are even or odd.

for value in {1..10};
do
	if [ "$(expr $value % 2)" == 0 ];
then
	echo "$value is even"
else
	echo "$value is odd"
	fi
done
