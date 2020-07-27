#!/bin/bash

rm -f plot_mathematica*

for m in 8 13 18 28 ; do
{
  awk -v mode=$m BEGIN'{
	ifile1="ev-sorted-xyz_htpg-2dnak.mode"mode".dat"
	print ifile1
	rc=getline <ifile1
	k=1
	while (rc==1)
	{
		x1[k]=$1
		y1[k]=$2
		z1[k]=$3
		k=k+1
		rc=getline <ifile1
	}
	print k
	{
		for(i=1;i<=(k-1);i++)
		{
			for(j=1;j<=(k-1);j++)
			{
				printf("%f\t",(x1[i]*x1[j]+y1[i]*y1[j]+z1[i]*z1[j])/((sqrt(x1[i]*x1[i]+y1[i]*y1[i]+z1[i]*z1[i]))*(sqrt(x1[j]*x1[j]+y1[j]*y1[j]+z1[j]*z1[j])))) >> "plot_mathematica_htpg-2dnak-mode"mode".dat"
        
			}

			printf("\n") >> "plot_mathematica_htpg-2dnak-mode"mode".dat"
		}
	}
  }'
}
done
