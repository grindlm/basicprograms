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
secondary_colors = ['grey','deepskyblue','violet','chartreuse']
residues = bfacs[:,0]

htpg_length=1248
dnak_length=605
grpe_length=318
htpg_domains =np.array([227, 489, 624])
dnak_domains = np.array([383, 510, 605])
grpe_domains = np.array([159, 318])
list_of_domains = []
list_of_domain_names = []
list_of_domain_colors = []
htpg_domain_names = [r"NTD$_{(GA)}$",r"MD$_{(GA)}$",r"CTD$_{(GA)}$",r"NTD$_{(GB)}$",r"MD$_{(GB)}$",r"CTD$_{(GB)}$"]
dnak_domain_namesA = [r"NBD$_{(KA)}$",r"SBD$\beta_{(KA)}$",r"SBD$\alpha_{(KA)}$"]
dnak_domain_namesB = [r"NBD$_{(KB)}$",r"SBD$\beta_{(KB)}$",r"SBD$\alpha_{(KB)}$"]
dnak_domain_names = [r"NBD$_{(K)}$",r"SBD$\beta_{(K)}$",r"SBD$\alpha_{(K)}$"]
grpe_domain_names = [r'GrpE$_{(A)}$', r'GrpE$_{(B)}$']
htpg_domain_colors = ['gold', 'green', 'blue', 'gold', 'green', 'blue']
dnak_domain_colors = ['grey', 'red', 'salmon']
grpe_domain_colors = ['orange','chocolate']
mode_color = []
# grpe interactors defined by gierasch bahar 2010 paper
dnak_grpe_interactors = [28,31,49,50,53,56,57,59,60,128,129,130,131,132,257,260,261,264,282,284,285]
# dnak-htpg interactors defined by kravats 2017 paper
dnak_htpg_interactors = [144, 145, 147, 148, 167, 170, 173, 206, 208, 210, 211, 212, 214, 215, 216, 217, 218, 219,220,221,222,223,322,326,327,328,329,386,387,388,389,390,391,392,393] 
# dnak-atp interactors defined by gierasch bahar 2010 paper
dnak_atp_interactors = np.array([12,13,14,15,201,202,203,230,231,268,271,272,275,338,339,340,342,343,366])
atp_interactors = []
nef_interactors = []
list_of_modes = []
dnak_grpe_yvalues=[]
dnak_htpg_yvalues=[]
atp_interactors_yval=[]
if len(bfacs[:,0])==(dnak_length+grpe_length):
	list_of_domains.extend(dnak_domains)
	list_of_domains.extend(grpe_domains+dnak_length)
	list_of_domain_names.extend(dnak_domain_names)
	list_of_domain_names.extend(grpe_domain_names)
	list_of_domain_colors.extend(dnak_domain_colors)
	list_of_domain_colors.extend(grpe_domain_colors)
	atp_interactors.extend(dnak_atp_interactors)
	list_of_modes = ["Sum of B Factors", "Mode 8", "Mode 14", "Mode 16"]
elif len(bfacs[:,0])>=htpg_length:
	list_of_domains.extend(htpg_domains)
	list_of_domains.extend(htpg_domains+624)
	list_of_domain_names.extend(htpg_domain_names)
	list_of_domain_colors.extend(htpg_domain_colors)
	if "-total-compare" not in bfac_file:
		list_of_modes = ["Sum of B factors","Mode 7", "Mode 8"]
	else:
		list_of_modes = ["G-0K","G-1K","G-2K"]
elif len(bfacs[:,0])==dnak_length:
	list_of_domains.extend(dnak_domains)
	list_of_domain_names.extend(dnak_domain_names)
	list_of_domain_colors.extend(dnak_domain_colors)
	if "dnak-adp" in bfac_file:
		list_of_modes = ["Sum of B Factors", "Mode 12", "Mode 7"]
	elif "dnak-grpe-adp-htpg" in bfac_file:
		list_of_modes = ["K-grpe","K-alone","K-G"]
		nef_interactors.extend(dnak_grpe_interactors)
		nef_interactors.extend(dnak_htpg_interactors)
	atp_interactors.extend(dnak_atp_interactors)
if len(bfacs[:,0])>=(htpg_length+dnak_length):
	list_of_domains.extend((htpg_length+dnak_domains))
	list_of_domain_names.extend(dnak_domain_namesA)
	list_of_domain_colors.extend(dnak_domain_colors)
	list_of_modes = ["Sum of B factors","Mode 10", "Mode 8"]
	if "dnak-htpg" in bfac_file:
		list_of_modes = ["Sum of B factors","Mode 19", "Mode 15", "Mode 40"]
		atp_interactors.extend((dnak_atp_interactors+htpg_length))
# Delete later when this becomes a problem
		plt.axis([1248,1853,0,0.1])
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
	for j in range(len(atp_interactors)):
		atp_interactors_yval.append(bfacs[atp_interactors[j],i+1])
	ax.plot(atp_interactors, atp_interactors_yval, 'o', color=secondary_colors[i], ms=8, mew=4, markerfacecolor='none', linestyle='', label=f"{list_of_modes[i]} ATP binding site")
	atp_interactors_yval = []
if 'dnak-grpe-adp' in bfac_file:
	for k in range(len(dnak_grpe_interactors)):
		dnak_grpe_yvalues.append(bfacs[dnak_grpe_interactors[k],1])
	for k in range(len(dnak_htpg_interactors)):
		dnak_htpg_yvalues.append(bfacs[dnak_htpg_interactors[k], 3])
	ax.plot(dnak_htpg_interactors,dnak_htpg_yvalues, '^c', linestyle='', label='K-HtpG binding site')
	ax.plot(dnak_grpe_interactors, dnak_grpe_yvalues, '^',color='orange', linestyle='', label='K-GrpE binding site')
legend_properties = {'fontsize' : 15,
	'weight' : 'bold'}
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
if len(bfacs[:,0])==(dnak_length+grpe_length) or len(bfacs[:,0])==dnak_length:
	ax.plot([1, 39], [0.019+0.001, 0.019+0.001], color='cyan', lw=10)
	ax.plot([116, 188], [0.019+0.001, 0.019+0.001], color='cyan', lw=10)
	ax.text((1+39)/2, 0.019-0.0025, 'IA', color='cyan', fontsize=12, ha='center')
	ax.text((116+188)/2, 0.019-0.0025, 'IA', color='cyan', fontsize=12, ha='center')
	ax.plot([40, 115], [0.019+0.001, 0.019+0.001], color='magenta', lw=10)
	ax.text((40+115)/2, 0.019-0.0025, 'IB', color='magenta', fontsize=12, ha='center')
	ax.plot([189, 228], [0.019+0.001, 0.019+0.001], color='green', lw=10)
	ax.plot([307, 378], [0.019+0.001, 0.019+0.001], color='green', lw=10)
	ax.text((189+228)/2, 0.019-0.0025, 'IIA', color='green', fontsize=12, ha='center')
	ax.text((307+378)/2, 0.019-0.0025, 'IIA', color='green', fontsize=12)
	ax.plot([229, 306], [0.019+0.001, 0.019+0.001], color='purple', lw=10)
	ax.text((229+306)/2, 0.019-0.0025, 'IIB', color='purple', fontsize=12, ha='center')
# remove this later when it becomes a hassle
	plt.axis([0,605,0.019,0.15])
plt.savefig(f"testestest{bfac_file[:-4]}-figure.svg")
