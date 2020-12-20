#!/usr/bin/env python
from sys import argv
import matplotlib.pyplot as plt
import numpy as np

script, bfac_file  = argv

bfacs = np.genfromtxt(bfac_file)
number_of_modes = len(bfacs[0]-2)

print(f"This is the number of lines in bfacs {len(bfacs[:,1])}. it has {len(bfacs[0])-2} modes.")

fig, ax = plt.subplots(figsize=(12,8), dpi=300)
thesecolors=['black','blue','red','green','purple','purple']
residues = bfacs[:,0]

htpg_length=1248
dnak_length=605
htpg_domains =np.array([227, 489, 624])
dnak_domains = np.array([383, 510, 605])
list_of_domains = []
list_of_domain_names = []
htpg_domain_names = ["NTD","MD","CTD"]
dnak_domain_names = ["NBD",r"SBD\beta",r"SBD\alpha"]

if len(bfacs[:,0])>=htpg_length:
	list_of_domains.extend(htpg_domains)
	list_of_domains.extend(htpg_domains+624)
if len(bfacs[:,0])>=(htpg_length+dnak_length):
	list_of_domains.extend((htpg_length+dnak_domains))
if len(bfacs[:,0])>=(htpg_length+dnak_length+dnak_length):
	list_of_domains.extend((htpg_length + dnak_length + dnak_domains))
print(f"These are the domains {list_of_domains}")

for i in range(len(bfacs[0])-1):
	ax.plot(bfacs[:,0], bfacs[:,i+1], color=thesecolors[i], linewidth = 3)

plt.xticks(rotation=45, fontsize=15, weight='bold')
plt.yticks(fontsize=15, weight='bold')
plt.xlabel('Residue Number', fontsize=25, weight='bold')
plt.ylabel(r'$\delta$q($\AA$)', fontsize=25, weight='bold')

xmin, xmax = ax.get_xlim()
ymin, ymax = ax.get_ylim()

plt.tight_layout()
plt.ylim(0, ymax+0.01)
ax.vlines(list_of_domains, 0, ymax+0.01, colors = 'k', linestyle='--')
plt.savefig(f"thisisabfactest{bfac_file[:-4]}.png")
