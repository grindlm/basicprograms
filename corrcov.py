#!/usr/bin/env python

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import sys
import math
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

args = sys.argv[1:]
num_args = len(args)

df = pd.read_csv(args[0],sep='\t',header=None)
dfsorted = df[::-1]

length_of_complex = len(df[0])

fig, ax = plt.subplots(figsize=(30,30))

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
newcmp = ListedColormap(vals)

hm = sns.heatmap(dfsorted, cmap=newcmp,center=0,square=True)

if length_of_complex==1248:
	fntsz = 16
	dom = [227,489,624,(624+227),(624+489)]
	domainname = [r'NTD$_{(GA)}$', r'MD$_{(GA)}$', r'CTD$_{(GA)}$', r'NTD$_{(GB)}$', r'MD$_{(GB)}$', r'CTD$_{(GB)}$']
	domaincolor = ['gold', 'forestgreen', 'blue', 'gold', 'forestgreen', 'blue']
<<<<<<< HEAD
	plt.yticks([48,148,248,348,448,548,648,748,848,948,1048,1148,1248],[1200,1100,1000,900,800,700,600,500,400,300,200,100,0], fontsize=16)
	plt.xticks([0,100,200,300,400,500,600,700,800,900,1000,1100,1200],np.arange(0,1201,step=100),rotation=45, fontsize=16)
=======
	plt.yticks([48,148,248,348,448,548,648,748,848,948,1048,1148,1248],[1200,1100,1000,900,800,700,600,500,400,300,200,100,0], fontsize=12)
	plt.xticks([0,100,200,300,400,500,600,700,800,900,1000,1100,1200],np.arange(0,1201,step=100),rotation=45, fontsize=12)
elif length_of_complex==1357:
	fntsz = 16
	dom = [390,510,605,(605+110),(605+254),(376+605),(376+605+110),(376+605+254)]
	domainname = [r'NBD$_{(K)}$', r'SBD$\beta_{(K)}$', r'SBD$\alpha_{(K)}$', r'JD$_{(JA)}$', r'CTDI$_{(JA)}$', r'CTDII$_{(JA)}$ ', r'JD$_{(JB)}$', r'CTDI$_{(JB)}$', r'CTDII$_{(JB)}$']
	domaincolor = ['grey','red','salmon','cyan','violet','purple','cyan','violet','purple']
	plt.xticks([0,100,200,300,400,500,600,700,800,900,1000,1100,1200,1300],np.arange(0,1301,step=100),rotation=45, fontsize=12)
	plt.yticks([57,157,257,357,457,557,657,757,857,957,1057,1157,1257,1357],[1300,1200,1100,1000,900,800,700,600,500,400,300,200,100,0], fontsize=12)
elif length_of_complex==923:
	fntsz = 16
	dom = [390,510,605,605+159]
	domainname = [r'NBD$_{(K)}$', r'SBD$\beta_{(K)}$', r'SBD$\alpha_{(K)}$', r'GrpE$_{(A)}$', r'GrpE$_{(B)}$']
	domaincolor = ['grey','red','salmon','orange','orange']
	plt.xticks([0,100,200,300,400,500,600,700,800,900],np.arange(0,901,step=100),rotation=45, fontsize=12)
	plt.yticks([23,123,223,323,423,523,623,723,823,923],[900,800,700,600,500,400,300,200,100,0], fontsize=12)
>>>>>>> 3d6c850c01ed788b5d3345180af04b309e6b8fcf
elif length_of_complex==1853 and "dnakatend" not in args[0]:
	fntsz = 14
	dom = [227,489,624,(624+227),(624+489),1248,(1248+390),(1248+510)]
	domainname = [r'NTD$_{(GA)}$', r'MD$_{(GA)}$', r'CTD$_{(GA)}$', r'NTD$_{(GB)}$', r'MD$_{(GB)}$', r'CTD$_{(GB)}$', r'NBD$_{(K)}$', r'SBD$\beta_{(K)}$', r'SBD$\alpha_{(K)}$']
	domaincolor = ['gold', 'forestgreen', 'blue', 'gold', 'forestgreen', 'blue', 'grey', 'red', 'salmon']
	plt.xticks(np.arange(0,1853,step=100),np.arange(0,1853,step=100),rotation=45, fontsize=16)
	plt.yticks([53,153,253,353,453,553,653,753,853,953,1053,1153,1253,1353,1453,1553,1653,1753,1853],[1800,1700,1600,1500,1400,1300,1200,1100,1000,900,800,700,600,500,400,300,200,100,0], fontsize=16)
elif length_of_complex==1853 and "dnakatend" in args[0]:
	fntsz = 14
	dom = [227,489,624,(624+227),(624+489),1248,(1248+390),(1248+510)]
	domainname = [r'NTD$_{(GA)}$', r'MD$_{(GA)}$', r'CTD$_{(GA)}$', r'NTD$_{(GB)}$', r'MD$_{(GB)}$', r'CTD$_{(GB)}$', r'NBD$_{(K)}$', r'SBD$\beta_{(K)}$', r'SBD$\alpha_{(K)}$']
	domaincolor = ['gold', 'forestgreen', 'blue', 'gold', 'forestgreen', 'blue', 'grey', 'red', 'salmon']
	plt.xticks(np.arange(0,1853,step=100),np.arange(0,1853,step=100),rotation=45, fontsize=16)
	plt.yticks([53,153,253,353,453,553,653,753,853,953,1053,1153,1253,1353,1453,1553,1653,1753,1853],[1800,1700,1600,1500,1400,1300,1200,1100,1000,900,800,700,600,500,400,300,200,100,0], fontsize=16)
elif length_of_complex==2458:
	fntsz = 9
	dom = [227,489,624,(624+227),(624+489),1248,(1248+390),(1248+510),1853,(1853+390),(1853+510)]
	domainname = [r'NTD$_{(GA)}$', r'MD$_{(GA)}$', r'CTD$_{(GA)}$', r'NTD$_{(GB)}$', r'MD$_{(GB)}$', r'CTD$_{(GB)}$', r'NBD$_{(KA)}$', r'SBD$\beta_{(KA)}$', r'SBD$\alpha_{(KA)}$', r'NBD$_{(KB)}$', r'SBD$\beta_{(KB)}$', r'SBD$\alpha_{(KB)}$']
	domaincolor = ['gold', 'forestgreen', 'blue', 'gold', 'forestgreen', 'blue', 'grey', 'red', 'salmon', 'grey', 'red', 'salmon']
	plt.xticks(np.arange(0,2458,step=100),np.arange(0,2458,step=100),rotation=45, fontsize=16)
	plt.yticks([58,158,258,358,458,558,658,758,858,958,1058,1158,1258,1358,1458,1558,1658,1758,1858, 1958,2058,2158,2258,2358,2458],[2400,2300,2200,2100,2000,1900,1800,1700,1600,1500,1400,1300,1200,1100,1000,900,800,700,600,500,400,300,200,100,0], fontsize=16)
elif length_of_complex==605:
	fntsz = 16
	dom = [390,510]
	domainname = [r'NBD$_{(K)}$', r'SBD$\beta_{(K)}$', r'SBD$\alpha_{(K)}$']
	domaincolor = ['grey', 'red', 'salmon']
	plt.xticks(np.arange(0,601,step=100),np.arange(0,601,step=100),rotation=45, fontsize=16)
	plt.yticks([5,105,205,305,405,505,605],[600,500,400,300,200,100,0], fontsize=16)
elif length_of_complex==604:
	fntsz = 16
	dom = [390,510]
	domainname = [r'NBD$_{(K)}$', r'SBD$\beta_{(K)}$', r'SBD$\alpha_{(K)}$']
	domaincolor = ['grey', 'red', 'salmon']
	plt.xticks(np.arange(0,601,step=100),np.arange(0,601,step=100),rotation=45, fontsize=16)
	plt.yticks([4,104,204,304,404,504,604],[600,500,400,300,200,100,0], fontsize=16)
elif length_of_complex==624:
	fntsz = 20
	dom = [227,489]
	domainname = ['NTD', 'MD', 'CTD', 'NTD', 'MD', 'CTD']
	domaincolor = ['gold', 'forestgreen', 'blue']
elif length_of_complex==1357:
	fntsz = 20
	dom = [390,510,605,981]
<<<<<<< HEAD
	plt.xticks(np.arange(0,1357,step=100),np.arange(0,1357,step=100),rotation=45, fontsize=16)
	plt.yticks([57,157,257,357,457,557,657,757,857,957,1057,1157,1257,1357],[1300,1200,1100,1000,900,800,700,600,500,400,300,200,100,0], fontsize=16)
elif length_of_complex==923:
	fntsz = 20
	dom = []
=======
	plt.xticks(np.arange(0,1357,step=100),np.arange(0,1357,step=100),rotation=45, fontsize=12)
	plt.yticks([57,157,257,357,457,557,657,757,857,957,1057,1157,1257,1357],[1300,1200,1100,1000,900,800,700,600,500,400,300,200,100,0], fontsize=12)
>>>>>>> 3d6c850c01ed788b5d3345180af04b309e6b8fcf
else:
	fntsz = 20
	dom = []
	print(length_of_complex, "is not an expected number of residues")

dominv=[]
if len(dom)>0:
	if len(dom) > 3:
		ax.text(length_of_complex,(-0.002*length_of_complex),f"{length_of_complex - dom[-2]}",ha='center', fontsize=8)
	else:
		ax.text(length_of_complex,(-0.002*length_of_complex),f"{length_of_complex}",ha='center', fontsize=8)
	for i in range(len(dom)):
		if i == 0:
			ax.text(dom[i]/2,(-0.03*length_of_complex), "{}".format(domainname[i]),ha='center', rotation=45,fontsize=fntsz, color=f"{domaincolor[i]}")
			print("first domain --> {} {} {}".format(dom[i], domainname[i], domaincolor[i]))
		elif dom[i] == dom[-1]:
			ax.text((dom[i]+dom[i-1])/2, (-0.03*length_of_complex), "{}".format(domainname[i]),ha='center',fontsize=fntsz,rotation=45, color=f"{domaincolor[i]}")
			ax.text((dom[i]+length_of_complex)/2, (-0.03*length_of_complex), "{}".format(domainname[i+1]), fontsize=fntsz, rotation=45, color=f"{domaincolor[i+1]}")
			print("This is the {} domain --> {} {} {}".format(i, dom[i], domainname[i], domaincolor[i]))
			print("{} domain --> {} {} {}".format(i+1, dom[i], domainname[i+1], domaincolor[i+1]))
		else:
			if domainname[i]==r'SBD$\alpha_{(KA)}$':
				hac = 'left'
			else:
				hac = 'center'
			ax.text((dom[i]+dom[i-1])/2, (-0.03*length_of_complex), "{}".format(domainname[i]),ha=hac,fontsize=fntsz, color=f"{domaincolor[i]}", rotation=45)
			print("{} domain --> {} {} {}".format(i, dom[i], domainname[i], domaincolor[i]))
		if dom[i] < 624:
			ax.text(dom[i],(-0.002*length_of_complex),f"{dom[i]}",fontsize=8, ha='center')
		elif 624 <= dom[i] < 1248:
			ax.text(dom[i], (-0.002*length_of_complex),f"{dom[i] - 624}",fontsize=8, ha='center')
		elif 1248 <= dom[i] < 1853:
			ax.text(dom[i], (-0.002*length_of_complex),f"{dom[i] - 1248}",fontsize=8, ha='center')
		elif 1853 <= dom[i] < 2458:
			ax.text(dom[i], (-0.002*length_of_complex),f"{dom[i] - 1853}",fontsize=8, ha='center')
		dominv.append(abs(dom[i]-length_of_complex))
		dominv.sort()
	ax.vlines(dom, 0, length_of_complex, linewidth=3, color='k')
	ax.hlines(dominv, 0, length_of_complex, linewidth=3,color='k')

plt.xlabel('Residue Number', fontsize=15)
plt.ylabel('Residue Number', fontsize=15)

print(dom, dominv, length_of_complex)

plt.show()
