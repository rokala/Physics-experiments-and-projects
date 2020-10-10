import numpy as np
from math import *
from pylab import *
from matplotlib import pyplot as plt

mRatio = 1.0 #0.223/0.203            #Mass ratio M_1/M_2 = M_1 (because M_2 = 1)
L=9.0                                # Distance between nuclei times number of nuclei (for lattice constant a=1)
xMass = range(1,int(L))
n = 1                                # Normal mode number n => (1,..,L-1)
C=1
def getK(n):
    return float(n)*np.pi/float(L)            # Constant k = (n*pi)/(L*a)

def getAmplitudes(n,xMass):
    k = getK(n)
    fjMassa = len(xMass)
    Ampl = [0]*fjMassa                                           # Initialize array of amplitudes (one for each mass).
    g=0
    while g < fjMassa:                                                      #Calculate the actual amplitudes of each mass
        Ampl[g] = np.sin(k*xMass[g])
        if (g+1) < fjMassa:
            Ampl[g+1] = np.sin(k*xMass[g+1])
        g+=2
    return Ampl

def getAngularFrequency(n):
    radSolution = []
    k = getK(n)
    for p in [1,-1]:                    #The solutions to the angular velocity. Positive: (radSolution[0]) and negative solution: (radSolution[1])
        radSolution.append(np.sqrt((1+float(p)*np.sqrt(1.0-(4.0*mRatio*(np.sin(0.5*k))**2)/(mRatio+1.0)**2))))
    return radSolution

f, ax = plt.subplots(int(L)-1,sharex=True)



omegas = getAngularFrequency(n)
omega = omegas[1]
xinterval = np.arange(0,L,0.05)
litir = ['black','red']
for n in range(1,int(L)):
    Ampl = getAmplitudes(n,xMass)
    wave = np.sin(getK(n)*xinterval)
    #dots = Ampl*real(np.exp(0+(omega*0)*1j))
    ax[n-1].plot(xinterval,wave,linestyle='--',color='black')
    ax[n-1].plot(xMass,Ampl, linestyle='', marker='o', color='black')
    ax[n-1].set_ylim([-1.2,1.2])

plt.xlabel('x')
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
plt.setp([a.get_yticklabels() for a in f.axes[:-1]], visible=False)

plt.show()
