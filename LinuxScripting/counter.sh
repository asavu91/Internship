#!/bin/bash




occurance=$(grep -o "StrictHostKeyChecking" bashcrc | wc -w)

echo $occurance 
