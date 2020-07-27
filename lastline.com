#!/bin/bash

#this is a script to remove the last line of a pdb file and rework the rest of it in the way that I want

touch col1-10$1 col11$1 col1-11$1

cut -c 1-60 $1 > col1-10$1
echo -e "CUT LINES\n"
head -n 2 col1-10$1
cut -c 61-66 $1 > col11$1
head -n 2 col11$1

paste col1-10$1 col11$1 > col1-11$1
echo -e "PASTE Lines\n"
head -n 2 col1-11$1

awk '{\
	if(NR<=4880){\
		print $0"\tGA"}\
	else{\
		print $0"\tGB"}\
	}' col1-11$1 > $2

rm col1-10$1 col11$1 col1-11$1

echo -e $2"\n------------------"
head -n 4 $2

