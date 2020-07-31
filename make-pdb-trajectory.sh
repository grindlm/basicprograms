#! /bin/bash

rm testvec*.dat

for m in `seq 1 50` ; do
	echo m=$m;
	awk -v num=$m 'BEGIN {
		ifile1="dnak-adp-ca.orie.pdb"
		rc=getline<ifile1
		i=1
		while (rc==1)
		{
			x[i]=substr($0,31,8)
			y[i]=substr($0,39,8)
			z[i]=substr($0,47,8)
			line1[i]=substr($0,1,30)
			line2[i]=substr($0,55,24)
			i=i+1
			rc=getline<ifile1
		}
		ifile2="ev-sorted-xyz-dnakADPtoATP.mode12.dat"
		rc=getline<ifile2
		k=1
		while (rc==1)
		{
			vecx[k]=$1*num
			vecy[k]=$2*num
			vecz[k]=$3*num
			k++
			rc=getline<ifile2}

			{
				j=1
				while ((j<k))
				{
					newvecx[j]=x[j]+vecx[j]
					newvecy[j]=y[j]+vecy[j]
					newvecz[j]=z[j]+vecz[j]
					#print newvecx[j]"  "newvecy[j]"  "newvecz[j]" "x[j]" "y[j]" "z[j]" "vecx[j]" "vecy[j]" "vecz[j] >> "testvec.add."m".dat"
					printf line1[j] >> "testvec.add."num".dat"
					printf "%8.3f",newvecx[j] >> "testvec.add."num".dat"
					printf "%8.3f",newvecy[j] >> "testvec.add."num".dat"
					printf "%8.3f",newvecz[j] >> "testvec.add."num".dat"
					print line2[j] >> "testvec.add."num".dat"
					#!print newx= " " "newvecx[j]"  "newy=" "newvecy[j]" "newz="  "newvecz[j]"  "oldx=" "x[j]" "oldy=" "y[j]" "oldz=" "z[j]" "addx=" "vecx[j]" "addy=" "vecy[j]"  "addz=" "vecz[j] >> "testvec.add.dat"
					j++}}
					print "ENDMDL" >> "testvec.add."num".dat"
				}'
		paste testvec.add.$m.dat >> testvec.dnak-adp.all.dat

done
rm testvec.add.*.dat
