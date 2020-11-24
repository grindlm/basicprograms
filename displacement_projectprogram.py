#!/usr/bin/env python
import sys
import matplotlib.pyplot as plt
import numpy as np
outliers = []
def detect_outlier(data_1):
	sorted_data = sorted(data_1, key=lambda x:x[1])
	q1, q3 = np.percentile(sorted_data, [25, 75])
	iqr = q3 - q1
	lower_bound = q1 - (1.5 * iqr)
	upper_bound = q3 + (1.5 * iqr)
	for y in range(len(data_1[1])):
		if data_1[y,1] > upper_bound:
			outliers.append([data_1[y,0], data_1[y,1]])
	if len(outliers) > 0:
		return True, max(outliers), min(outliers), upper_bound
	else:
		return False, 0, 0, upper_bound

args = sys.argv[1:]
num_args = len(args)


thesecolors=['black','red','blue','purple','green','orange']
xtickmarks=[]
for i in range(num_args):
	disp=np.genfromtxt(args[i])
	result_of_outliers = detect_outlier(disp)
	thisx=(disp[:,0])
	thisy=(disp[:,1])
	if len(thisy)==1248:
		xposition=[227,489,624,(624+227),(624+489)]
	elif len(thisy)==1853:
		xposition=[227,489,624,(624+227),(624+489),1248,(1248+383),(1248+510)]
	elif len(thisy)==2458:
		xposition=[227,489,624,(624+227),(624+489),1248,(1248+383),(1248+510),1853,(1853+383),(1853+510)]
	elif 603 <= len(thisy) <= 606:
		xposition = [383, 510]
	else:
		xposition=[]
	if result_of_outliers[0]:
		fig, (ax1,ax2) = plt.subplots(2,1, sharex=True, figsize=(8,4))
		ax1.plot(thisx, thisy, color=thesecolors[i])
		ax2.plot(thisx, thisy, color=thesecolors[i])
		ax1.set_ylim(result_of_outliers[2] - 0.05, result_of_outliers[1] + 0.05)
		ax2.set_ylim(0,result_of_outliers[3])
	else:
		fig, ax = plt.subplots(figsize=(8,4))
		ax.plot(thisx,thisy,color=thesecolors[i])
for xc in xposition:
	if xc==624 or xc==1248 or xc==1853:
		plt.axvline(x=xc,color='k',linestyle='-')
	else:
		plt.axvline(x=xc, color='grey',linestyle='--')
xticks_length = len(thisy)//100 + 1
for z in range(xticks_length):
	xtickmarks.append(z*100)

plt.xlabel('Residue Number')
plt.ylabel(r'$\delta$q($\AA$)')
plt.xticks(xtickmarks, rotation=45)

plt.show()
