#!/bin/bash

#create a script which will accept some command line arguments and echo out some details

name="General Kenobi"
location=$(pwd)
code="$1"


echo "Hello there!"
sleep 2
echo "$name"
sleep 2
echo "You find yourself in $location."
sleep 1
echo "You go by the code of $code."
sleep 1

#Create a script which will print a random word

random_word=$( cat fisier.txt | shuf -n 1 )
echo "$random_word"



