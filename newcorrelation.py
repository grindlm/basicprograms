#!/usr/bin/env python

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import sys 
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

#sekect the argument that we want (Just the first one)
args = sys.argv[1:]
num_args = len(args)

# Read the file as a .csv so we can get the values that we want, then list them in reverse order because that's how the heatmap function works in python
data_frame = pd.read_csv(args[0],sep='\t',header=None)
sorted_data_frame = data_frame[::-1]

length_of_complex = len(args)

#These are the lengths of the proteins that we are working with so I don't have to remember them the whole time
G_length = 1248
K_length = 605
E2_length = 318
J2_length = 752

GA_NTD = 227
GA_MD = 489
GA_CTD = 624
GB_NTD = 624 + 227
GB_MD = 624 + 489
GB_CTD = 624 + 624
K_NBD = 383
K_SBDB = 510
K_SBDA = 605
E_Length = 156
JA_JD = 70
JA_CTD = 376
JB_JD = 376 + 70
JB_CTD = 376 + 376

working_complexes = []
list_of_complexes = [G_length, K_length, E2_length, J2_length]

#this is going to find the complexes we are using
def find_complexes():
	for i in len(list_of_complexes):
		if (length_of_complex - list_of_complexes[i])==0:
			working_complexes.append(list_of_complexes[i])
			return
		for j in len(list_of_complexes):
			if (length_of_complex - list_of_complexes[i] - list_of_complexes[j])==0:
				working_complexes.append(list_of_complexes[i])
				working_complexes.append(list_of_complexes[j])
				return
			for k in len(list_of_complexes):
				if (length_of_complex - list_of_complexes[i] - list_of_complexes[j] -list_of_complexes[k])==0:
					working_complexes.append(list_of_complexes[i])
					working_complexes.append(list_of_complexes[j])
					working_complexes.append(list_of_complexes[k])
					return
find_complexes()

fig, ax = plt.subplots(figsize=(30,30))

# This section is describing the exact colors that I want for the heatmap
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
# Create the heatmap with all the data
covariance_map = sns.heatmap(dfsorted, cmap=newcmp,center=0,square=True)
# from here out, the program is adding fluorishes like lines, labels, and residue numbers

list_of_domain_lengths = [[GA_NTD, GA_MD, GA_CTD, GB_NTD, GB_MD, GB_CTD], [K_NBD, K_SBDB, K_SBDB], [E_length, E2_length], [JA_JD, JA_CTD, JB_JD, JB_CTD]]
list_of_domain_names = [[r'NTD$_{(GA)}$', r'MD$_{(GA)}$', r'CTD$_{(GA)}$', r'NTD$_{(GB)}$', r'MD$_{(GB)}$', r'CTD$_{(GB)}$'], [r'NBD$_{(K)}$', r'SBD$\beta_{(K)}$', r'SBD$\alpha_{(K)}$'], [r'GrpE$_{(A)}$', r'GrpE$_{(B)}$'], [r'JD$_{(JA)}$', r'CTD$_{(JA)}$', r'JD$_{(JB)}$', r'CTD$_{(JB)}$']]
list_of_domain_colors = [['gold', 'forestgreen', 'blue', 'gold', 'forestgreen', 'blue'], ['grey', 'red', 'salmon'], ['orange'], ['cyan','purple','cyan','purple']]

# this will make some lines
def make_graph_lines():
	inverted_domain_lengths = []
	for i in len(working_complexes):
		for j in len(list_of_complexes):
			if working_complexes[i]==list_of_complexes[j]:
				for k in len(list_of_domain_lengths[j]):
					ax.vlines(list_of_domain_lengths[j][k], 0, length_of_complex, linewidth=3, color='k')
					#domains must be inverted for horizontal lines
					inverted_domain_lengths.append(abs(list_of_domain_lengths[j][k]-length_of_complex)).sort()
					ax.hlines(inverted_domain_lengths[k], 0, length_of_complex, linewidth=3, color='k')
					
					
				
				
			
		
			
ax.text(length_of_complex, (-0.002*length_of_complex), f"{length_of_complex}", ha='center', fontsize=8)		



