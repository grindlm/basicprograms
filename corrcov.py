#!/usr/bin/env python

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import sys
import math
import matplotlib

args = sys.argv[1]
num_args = len(args)

matplotlib.rcParams['axes.linewidth'] = 3

df = pd.read_csv(args,sep='\t',header=None)
dfsorted = df[::-1]

length_of_complex = len(df[0])

fig, ax = plt.subplots(figsize=(15,15), dpi=300)

font = {'weight' : 'bold',
	'size' : 28}
matplotlib.rc('font', **font)

N=256
vals = np.ones((N,4))
vals[0:26, 2] = np.linspace(0.5,1,26)
vals[27:132, 2] = 1
vals[132:178, 2] = np.linspace(0.89,0,46)
vals[178:256, 2] = 0

vals[0:26, 1] = 0
vals[26:108, 1] = np.linspace(0,1,82)
vals[108:148, 1] = 1
vals[148:230, 1] = np.linspace(1,0,82)
vals[229:256, 1] = 0

vals[0:78, 0] = 0
vals[78:124, 0] = np.linspace(0,1,46)
vals[124:229, 0] = 1
vals[229:256, 0] = np.linspace(1,0.5,27)
newcmp = matplotlib.colors.ListedColormap(vals)

hm = sns.heatmap(dfsorted, cmap=newcmp,center=0,square=True, cbar_kws={"shrink": 0.5})
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(labelsize=15)
cbar.set_ticks([-0.99, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1])
cbar.set_ticklabels(["-1.00","-0.75","-0.50","-0.25","0", "0.25", "0.50", "0.75", "1.00"])
if length_of_complex==1248:
	dom = [227,489,624,(624+227),(624+489)]
	domainname = [r'NTD$_{(GA)}$', r'MD$_{(GA)}$', r'CTD$_{(GA)}$', r'NTD$_{(GB)}$', r'MD$_{(GB)}$', r'CTD$_{(GB)}$']
	domaincolor = ['gold', 'forestgreen', 'blue', 'gold', 'forestgreen', 'blue']
	plt.yticks([48,248,448,648,848,1048,1248],[1200,1000,800,600,400,200,0], fontsize = 25, weight='bold')
	plt.xticks([0,200,400,600,800,1000,1200],np.arange(0,1201,step=200),rotation=45, fontsize = 25, weight='bold')
elif length_of_complex==1357:
	dom = [390,510,605,(605+110),(605+254),(376+605),(376+605+110),(376+605+254)]
	domainname = [r'NBD$_{(K)}$', r'SBD$\beta_{(K)}$', r'SBD$\alpha_{(K)}$', r'JD$_{(JA)}$', r'CTDI$_{(JA)}$', r'CTDII$_{(JA)}$ ', r'JD$_{(JB)}$', r'CTDI$_{(JB)}$', r'CTDII$_{(JB)}$']
	domaincolor = ['grey','red','salmon','cyan','violet','purple','cyan','violet','purple']
	plt.xticks([0,200,400,600,800,1000,1200],np.arange(0,1301,step=200),rotation=45, fontsize = 25, weight='bold')
	plt.yticks([57,257,457,657,857,1057,1257],[1200,1000,800,600,400,200,0], fontsize = 25, weight='bold')
elif length_of_complex==923:
	dom = [390,510,605,605+159]
	domainname = [r'NBD$_{(K)}$', r'SBD$\beta_{(K)}$', r'SBD$\alpha_{(K)}$', r'GrpE$_{(A)}$', r'GrpE$_{(B)}$']
	domaincolor = ['grey','red','salmon','orange','orange']
	plt.xticks([0,200,400,600,800],np.arange(0,901,step=200),rotation=45, fontsize = 25, weight='bold')
	plt.yticks([23,223,423,623,823],[800,600,400,200,0], fontsize = 25, weight='bold')
elif length_of_complex==1853 and "dnakatend" not in args:
	dom = [227,489,624,(624+227),(624+489),1248,(1248+390),(1248+510)]
	domainname = [r'NTD$_{(GA)}$', r'MD$_{(GA)}$', r'CTD$_{(GA)}$', r'NTD$_{(GB)}$', r'MD$_{(GB)}$', r'CTD$_{(GB)}$', r'NBD$_{(K)}$', r'SBD$\beta_{(K)}$', r'SBD$\alpha_{(K)}$']
	domaincolor = ['gold', 'forestgreen', 'blue', 'gold', 'forestgreen', 'blue', 'grey', 'red', 'salmon']
	plt.xticks(np.arange(0,1853,step=200),np.arange(0,1853,step=200),rotation=45, fontsize = 25, weight='bold')
	plt.yticks([53,253,453,653,853,1053,1253,1453,1653,1853],[1800,1600,1400,1200,1000,800,600,400,200,0], fontsize = 25, weight='bold')
elif length_of_complex==1853 and "dnakatend" in args:
	dom = [227,489,624,(624+227),(624+489),1248,(1248+390),(1248+510)]
	domainname = [r'NTD$_{(GA)}$', r'MD$_{(GA)}$', r'CTD$_{(GA)}$', r'NTD$_{(GB)}$', r'MD$_{(GB)}$', r'CTD$_{(GB)}$', r'NBD$_{(K)}$', r'SBD$\beta_{(K)}$', r'SBD$\alpha_{(K)}$']
	domaincolor = ['gold', 'forestgreen', 'blue', 'gold', 'forestgreen', 'blue', 'grey', 'red', 'salmon']
	plt.xticks(np.arange(0,1853,step=200),np.arange(0,1853,step=200),rotation=45, fontsize = 25, weight='bold')
	plt.yticks([53,253,453,653,853,1053,1253,1453,1653,1853],[1800,1600,1400,1200,1000,800,600,400,200,0], fontsize = 25, weight='bold')
elif length_of_complex==2458:
	dom = [227,489,624,(624+227),(624+489),1248,(1248+390),(1248+510),1853,(1853+390),(1853+510)]
	domainname = [r'NTD$_{(GA)}$', r'MD$_{(GA)}$', r'CTD$_{(GA)}$', r'NTD$_{(GB)}$', r'MD$_{(GB)}$', r'CTD$_{(GB)}$', r'NBD$_{(KA)}$', r'SBD$\beta_{(KA)}$', r'SBD$\alpha_{(KA)}$', r'NBD$_{(KB)}$', r'SBD$\beta_{(KB)}$', r'SBD$\alpha_{(KB)}$']
	domaincolor = ['gold', 'forestgreen', 'blue', 'gold', 'forestgreen', 'blue', 'grey', 'red', 'salmon', 'grey', 'red', 'salmon']
	plt.xticks(np.arange(0,2458,step=200),np.arange(0,2458,step=200),rotation=45, fontsize =25, weight = 'bold')
	plt.yticks([58,258,458,658,858,1058,1258,1458,1658,1858,2058,2258,2458],[2400,2200,2000,1800,1600,1400,1200,1000,800,600,400,200,0], fontsize = 25, weight = 'bold')
elif length_of_complex==605:
	dom = [390,510]
	domainname = [r'NBD$_{(K)}$', r'SBD$\beta_{(K)}$', r'SBD$\alpha_{(K)}$']
	domaincolor = ['grey', 'red', 'salmon']
	plt.xticks(np.arange(0,601,step=100),np.arange(0,601,step=100),rotation=45, fontsize = 25, weight='bold')
	plt.yticks([5,205,405,605],[600,400,200,0], fontsize = 25, weight='bold')
elif length_of_complex==604:
	dom = [390,510]
	domainname = [r'NBD$_{(K)}$', r'SBD$\beta_{(K)}$', r'SBD$\alpha_{(K)}$']
	domaincolor = ['grey', 'red', 'salmon']
	plt.xticks(np.arange(0,601,step=100),np.arange(0,601,step=100),rotation=45, fontsize = 25, weight='bold')
	plt.yticks([4,204,404,604],[600,400,200,0], fontsize = 25, weight='bold')
elif length_of_complex==624:
	dom = [227,489]
	domainname = ['NTD', 'MD', 'CTD', 'NTD', 'MD', 'CTD']
	domaincolor = ['gold', 'forestgreen', 'blue']
else:
	dom = []
	print(length_of_complex, "is not an expected number of residues")

dominv=[]
if len(dom)>0:
	ax.text(length_of_complex,(-0.002*length_of_complex),f"{length_of_complex-dom[-3]}",ha='center', fontsize = 12)
	for i in range(len(dom)):
		if i == 0:
			ax.text(dom[i]/2,(-0.03*length_of_complex), "{}".format(domainname[i]),ha='left', rotation=45, color=f"{domaincolor[i]}")
			print("first domain --> {} {} {}".format(dom[i], domainname[i], domaincolor[i]))
		elif dom[i] == dom[-1]:
			ax.text((dom[i]+dom[i-1])/2, (-0.03*length_of_complex), "{}".format(domainname[i]),ha='left',rotation=45, color=f"{domaincolor[i]}")
			ax.text((dom[i]+length_of_complex)/2, (-0.03*length_of_complex), "{}".format(domainname[i+1]), rotation=45, color=f"{domaincolor[i+1]}")
			print("This is the {} domain --> {} {} {}".format(i, dom[i], domainname[i], domaincolor[i]))
			print("{} domain --> {} {} {}".format(i+1, dom[i], domainname[i+1], domaincolor[i+1]))
		else:
			hac = 'left'
			ax.text((dom[i]+dom[i-1])/2, (-0.03*length_of_complex), "{}".format(domainname[i]),ha=hac, color=f"{domaincolor[i]}", rotation=45)
			print("{} domain --> {} {} {}".format(i, dom[i], domainname[i], domaincolor[i]))
		if dom[i] < 624:
			ax.text(dom[i],(-0.002*length_of_complex),f"{dom[i]}", ha='center', fontsize = 12)
		elif 624 <= dom[i] < 1248:
			ax.text(dom[i], (-0.002*length_of_complex),f"{dom[i] - 624}", ha='center', fontsize = 12)
		elif 1248 <= dom[i] < 1853:
			ax.text(dom[i], (-0.002*length_of_complex),f"{dom[i] - 1248}", ha='center', fontsize = 12)
		elif 1853 <= dom[i] < 2458:
			ax.text(dom[i], (-0.002*length_of_complex),f"{dom[i] - 1853}", ha='center', fontsize = 12)
		dominv.append(abs(dom[i]-length_of_complex))
		dominv.sort()
	ax.vlines(dom, 0, length_of_complex, linewidth=5, color='k')
	ax.hlines(dominv, 0, length_of_complex, linewidth=5,color='k')

plt.xlabel('Residue Number', fontsize=24, weight = 'bold')
plt.ylabel('Residue Number', fontsize=24, weight = 'bold')
ax.tick_params(direction='out', length=8, width=4)
print(dom, dominv, length_of_complex)

plt.savefig(f"{args[:-4]}.png")
