import math

from matplotlib import pyplot as plt, patches
import numpy as np
from fractions import Fraction as fr

import matplotlib as mpl

fig = plt.figure(figsize=(3*6.4,3*4.8))
ax = fig.subplots()

ymp = patches.Circle((0, 0), radius=3, fill=0, color="red",  linewidth=2.5, linestyle="--")
ax.add_patch(ymp)
plt.annotate(f"ympyrä",xy=(-math.pi,math.pi),fontsize=40)
#xy=(3*np.cos(radianpist[i]), 3*np.sin(radianpist[i]))



# Move left y-axis and bottom x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.axis('equal')

plt.xticks([-3, 0, 3], minor=True)
plt.yticks([-3, 0, 3])

pii=np.pi
pist_xy=np.array([pii, pii, 3*pii, pii])
nim=np.array([1, 2, 4, 6])
varit=np.array(['red', 'green', 'blue', 'orange','red', 'green', 'blue', 'orange','red', 'green'])

uudet=np.array([30,45,60,90,120,135,150,180,270,360])
radianpist=[]
for i in uudet:
    rad=np.radians(i)
    radianpist.append(rad)
radianpist=np.array(radianpist)

text=[r'$\pi$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\frac{\pi}{6}$']

#x = np.cos(pist_xy/nim)
#y = np.sin(pist_xy/nim)

x = 3*np.cos(radianpist)
y = 3*np.sin(radianpist)

plt.scatter(x, y, color=varit, marker='X')

for i in range(len(radianpist)):
    plt.annotate(f"{uudet[i]}",
             xy=(3*np.cos(radianpist[i]), 3*np.sin(radianpist[i])), xycoords='data',
             xytext=(+30, +5), textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))


plt.show()