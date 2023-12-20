#!/bin/bash


#Create a function  will print the numbers 1 - 10 (each on a separate line) and whether they are even or odd.


print_numbers () {

	for numbers in {1..10}; do

	if [ $((numbers % 2)) -eq 0 ]; then
		echo "$1 $numbers in even"
	else
		echo "$1 $numbers is odd" 
fi
done
}

print_numbers "The" 
