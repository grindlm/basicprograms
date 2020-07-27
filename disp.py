#!/usr/bin/env python
import sys
import matplotlib.pyplot as plt
import numpy as np

args = sys.argv[1:]
num_args = len(args)

thesecolors=['black','grey','blue','red','green','purple']

for i in range(num_args):
	disp=np.genfromtxt(args[i])
	thisx=(disp[:,0])
	thisy=(disp[:,1])
	if len(thisy)==1248:
		xposition=[227,489,624,(624+227),(624+489)]
	elif len(thisy)==1853:
		xposition=[227,489,624,(624+227),(624+489),1248,(1248+389),(1248+510)]
	elif len(thisy)==2458:
		xposition=[227,489,624,(624+227),(624+489),1248,(1248+389),(1248+510),1853,(1853+389),(1853+510)]
	else:
		xposition=[]
	plt.plot(thisx,thisy,color=thesecolors[i])
for xc in xposition:
	if xc==624 or xc==1248 or xc==1853:
		plt.axvline(x=xc,color='k',linestyle='-')
	else:
		plt.axvline(x=xc, color='grey',linestyle='--')
plt.xlabel('Residue Number')
plt.ylabel(r'$\delta$q($\AA$)')

plt.show()
