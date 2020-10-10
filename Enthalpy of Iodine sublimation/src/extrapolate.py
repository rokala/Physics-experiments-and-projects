import numpy as np
from scipy import polyval, polyfit
from matplotlib import pyplot as plt
#from operator import mul
from fastar import *

# Assume a 2nd degree polynomial with coefficients a, b, c: y(x) = ax^2 + bx + c
a, b, c = polyfit(givenTemp, givenMAC, 2)
y_val_lineMAC = polyval([a, b, c], givenTemp)    # predicted values of y
x_val_lineTemp = np.linspace(20.0, 80.0, 20)
y_val_lineMAC = polyval([a, b, c], x_val_lineTemp)

# Here we add the temperature values we want to find MAC for 
newTemp = [25.0,35.0,45.0,55.0,65.0,75.0,80.0]
newMAC = polyval([a, b, c], newTemp)
allTemps = sorted(givenTemp+newTemp)
allMACS= sorted((givenMAC+newMAC.tolist()),reverse=True) 

writeFile = open('TempvsMAC.txt','w')
aRow = "T [°C]\tMAC [m^2/mol]\n"
for k in range(len(allTemps)):
	writeFile.write(aRow)
	aRow = "%.1f\t%.1f\n" % (allTemps[k], allMACS[k])

writeFile.write(aRow)	
writeFile.close()

# Create plots
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(x_val_lineTemp, y_val_lineMAC, 'b-',givenTemp,givenMAC,'ro',newTemp,newMAC,'ko')
plt.xlabel(r'$T$ [K]', fontsize=18)
plt.ylabel(r'$\varepsilon$ [m$^2/$mol] ', fontsize=16)
plt.legend(["Best fit line","Referenced values","Extrapolated values"])
plt.grid(True)
plt.show()
