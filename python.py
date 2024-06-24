"""
 VPythonMath: none
 Ver. 1: 2018/2/18
 Ver. 2: 2019/9/5

"""
from vpython import *

"""
 1. , setting variables + values
"""
size = 0.1   # size of the box
L = 1        # length of the floor
v = 0.03     # velocity or speed
t = 0        # time
dt = 0.01    # time interval Graph

"""
 2. settings
"""
scene = canvas(title="1D Motion", width=800, height=600, x=0, y=0, center=vec(0, 0.1, 0), background=vec(0, 0.6, 0.6))
floor = box(pos=vec(0, 0, 0), size=vec(L, 0.1*size, 0.5*L), color=color.blue)
cube = box(pos=vec(-0.5*L + 0.5*size, 0.55*size, 0), size=vec(size, size, size), color=color.red, v=vec(v, 0, 0))


#"""
# 3.The moving object

#"""
#while(cube.pos.x <= 0.5*L- 0.5*size)#????:
    #rate(1001) #????
    #cube.pos.x += v*dt
   # xt.plot(pos = (t, cube.pos.x))#????
    #vt.plot(pos = (t, cube.v.x))
    #t += dt

print("t = ", t)
