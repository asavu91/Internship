#!/bin/bash


search_string="StrictHostKeyChecking"
files="bashcrc bashrc.txt"

echo "Search String StrictHostKeyChecking was found on the lines:"
for file in $files; do
        
        grep -n "$search_string" "$file" | while IFS=: read -r line_number content;
	 do
            echo "$file:$line_number"
        done
    
done





