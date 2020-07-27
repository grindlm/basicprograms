#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import sys
# this is a python script to graph the rmsds of htpg systems

data=np.genfromtxt(sys.argv[1])

if len(sys.argv) > 2:
	sys.exit('too many args')
	
xdat = data[:,0]
ydat = data[:,1]
ym = max(ydat) + 5

#plt.plot(xdat,ydat)
plt.xlabel('Residue')
plt.ylabel('$\delta$q($\AA$)')

if len(xdat)<623:
	plt.axvline(x=383,color='k',linestyle='--')
	plt.axvline(x=510, color='k',linestyle='--')
	nbddat=data[:383]
	sbdbetdat=data[384:509]
	sbdalpdat=data[510:]
	plt.plot(nbddat[:,0],nbddat[:,1],color='grey')
	plt.plot(sbdbetdat[:,0],sbdbetdat[:,1],color='purple')
	plt.plot(sbdalpdat[:,0],sbdalpdat[:,1],color='teal')
else:
	nbddat = data[:226]
	mddat = data[227:488]
	ctddat = data[488:624]
	plt.axvline(x=227,color='k',linestyle='--')
	plt.axvline(x=489,color='k',linestyle='--')
	plt.plot([1,227],[ym,ym], label='NTD', color='green')
	plt.plot([227,489],[ym,ym], label='MD', color='orange')
	plt.plot([489,624],[ym,ym], label='CTD', color='blue')
	plt.plot(nbddat[:,0],nbddat[:,1],color='green')
	plt.plot(mddat[:,0],mddat[:,1],color='orange')
	plt.plot(ctddat[:,0],ctddat[:,1],color='blue')
	if len(xdat) > 625:
		nbddat2 = data[625:(625+226)]
		mddat2 = data[(625+227):(625+488)]
		ctddat2 = data[(625+488):1248]
		plt.axvline(x=624,color='k',linestyle='-')
		plt.axvline(x=(624+227),color='k',linestyle='--')
		plt.axvline(x=(624+489),color='k',linestyle='--')
		plt.plot(nbddat2[:,0],nbddat2[:,1], label='NTD', color='green')
		plt.plot(mddat2[:,0],mddat2[:,1],color='orange')
		plt.plot(ctddat2[:,0],ctddat2[:,1],color='blue')


plt.show()

#	ntd=227/2
#	md=(227+489)/2
#	ctd=(489+624)/2
#	plt.text(ntd,(ym-5),'NTD',color='green')
#	plt.text(md,(ym-5),'MD', color='orange')
#	plt.text(ctd,(ym-5),'CTD',color='blue')
#		plt.text((624+ntd),(ym-5),'NTD',color='green')
#		plt.text((624+md),(ym-5),'MD', color='orange')
#		plt.text((624+ctd),(ym-5),'CTD',color='blue')
