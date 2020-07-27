#!/bin/bash

sed -n '1~3p' $1 > Xdat.dat
sed -n '2~3p' $1 > Ydat.dat
sed -n '3~3p' $1 > Zdat.dat

paste Xdat.dat Ydat.dat Zdat.dat > XYZ$1
rm Xdat.dat Ydat.dat Zdat.dat
