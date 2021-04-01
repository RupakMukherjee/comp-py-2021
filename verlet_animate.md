```python
#!/usr/bin/ python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits import mplot3d

Lx      = 10.0   # System length in X
Ly      = 10.0   # System length in Y
Lz      = 10.0   # System length in Z

N       = 100    # Number of particles

tmax    = 1.0   # Final time
dt      = 0.01   # time step size
Nt      = round(tmax/dt)  #number of time steps


datadt = 10
file_num = np.arange(start=0, stop=Nt, step=datadt, dtype=int)


def animate(i):
    file='data/time%04d'%file_num[i]+'.txt'
    x,y,z = np.loadtxt(file, unpack=True)
    id = i*datadt
    ax.cla()
    ax.scatter(x,y,z,marker='o',color='b',alpha=1.0,s=10)
    ax.set_title('TimeSteps = %d'%id)
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.set_zlabel("$z$")
    ax.set_xlim([-Lx, Lx])
    ax.set_ylim([-Ly, Ly])
    ax.set_zlim([-Lz, Lz])

fig = plt.figure(figsize=(6, 6))
ax = plt.axes(projection ="3d")
ani = animation.FuncAnimation(fig,animate,frames=len(file_num),interval=10,blit=False)
plt.show()

```
