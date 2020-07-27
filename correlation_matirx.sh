#!/bin/bash

rm -f plot_thermo.closed_correlation_mode*

for m in 6 9 11 ; do
{
  awk -v mode=$m BEGIN'{
	ifile1="vector_1a6d_"mode".dat"
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
		for(j=(k-1);j>=1;j--)
		{
  			for(i=1;i<k;i++)
			{
				printf("%f\t",(x1[j]*x1[i]+y1[j]*y1[i]+z1[j]*z1[i])/((sqrt(x1[j]*x1[j]+y1[j]*y1[j]+z1[j]*z1[j]))*(sqrt(x1[i]*x1[i]+y1[i]*y1[i]+z1[i]*z1[i])))) >> "plot_thermo.closed_correlation_mode"mode"_subunit_1.dat"
        
			}
			printf("\n")>>"plot_thermo.closed_correlation_mode"mode"_subunit_1.dat"

		}
	}
  }'
}
done
