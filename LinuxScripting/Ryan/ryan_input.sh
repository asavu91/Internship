#!/bin/bash
 
#simple script which will ask the user for a few pieces of information then combine this into a message which is echo'd to the screen.
#Add to the previous script to add in some data coming from command line arguments and maybe some of the other system variables.
argument=$1
user=$(whoami)
date=$(date)
current_loc=$(pwd)
current_ls=$(ls)
echo Insert your name:

read varname

echo "Hello $varname"
echo "You are logged as $user, you are in the directory $current_loc with the following list $current_ls  and today's date is $date."
echo "You inserted $argument word."

 
