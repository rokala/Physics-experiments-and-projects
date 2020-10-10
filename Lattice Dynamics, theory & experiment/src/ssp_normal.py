import numpy as np
from math import *
from pylab import *
from matplotlib import pyplot as plt
from matplotlib import animation

# Constants
isqrt = 2**(-0.5)
L=9                             # Length of the system
n = 4                           # Normal mode number n => (1,..,L-1)
omega = np.sqrt(2-2*np.cos(n*np.pi/L))   # Angular velocity
fjMassa = arange(1,L)
Ampl = [0]*(L-1)                # Initialize array of amplitudes.
A_max = 1                       # Maximum relative amplitude
for j in fjMassa:
    Ampl[j-1] = A_max*np.sin(j*n*np.pi/L)

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, L), ylim=(-1.1, 1.1))

line, = ax.plot([], [], lw=2, color='b')
scat, = ax.plot([],[], linestyle='', marker='o', color='r')
# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    scat.set_data([], [])
    return [scat,line,]

# animation function.  This is called sequentially
def animate(t):
    xinterval = np.arange(0,L,0.05)
    wave = A_max*np.cos(0.1*omega*t)*np.sin(n*xinterval*np.pi/float(L))
    line.set_data(xinterval, wave)
    dots = Ampl*real(np.exp(0+(omega*0.1*t)*1j))

    scat.set_data(fjMassa, dots)
    return [scat,line,]

# call the animator.
init()
animate(0)
animate(15)
#anim = animation.FuncAnimation(fig, animate,init_func=init,frames=range(int(ceil(2*np.pi/(0.1*omega)))),interval=20,blit=True)
plt.grid(True)
plt.show()
