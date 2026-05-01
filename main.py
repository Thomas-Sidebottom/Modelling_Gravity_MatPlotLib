import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as Fa

## Gravitational const
G = 100

#Time period delta time
dt = 0.01

##Masses
m = [10, 10]

# pos of objects init x,y
pos0 = [0, 0]
pos1 = [0, 1]

#velocities of objects init x,y
v0 = [0, 0]
v1 = [0,-2]

#sets up window
fig, ax = plt.subplots()
ax.grid(True)
ax.set_aspect("equal")
ax.set_ylim(-200,200)
ax.set_xlim(-200,200)
obj0, = ax.plot(pos0[0], pos0[1], "go")
obj1, = ax.plot(pos1[0], pos1[1], "ro")


def update(frame):
    global G, pos0, pos1, v0, v1, m

    #Finds Dist
    rx = pos1[0]-pos0[0] 
    ry = pos1[1]-pos0[1]
    r = np.sqrt(rx**2+ry**2)
    if rx == 0:
        theta = np.pi/2
    else:
        theta = np.arctan(ry/rx)

    #Finds forces 
    F = G*m[0]*m[1]/r**2

    Fx0 = -F*np.cos(theta) 
    Fy0 = -F*np.sin(theta)
    Fx1 = F*np.cos(theta) 
    Fy1 = F*np.sin(theta)


    #finds velocities 
    v0 = [Fx0*dt/m[0]+v0[0], Fy0*dt/m[0]+v0[1]] 
    v1 = [Fx1*dt/m[1]+v1[0], Fy1*dt/m[1]+v1[1]]

    #updates coords x,y
    pos0 = [pos0[0]+v0[0]*dt, pos0[1]+v0[1]*dt]
    pos1 = [pos1[0]+v1[0]*dt, pos1[1]+v1[1]*dt]

    obj0.set_data([pos0[0]], [pos0[1]])
    obj1.set_data([pos1[0]], [pos1[1]])
    

ani = Fa(fig, update,frames=100, interval=10)

plt.show()




    









        












