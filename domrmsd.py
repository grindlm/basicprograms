#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib
# this is a python script to graph the rmsds of htpg systems

matplotlib.rcParams.update({'font.size': 18})

data=np.genfromtxt(sys.argv[1])

if len(sys.argv) > 2:
	sys.exit('too many args')
	
nbddat = data[:226]
mddat = data[227:488]
ctddat = data[488:]

ntd=227/2
md=(227+489)/2
ctd=(489+624)/2

for i in [nbddat,mddat,ctddat]:
	ym = max(i[:,1])
	if i[0,0]==1:
		plt.text(ntd,(ym-5),'NTD',color='green')
	elif 1<i[0,0]<450:
		plt.text(md,(ym-5),'MD', color='orange')
	else:
		plt.text(ctd,(ym-5),'CTD',color='blue')

plt.plot(nbddat[:,0],nbddat[:,1],color='green')
plt.plot(mddat[:,0],mddat[:,1],color='orange')
plt.plot(ctddat[:,0],ctddat[:,1],color='blue')
plt.xlabel('Residue')
plt.ylabel('$\delta$q($\AA$)')

plt.axvline(x=227,color='k',linestyle='--')
plt.axvline(x=489,color='k',linestyle='--')

plt.show()
