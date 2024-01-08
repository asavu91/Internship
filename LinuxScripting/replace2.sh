#!/bin/bash

key_word="AUTOMATION"

letters=($(echo $key_word | sed 's/./& /g'))

for l in {63..71}; do

	word_replace=$(awk -v line=$l 'NR==line {print $6)' log.txt}

	random_letter=${letters[$(( RANDOM % ${#letters[@]}))]}

	replace_word=$(echo "$word_replace" | sed "s/./$random_letter/")

	sed -i "${line_number}s/\b$word_replace\b/$replace_word/" log.txt

	echo "$word_replace was replaced with the letter $random_letter" >> replace.txt

done
