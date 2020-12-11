#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib
from operator import itemgetter
import math

args=sys.argv[1:]
font = {'weight' : 'bold',
	'size' : 25}
matplotlib.rc('font', **font)

num_args=len(args)
each_color = ['black','blue','red','green','purple','orange','magenta','cyan','forestgreen']
ymax = 0
fig, ax = plt.subplots(figsize=(2,2), dpi=300)
for i in range(num_args):
	ov=np.genfromtxt(args[i])
	if ov[0][0] == 6:
		ov[:,0] = ov[:,0]+1
	Xdata=ov[:,0]
	Ydata=ov[:,1]
	if len(Ydata)>100 and max(Ydata[100:]) < 0.25:
		ax.plot(Xdata[:100],Ydata[:100],'-o',color=each_color[i])
	else:
		ax.plot(Xdata,Ydata,'-o',color=each_color[i])
	print(args[i], '\n-----------------\nmode\t overlap')
	ovs = sorted(ov,key=itemgetter(1),reverse=True)
	x = 1
	j = 0
	x1, x2, x3, x4 = ovs[0][0], ovs[1][0], ovs[2][0], ovs[3][0]
	y1, y2, y3, y4 = ovs[0][1], ovs[1][1], ovs[2][1], ovs[3][1]
	if y1>ymax: ymax=y1
	if y1>0.3: ax.text(65,(ymax-0.18*i*ymax),r"Mode={}, I$_M$={}".format(int(x1),math.trunc(y1*100)/100.0), color=each_color[i])
	if y2>0.3: ax.text(65,(0.95*ymax)-(0.18*i*ymax),r"Mode={}, I$_M$={}".format(int(x2),math.trunc(y2*100)/100.0), color=each_color[i])
	if y3>0.3: ax.text(65,(0.9*ymax)-(0.18*i*ymax),r"Mode={}, I$_M$={}".format(int(x3),math.trunc(y3*100)/100.0), color=each_color[i])
	if y4>0.4: ax.text(65,(0.85*ymax)-(0.18*i*ymax),r"Mode={}, I$_M$={}".format(int(x4),math.trunc(y4*100)/100.0), color=each_color[i])
	#plt.annotate(f"({int(x1)}, {math.trunc(y1*100.0)/100.0})", xy=(x1,y1), xytext=(x1+8,y1+(0.1*ymax)), arrowprops=dict(color=each_color[i], arrowstyle='wedge'))
	#plt.annotate(f"({int(x2)}, {math.trunc(y2*100.0)/100.0})", xy=(x2,y2), xytext=(x2+8,y2+(0.1*ymax)), arrowprops=dict(color=each_color[i], arrowstyle='wedge'))
	#plt.annotate(f"({int(x3)}, {math.trunc(y3*100.0)/100.0})", xy=(x3,y3), xytext=(x3+8,y3+(0.1*ymax)), arrowprops=dict(color=each_color[i], arrowstyle='wedge'))
	while x > 0.3:
		print(int(ovs[j][0]),'\t',ovs[j][1])
		j = j+1
		x = ovs[j][1]
		#newsort = sorted(ov, key=lambda ydata: ydata[1])
		#newsort = np.array(newsort)
		#yd = newsort[(len(newsort)-1-j), 1]
		#xd = newsort[(len(newsort)-1-j), 0]
		#print(xd,"\t",yd)
		#plt.text(xd+1.5,yd,'Mode %s, %s' %(xd,yd), color='magenta')
	print(' ')
plt.xlabel('M')
plt.ylabel('I$_M$')

plt.show()
