import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as Fa

## Gravitational const
G = 100

#Time period delta time
dt = 0.01

##Masses
m = [10, 2]

# pos of objects init x,y
pos0 = [0, 0]
pos1 = [0, 30]

#velocities of objects init x,y
v0 = [0, 0]
v1 = [-3,0]

#sets up window
fig, ax = plt.subplots()
ax.grid(True)
ax.set_aspect("equal")
ax.set_ylim(-100,100)
ax.set_xlim(-100,100)
obj0, = ax.plot(pos0[0], pos0[1], "go")
obj1, = ax.plot(pos1[0], pos1[1], "ro")

def update(frame):
    global G, pos0, pos1, v0, v1, m

    #Finds Dist
    rx = pos1[0]-pos0[0] 
    ry = pos1[1]-pos0[1]
    r = np.sqrt(rx**2+ry**2)
    if rx == 0:
        theta = np.pi/2 # avoids /0 error
    else:
        theta = np.arctan(ry/rx)

    #Finds forces 
    F = G*m[0]*m[1]/r**2

    #decides direction of forces and magnitude of them in x and y
    if rx < 0:
        F0 = [-1*F*np.cos(theta), -1*F*np.sin(theta)]        
        F1 = [F*np.cos(theta), F*np.sin(theta)]  
    else:
        F0 = [F*np.cos(theta), F*np.sin(theta)]         
        F1 = [-1*F*np.cos(theta), -1*F*np.sin(theta)]

    #finds velocities in x and y
    v0 = [F0[0]*dt/m[0]+v0[0], F0[1]*dt/m[0]+v0[1]] 
    v1 = [F1[0]*dt/m[1]+v1[0], F1[1]*dt/m[1]+v1[1]]

    #updates coords x,y
    pos0 = [pos0[0]+v0[0]*dt, pos0[1]+v0[1]*dt]
    pos1 = [pos1[0]+v1[0]*dt, pos1[1]+v1[1]*dt]

    #updates pos
    obj0.set_data([pos0[0]], [pos0[1]])
    obj1.set_data([pos1[0]], [pos1[1]])

ani = Fa(fig, update,frames=10000, interval=10)

plt.show()




    









        












