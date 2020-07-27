#!/bin/bash

# This script will eventually be able to take the coordinates from a file and find the RMSD values for those files

# Extract the coordinates from files
# combine coordinates into one file
# take rmsd of coordinates
touch foo.dat foo1.dat foo3.dat
cut -c 32-54 $1 > foo.dat
echo "foo.dat"
head -n 2 foo.dat
cut -c 32-54 $2 > foo1.dat
echo "foo1.dat"
head -n 2 foo1.dat
paste foo.dat foo1.dat > foo3.dat
echo "foo3.dat"
head -n 2 foo3.dat

awk '{print NR, sqrt(($1-$4)^2+($2-$5)^2+($3-$6)^2)}' foo3.dat > RMSD$1$2.dat
echo RMSD$1$2.dat
head -n 2 RMSD$1$2.dat

rm foo.dat foo1.dat foo3.dat

