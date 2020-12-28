#!/usr/bin/env python
from sys import argv
import matplotlib.pyplot as plt
import numpy as np

script, bfac_file  = argv

bfacs = np.genfromtxt(bfac_file)
number_of_modes = len(bfacs[0]-2)

print(f"This is the number of lines in bfacs {len(bfacs[:,1])}. it has {len(bfacs[0])-2} modes.")

fig, ax = plt.subplots(figsize=(12,8), dpi=300)
thesecolors=['black','blue','red','green','purple']
residues = bfacs[:,0]

htpg_length=1248
dnak_length=605
htpg_domains =np.array([227, 489, 624])
dnak_domains = np.array([383, 510, 605])
list_of_domains = []
list_of_domain_names = []
list_of_domain_colors = []
htpg_domain_names = [r"NTD$_{(GA)}$",r"MD$_{(GA)}$",r"CTD$_{(GA)}$",r"NTD$_{(GB)}$",r"MD$_{(GB)}$",r"CTD$_{(GB)}$"]
dnak_domain_namesA = [r"NBD$_{(KA)}$",r"SBD$\beta_{(KA)}$",r"SBD$\alpha_{(KA)}$"]
dnak_domain_namesB = [r"NBD$_{(KB)}$",r"SBD$\beta_{(KB)}$",r"SBD$\alpha_{(KB)}$"]
htpg_domain_colors = ['gold', 'green', 'blue', 'gold', 'green', 'blue']
dnak_domain_colors = ['grey', 'red', 'salmon']
mode_color = []
list_of_modes = []

if len(bfacs[:,0])>=htpg_length:
	list_of_domains.extend(htpg_domains)
	list_of_domains.extend(htpg_domains+624)
	list_of_domain_names.extend(htpg_domain_names)
	list_of_domain_colors.extend(htpg_domain_colors)
	list_of_modes = ["Sum of B factors","Mode 7", "Mode 8"]
if len(bfacs[:,0])>=(htpg_length+dnak_length):
	list_of_domains.extend((htpg_length+dnak_domains))
	list_of_domain_names.extend(dnak_domain_namesA)
	list_of_domain_colors.extend(dnak_domain_colors)
	list_of_modes = ["Sum of B factors","Mode 10", "Mode 8"]
if len(bfacs[:,0])>=(htpg_length+dnak_length+dnak_length):
	list_of_domains.extend((htpg_length + dnak_length + dnak_domains))
	list_of_domain_names.extend(dnak_domain_namesB)
	list_of_domain_colors.extend(dnak_domain_colors)
	list_of_modes = ["Sum of B factors", "Mode 13", "Mode 28", "Mode 8"]
print(f"These are the domains {list_of_domains}")
print(f"These are the domain names {list_of_domain_names}")
print(f"These are the domain colors {list_of_domain_colors}")
print(f"These are the modes {list_of_modes}")

for i in range(len(bfacs[0])-1):
	ax.plot(bfacs[:,0], bfacs[:,i+1], color=thesecolors[i], linewidth = 2, label = list_of_modes[i])
ax.legend()	
all_domains = [0]
all_domains.extend(list_of_domains)
xmin, xmax = ax.get_xlim()
ymin, ymax = ax.get_ylim()
for j in range(len(list_of_domains)):
	ax.text((all_domains[j]+all_domains[j+1])*0.5, ymax+0.015, f"{list_of_domain_names[j]}", verticalalignment='bottom', weight='bold', rotation=45, fontsize=20, color=list_of_domain_colors[j])
plt.xticks(rotation=45, fontsize=15, weight='bold')
plt.yticks(fontsize=15, weight='bold')
plt.xlabel('Residue Number', fontsize=25, weight='bold')
plt.ylabel(r'$\delta$q($\AA$)', fontsize=25, weight='bold')
plt.tight_layout()
plt.ylim(0, ymax+0.01)
ax.vlines(list_of_domains, 0, ymax+0.01, colors = 'k', linestyle='--')
plt.savefig(f"testestest{bfac_file[:-4]}-figure.svg")
