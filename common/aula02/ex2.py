import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

x1 = [2, 1, 3]
x2 = [3, 1, 4]
x3 = [5, 7, 12]

ax = plt.axes(projection='3d')
ax.set_xlim([0, 6])
ax.set_ylim([7, 0])
ax.set_zlim([0, 14])
start = [0,0,0]
ax.quiver(start[0], start[1], start[2], x1[0], x1[1], x1[2], color='r')
ax.quiver(start[0], start[1], start[2], x2[0], x2[1], x2[2],color='b')
ax.quiver(start[0], start[1], start[2], x3[0], x3[1], x3[2], color='g')
ax.view_init(15, 180)
plt.show()
