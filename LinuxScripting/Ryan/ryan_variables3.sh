#!/bin/bash

#create a script which will take a filename as its first argument and create a dated copy of the file

filename="$1"

current_date=$(date "+%Y-%m-%d")

new_filename="${current_date}_${filename}"

cp "$filename" "$new_filename"

echo "File copied succesfully"

