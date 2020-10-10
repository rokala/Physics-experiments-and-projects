import numpy as np
from math import *
from pylab import *
from matplotlib import pyplot as plt

mRatio = 2.0 #0.223/0.203            #Mass ratio M_1/M_2 = M_1 (because M_2 = 1)
L=4.5                                # Distance between nuclei times number of nuclei (for lattice constant a=1)
#xMass = range(1,int(L))
xMass = np.arange(0.5,L,0.5) 
#n = 2                                # Normal mode number n => (1,..,L-1)
mass=0.203
def getK(n):
    return float(n)*np.pi/float(L)            # Constant k = (n*pi)/(L*a)

period = 0.72116470588235293
C = 0.04*(2.0*np.pi/period)**2
omega0 = np.sqrt(C*(1+mRatio)/mass)
def getAmplitudes(n,xMass):
    k = getK(n)
    AmplRatio = getAmplRatio(n)
    fjMassa = len(xMass)
    Ampl = [0]*fjMassa                                           # Initialize array of amplitudes (one for each mass).
    g=0
    while g < fjMassa:                                                      #Calculate the actual amplitudes of each mass
        Ampl[g] = AmplRatio*np.sin(k*xMass[g])
        if (g+1) < fjMassa:
            Ampl[g+1] = np.sin(k*xMass[g+1])
        g+=2
    return Ampl

def getAngularFrequency(n):
    radSolution = []
    k = getK(n)
    for p in [1,-1]:                    #The solutions to the angular velocity. Positive: (radSolution[0]) and negative solution: (radSolution[1])
        radSolution.append(omega0*np.sqrt((1+float(p)*np.sqrt(1.0-(4.0*mRatio*(np.sin(0.5*k))**2)/(mRatio+1.0)**2))))
    return radSolution

def getAmplRatio(n):
    return ((mass*omega**2/C)-2.0)/(2.0*np.cos(0.5*getK(n)))

f, ax = plt.subplots(4,2,sharex=True)

xinterval = np.arange(0,L,0.05)
litir = ['black','red']
for switch in [0,1]:
    for n in range(1,5):
        omegas = getAngularFrequency(n)
        omega = omegas[switch]
        Ampl = getAmplitudes(n,xMass)
        AmplRatio = getAmplRatio(n)
        wave = AmplRatio*np.sin(getK(n)*xinterval)
        wave2 = np.sin(getK(n)*xinterval)
        #ax[n-1,switch].set_ylim([-1.2,1.2])
        ax[n-1,switch].plot(xinterval,wave,linestyle='--',color='black')
        ax[n-1,switch].plot(xinterval,wave2,linestyle='--',color='black')
        ax[n-1,switch].plot(xMass,Ampl, linestyle='', marker='o', color='black')


plt.xlabel('x')
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
plt.setp([a.get_yticklabels() for a in f.axes[:-1]], visible=False)
plt.show()
