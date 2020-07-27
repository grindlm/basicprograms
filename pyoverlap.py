#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib
from operator import itemgetter

args=sys.argv[1:]
num_args=len(args)
each_color = ['black','grey','blue','green','red','purple','orange','magenta','cyan','forestgreen']
for i in range(num_args):
	ov=np.genfromtxt(args[i])
	if ov[0][0] == 6:
		ov[:,0] = ov[:,0]+1
	Xdata=ov[:,0]
	Ydata=ov[:,1]
	if len(Ydata)>100 and max(Ydata[100:]) < 0.25:
		plt.plot(Xdata[:100],Ydata[:100],'-o',color=each_color[i])
	else:
		plt.plot(Xdata,Ydata,'-o',color=each_color[i])
	print(args[i], '\n-----------------\nmode\t overlap')
	ovs = sorted(ov,key=itemgetter(1),reverse=True)
	x = 1
	j = 0
	while x > 0.25:
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
		

plt.xlabel('M',fontsize=20)
plt.ylabel('I$_M$',fontsize=20)

plt.show()

