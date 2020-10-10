import numpy as np
from math import *
from pylab import *
from matplotlib import pyplot as plt
mass = 0.203
dm = 0.01
dT = 0.05

springK = mass*(2.0*np.pi/0.72116470588235293)**2

#theory = [[1.7211877671537488, 3.3560679926081987, 4.8226609551937614, 4.8226609551937614, 3.3560679926081991, 1.7211877671537501], [1, 2, 3, 4, 5, 6], [7.5410163280796452, 6.9689469950024945, 6.0474255598075057, 6.0474255598075057, 6.9689469950024945, 7.5410163280796452]]
theory =[[1.7610211878247046, 3.4328042468729776, 4.925195204974063, 4.925195204974063, 3.4328042468729785, 1.7610211878247055], [1, 2, 3, 4, 5, 6], [7.7249906646330055, 7.1409055024755421, 6.20637805692943, 6.20637805692943, 7.1409055024755421, 7.7249906646330055]]

#periodMeas = [3.7270, 1.9280, 1.3210, 1.0520, 0.9214, 0.8462]
periodMeas = [3.7125, 1.9590, 1.3276, 1.0652, 0.9393, 0.8524]

omegaM,domega = [],[]

#for k in range(0,len(periodMeas)):
for k in range(0,len(periodMeas)):
    omegaM.append(2.0*np.pi/periodMeas[k])
    domega.append(omegaM[k]*(dT/periodMeas[k]+dm/mass))

plt.axes(xlim=(0.9, 6.1))
plot(theory[1],theory[0], color='red')
p1, = plot(theory[1],theory[0], linestyle='', marker='o', color='red')

plot(theory[1],theory[2], color='blue')
p2, = plot(theory[1],theory[2], linestyle='', marker='o', color='blue')

plot(theory[1],omegaM, color='black')
p3, = plot(theory[1],omegaM, linestyle='', marker='o', color='black')
errorbar(theory[1], omegaM, yerr=domega, fmt='o', color='black')

plt.ylabel(r'$\omega$',fontsize=16)                         
plt.xlabel(r'$n$',fontsize=16)
l1 = legend([p1,p2,p3], ["Acoustic","Optical","Measured",], loc=2)
plt.grid(True)
plt.show()
