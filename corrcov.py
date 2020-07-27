#!/usr/bin/env python

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import sys 
import math
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib import cm

args = sys.argv[1:]
num_args = len(args)

df = pd.read_csv(args[0],sep='\t',header=None)
dfsorted = df[::-1]

length_of_complex = len(df[0])

fig, ax = plt.subplots()

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
	dom = [227,489,624,(624+227),(624+489)]
	plt.yticks([48,148,248,348,448,548,648,748,848,948,1048,1148,1248],[1200,1100,1000,900,800,700,600,500,400,300,200,100,0])
	plt.xticks([0,100,200,300,400,500,600,700,800,900,1000,1100,1200],np.arange(0,1201,step=100),rotation=45)
elif length_of_complex==1853:
	dom = [227,489,624,(624+227),(624+489),1248,(1248+390),(1248+510)]
	plt.xticks(np.arange(0,1853,step=100),np.arange(0,1853,step=100),rotation=45)
	plt.yticks([53,153,253,353,453,553,653,753,853,953,1053,1153,1253,1353,1453,1553,1653,1753,1853],[1800,1700,1600,1500,1400,1300,1200,1100,1000,900,800,700,600,500,400,300,200,100,0])
elif length_of_complex==2458:
	dom = [227,489,624,(624+227),(624+489),1248,(1248+390),(1248+510),1853,(1853+390),(1853+510)]
	plt.xticks(np.arange(0,2458,step=100),np.arange(0,2458,step=100),rotation=45)
	plt.yticks([58,158,258,358,458,558,658,758,858,958,1058,1158,1258,1358,1458,1558,1658,1758,1858, 1958,2058,2158,2258,2358,2458],[2400,2300,2200,2100,2000,1900,1800,1700,1600,1500,1400,1300,1200,1100,1000,900,800,700,600,500,400,300,200,100,0])
elif length_of_complex==605:
	dom = [390,510]
	plt.xticks(np.arange(0,601,step=100),np.arange(0,601,step=100),rotation=45)
	plt.yticks([5,105,205,305,405,505,605],[600,500,400,300,200,100,0])
elif length_of_complex==604:
	dom = [390,510]
	plt.xticks(np.arange(0,601,step=100),np.arange(0,601,step=100),rotation=45)
	plt.yticks([4,104,204,304,404,504,604],[600,500,400,300,200,100,0])
elif length_of_complex==624:
	dom = [227,489]
elif length_of_complex==1357:
	dom = [390,510,605,981]
	plt.xticks(np.arange(0,1357,step=100),np.arange(0,1357,step=100),rotation=45)
	plt.yticks([57,157,257,357,457,557,657,757,857,957,1057,1157,1257,1357],[1300,1200,1100,1000,900,800,700,600,500,400,300,200,100,0])
elif length_of_complex==923:
	dom = []
else:
	dom = []
	print(length_of_complex, "is not an expected number of residues")

dominv=[]
if len(dom)>0:
	for i in range(len(dom)):
		dominv.append(abs(dom[i]-length_of_complex))
		dominv.sort()
	ax.vlines(dom, 0, length_of_complex, linewidth=3, color='k')
	ax.hlines(dominv, 0, length_of_complex, linewidth=3,color='k')

print(dom, dominv, length_of_complex)

plt.show()
