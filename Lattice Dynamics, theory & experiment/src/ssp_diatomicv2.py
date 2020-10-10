import numpy as np
from math import *
from pylab import *
from matplotlib import pyplot as plt
from matplotlib import animation

#-- Experimental results --#
mass = 0.203                        #m_u                                                                           # The reciprocal of the weights mass [k]
period10 = [7.159,7.284,7.155,7.280,7.214,7.401,6.906,6.903,7.217,7.280,7.216,7.114,7.340,7.335,7.289,7.289,7.216]  # Average of 10 periods
period = 0.1*mean(period10)
C = 0.04*(2.0*np.pi/period)**2


#-- The systems fundamental parameters --#
mRatio = 0.253/0.203 #1.0                          #Mass ratio M_1/M_2 = M_1 (because M_2 = 1)
L=5.5                                 # Distance between nuclei times number of nuclei (for lattice constant a=1)
n = 6                               # Normal mode number n => (1,..,L-1)
#C = 1.0                               # Spring constant [N/m]

#-- Calculate other constants withe the parmeters given above. --#
redMassRec=(1+mRatio)/mass # Calculate the reciprocal of the reduced mass
k = float(n)*np.pi/float(L)            # Constant k = (n*pi)/(L*a)
omega0 = np.sqrt(C*redMassRec)      # Calculate the natural frequency w0 = sqrt(C/mu)
radSolution = []

for p in [1,-1]:                    #The solutions to the angular velocity. Positive: (radSolution[0]) and negative solution: (radSolution[1])
    radSolution.append(omega0*np.sqrt((1+float(p)*np.sqrt(1.0-(4.0*mRatio*(np.sin(0.5*k))**2)/(mRatio+1.0)**2))))

omega = radSolution[0]
#AmplRatio = 2.0*np.cos(0.5*k)/(2.0-(mass*(omega**2)/C))                             # Calculate the realtive amplitude ratio A_1/A_2 = A_1 (A_2=1)
AmplRatio = ((mass*(omega**2)/C)-2.0)/(2.0*np.cos(0.5*k))                             # Calculate the realtive amplitude ratio A_1/A_2 = A_1 (A_2=1)
xMass = np.arange(0.5,L,0.5)                                        # The x-axis position of the masses (based on the systems length L)

g=0
fjMassa = len(xMass)
Ampl = [0]*fjMassa                                           # Initialize array of amplitudes (one for each mass).
while g < fjMassa:                                                      #Calculate the actual amplitudes of each mass
    Ampl[g] = AmplRatio*np.sin(k*xMass[g])
    if (g+1) < fjMassa:
        Ampl[g+1] = np.sin(k*xMass[g+1])
    g+=2

#-- First set up the figure, the axis, and the plot element we want to animate --#
fig = plt.figure()
if abs(AmplRatio) > 1:
    ylims = AmplRatio
else:
    ylims = 1

#-- Plot parameters --#
ax = plt.axes(xlim=(0, L), ylim=(-ylims-0.1*ylims, ylims+0.1*ylims))    # Axis limits generated
plt.ylabel('Amplitude',fontsize=16)                                     # Axis labels created
plt.xlabel('Equilibrium position',fontsize=16)

plt.draw()
tickInt = arange(1.5,(L+0.5),0.5)                       # Create and set labels for x-axis ticks.
lyst = map(str,tickInt)
x_label = ['$0$','$0.5a$','$a$']+['$'+lyst[x-2]+'a$' for x in range(0,len(tickInt))]
ax.set_xticklabels(x_label, fontsize=10)
line1, = ax.plot([], [], lw=2, color='red')                             # Initialize a line
line2, = ax.plot([], [], lw=2, color='blue')                            # - || -
scat, = ax.plot([],[], linestyle='', marker='o', color='black')         # Initialize scatter plot

#-- Print out details of the systems parameters. --#
details = "%d mass diatomic linear chain system, with; \n \
            \t Angular velocity: Omega = %.2f [rad/s]\n \
            \tNatural frequency: Omega0 = %.2f [rad/s]\n \
            \t       Mass ratio: M_1/M_2 = %.2f\n \
            \t  Amplitude ratio: A_1/A_2 = %.2f\n \
            \t      Normal mode: n = %d (where n: 1,...,%d)\n " % (fjMassa,omega, omega0, mRatio, AmplRatio, n, fjMassa)
print details 
#--------------------------------------------------
ttl = ax.text(.5, 1.005, '', transform = ax.transAxes)
#ax.annotate('t='+str(5)+'s', xy=(L-0.05*L, ylims), xycoords="data",bbox=dict(boxstyle="round", fc="w"))
time_text = ax.text(1,0,"",transform = ax.transAxes, ha="right")
#-- Initialization function: plot the background of each frame --#
def init():
    time_text.set_text("")
    line1.set_data([], [])
    line2.set_data([], [])
    scat.set_data([], [])
    return [scat,line1,line2,time_text,]

#-- Animation function.  This is called sequentially --#
def animate(t):
    time_text.set_text('t = %.2f s' % t)
    xinterval = np.arange(0,L,0.05)
    wave1 = AmplRatio*np.cos(omega*t)*np.sin(k*xinterval)
    wave2 = np.cos(omega*t)*np.sin(k*xinterval)
    line1.set_data(xinterval, wave1)
    line2.set_data(xinterval,wave2)
    dots = Ampl*real(np.exp(0+(omega*t)*1j))

    scat.set_data(xMass, dots)
    return [scat,line1,line2,time_text,]

drawLimm = np.arange(0,(2.0*np.pi/omega),0.01)
#-- Call the animator --#
#init()
#animate(0.1*100)
anim = animation.FuncAnimation(fig, animate,init_func=init,frames=drawLimm,interval=10,blit=True, repeat=True)
#anim.save('movie.mp4', fps=100)
#-- Draws a beautiful frequency spectrum for the system, given a big enough L --#
freqSpectrum = [[],[],[]]
for ntmp in range(1,fjMassa+1):
    ktmp = float(ntmp)*np.pi/float(L)
    freqSpectrum[1].append(ntmp)
    for p in [1,-1]:
        freqSpectrum[p+1].append(omega0*np.sqrt((1+float(p)*np.sqrt(1.0-(4.0*mRatio*(np.sin(0.5*ktmp))**2)/(mRatio+1.0)**2))))
plt.grid(True)
plt.show()
