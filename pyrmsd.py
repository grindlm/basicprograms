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
def ymax(domain):
	return (max(domain[:,1]) + 5)

fig, ax = plt.subplots(figsize=(10,6))
#plt.plot(xdat,ydat)
plt.xlabel('Residue', fontsize='large')
plt.ylabel('$\delta$q($\AA$)',fontsize='large')

if len(xdat)<623:
	ax.axvline(x=383,color='k',linestyle='--')
	ax.axvline(x=510, color='k',linestyle='--')
	nbddat=data[:383]
	linker=data[383:391]
	sbdbetdat=data[390:509]
	sbdalpdat=data[510:]
	ax.text(373,ymax(sbdalpdat)+3,'383',fontsize='small')
	ax.text(500,ymax(sbdalpdat)+3,'510',fontsize='small')
	ax.plot(nbddat[:,0],nbddat[:,1],color='grey')
	ax.text(((383/2)),(ymax(nbddat)),'NBD',color='grey',fontsize='x-large')
	ax.plot(linker[:,0],linker[:,1],color='cyan')
	ax.plot(sbdbetdat[:,0],sbdbetdat[:,1],color='red')
	ax.text(((383+383+510)/3),(ymax(sbdbetdat)), r'SBD$\beta$',color='red',fontsize='x-large')
	ax.plot(sbdalpdat[:,0],sbdalpdat[:,1],color='salmon')
	ax.text(((510+605+510)/3),(ymax(sbdalpdat)-10), r'SBD$\alpha$',color='salmon',fontsize='x-large')
else:
	nbddat = data[:226]
	mddat = data[227:488]
	ctddat = data[488:624]
	ax.axvline(x=227,color='k',linestyle='--')
	ax.text(217,82,'227',fontsize='small')
	ax.axvline(x=489,color='k',linestyle='--')
	ax.text(477,82,'489',fontsize='small')
	#ax.plot([1,227],[ym,ym], label='NTD', color='yellow')
	#ax.plot([227,489],[ym,ym], label='MD', color='forestgreen')
	#ax.plot([489,624],[ym,ym], label='CTD', color='blue')
	ntd=227/2
	md=(227+489)/2
	ctd=(489+624)/2
	ax.text(ntd,(ymax(nbddat)-10),'NTD',color='gold',fontsize='x-large')
	ax.text(md,(ymax(mddat)-12),'MD', color='forestgreen',fontsize='x-large')
	ax.text(ctd,(ymax(ctddat)-10),'CTD',color='blue',fontsize='x-large')
	ax.plot(nbddat[:,0],nbddat[:,1],color='gold')
	ax.plot(mddat[:,0],mddat[:,1],color='forestgreen')
	ax.plot(ctddat[:,0],ctddat[:,1],color='blue')
	if len(xdat) > 625:
		nbddat2 = data[625:(625+226)]
		mddat2 = data[(625+227):(625+488)]
		ctddat2 = data[(625+488):1248]
		ax.axvline(x=624,color='k',linestyle='-')
		ax.axvline(x=(624+227),color='k',linestyle='--')
		ax.axvline(x=(624+489),color='k',linestyle='--')
		ax.plot(nbddat2[:,0],nbddat2[:,1], label='NTD', color='gold')
		ax.plot(mddat2[:,0],mddat2[:,1],color='forestgreen')
		ax.plot(ctddat2[:,0],ctddat2[:,1],color='blue')

plt.show()
