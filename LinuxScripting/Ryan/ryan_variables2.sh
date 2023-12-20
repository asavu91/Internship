#!/bin/bash

#f a number is supplied as the first command line argument then it will select from only words with that many characters


word_length="$1"
file=fisier.txt
random_word=$(grep -E "^.{${word_length}}$" "$file"| shuf -n 1 )


echo "$random_word"


