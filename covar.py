#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys
import math
import psutil

# how do I make a covariance plot?

#load data

args = sys.argv[1:]
num_args = len(args)
if num_args > 1:
	print('too many plot arguments')
	sys.exit()
df = pd.read_csv(args[0],sep='\t', header=None, names=['x','y','cov'], dtype={'x':int, 'y':int, 'cov':float})

result = df.pivot_table(index='x',columns='y',values='cov')
resulted = result.sort_values('x', ascending=False)

fig, ax = plt.subplots()

hm = sns.heatmap(resulted, center=0, cmap='coolwarm', square=True)
plt.xlabel('Residue Number')
plt.ylabel('Residue Number')

dom = [227,489,624,(624+227),(624+489),1248,(1248+390),(1248+510)]
dominv=[]
for i in range(len(dom)):
	dominv.append(abs(dom[i]-1853))
	dominv.sort()
ax.vlines(dom, 0, 1853, linewidth=2, color='k')
ax.hlines(dominv, 0, 1853, linewidth=2,color='k')


plt.xticks(np.arange(100,1853,step=100),np.arange(100,1853, step=100), rotation=45)
plt.yticks([53, 153, 253, 353, 453, 553, 653, 753, 853, 953, 1053, 1153, 1253, 1353, 1453, 1553, 1653, 1753, 1853], [1800,1700,1600,1500,1400,1300,1200,1100,1000,900,800,700,600,500,400,300,200,100,0])

#plt.xticks([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300,1400,1500,1600,1700,1800,1853])
#plt.yticks([0, 53, 153, 253, 353, 453, 553, 653, 753, 853, 953, 1053, 1153, 1253, 1353, 1453, 1553, 1653, 1753, 1853])
plt.show()
