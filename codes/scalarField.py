from pylab import *
from mpl_toolkits.mplot3d import Axes3D

xvalues, yvalues = meshgrid(arange(-10, 10, 0.05), arange(-10,10, 0.05)) 

zvalues = 3*xvalues**2*yvalues+yvalues**3*xvalues**2 #the scalar field function

ax = gca(projection='3d')
ax.plot_surface(xvalues, yvalues, zvalues)

show()
