#!/bin/bash

# Takes a number and returns an Arnold Schwarzenegger quote.

echo "AHHHHNOLD QUOTES"
echo "Lorenzo Galante, 2019"
echo "Embedded Linux"

echo 
echo 


number=$1

#RANDOM GENERATOR NOT WORKING

#if [$1=="random"]
#then
#	$number=$((1 + RANDOM % 10))
#fi

case $number in 

1) echo "If it bleeds, we can kill it."
;;
2) echo "The worst thing I can be is the same as everybody else. I hate that."
;;
3) echo "The mind is the limit. As long as the mind can envision the fact that you can do something, you can do it, as long as you really believe 100 percent."
;;
4) echo "It's simple, if it jiggles, it's fat."
;;
5) echo "Milk is for babies. When you grow up you have to drink beer."
;;
6) echo "For me life is continuously being hungry. The meaning of life is not simply to exist, to survive, but to move ahead, to go up, to achieve, to conquer."
;;
7) echo "Help others and give something back. I guarantee you will discover that while public service improves the lives and the world around you, its greatest reward is the enrichment and new meaning it will bring your own life."
;;
8) echo "I welcome and seek your ideas, but do not bring me small ideas; bring me big ideas to match our future."
;;
9) echo "Failure is not an option. Everyone has to succeed."
;;
10) echo "I am the most helpful and open up doors for everyone and I like to share."
;;
esac

