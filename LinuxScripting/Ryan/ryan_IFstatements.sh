#!/bin/bash

#Dark Souls IF it was a statement

echo "Choosen undead, pick your class:
1 - Knight
2 - Cleric
3 - Deprived"

read class 

case $class in

	1)

	type="Knight"
	vitality=12
	strength=10
	intelligence=3
	;;

	2)

	type="Cleric"
	vitality=8
	strength=3
	intelligence=14	
	;;

	3)

	type="Deprived"
	vitality=2
	strength=1
	intelligence=0
	;;

esac

echo "Yes, indeed. You chose $type class. With HP of $vitality, strength of $strength and intelligence of $intelligence you are ready journey into Lordran"

sleep 4

echo "**Undead Asylum**"

sleep 2

echo "The asylum demon jumps from above. RUN!. Pick a number between 0-5."

demon=$(( RANDOM % 6 ))

read undead

if [[ $(( undead + strength )) -gt $demon ]];	
	then
	echo "You escaped!"
else
	echo "YOU DIED"
	exit 1
fi

sleep 2

echo "You managed to recover your lost gear and return to defeat the beast. Type what weapons will you use: Sword, Dagger, Staff or Crossbow"

read weapon

if [[  &intelligence -gt  10 || $weapon == "Crossbow" ]];
	then
	echo "With your mighty intellect, you defeated the beast and managed to escape the asylum. From there, Lordran is just a fly away..."

elif [[  $type == "Knight" && $weapon == "Sword" ]];
	then
	echo "You plunged from above and managed to land a critical hint. The beast is defeated. Now the real adventure begins... "
else
	echo "YOU DIED"
fi

sleep 1

echo "To never be continued..."
