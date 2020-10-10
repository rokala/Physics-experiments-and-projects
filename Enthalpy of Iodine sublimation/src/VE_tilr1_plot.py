import numpy as np
from fastar import *
from fallabanki import *
#from extrapolate import *
# Load data
T,A1,A2,lam = np.transpose(np.loadtxt('VE_tilr1_data.dat',skiprows=1))  	# Raw data
refT, refMAC = np.transpose(np.loadtxt('TempvsMAC.txt',skiprows=1))        # If this doesn't load/exist, then run extrapolate.py to create it

# Temperature   : T, refT
# A1,A2         : Absorption Coefficients
# lam           : Wavelength
# MAC           : Molar Absorption Coefficients


#----- Compute observables -----#
A_Igas = A1-A2 # Correction to obtain only the absorption due to I_2(g)
MAC,indicesT = [],[]

for uniqueT in list(sorted(set(T))): # This loop makes an array of arrays, where each array contains indices for some specific temperature.
	indicesT.append([indexT for indexT, Tval in enumerate(T) if Tval == uniqueT])
A_new = np.zeros(len(T))
for indexT in indicesT:
	if len(indexT) > 1:
		A_new[indexT] = A_Igas[indexT[0]]-A_Igas[indexT[1]]
		if sum(A_new[indexT]) < 0:
			A_new[indexT]=-A_new[indexT]
	else:
		A_new[indexT] = A_Igas[indexT]

for Tval in T:
    MAC.append(refMAC[refT.tolist().index(Tval)])
	
#----- Split table by lam -----#
lamIndices = [i for a in set(lam) for i, x in enumerate(lam) if x == a] # Set() finds unique elements
epsIndices = [lamIndices[0:12],lamIndices[12:]]
print(A_new)
print(T)
T = T+273.15                            # Convert T from °C to Kelvin
MAC = np.array(MAC)
invT = T**(-1) 						# Reciprocal of the temperature
MAC = MAC[epsIndices[0]]
T=T[epsIndices[0]]
invT=invT[epsIndices[0]]
A_new=A_new[epsIndices[0]]
print(A_new)
print(T)
vaPr = np.log(A_new*R*T/(d*MAC)) 	# Calculate the natural logarithm of the vapor pressure



#----- Create a new table with all computed data ------#
writeFile = open('tilraun_1_observables.txt','w')
aRow = "T [°C]\tA_Igas\tA_diff\tP_vap [Pa]\tMAC [m^2/mol]\tlam [1E-09]\n"
for k in range(len(T)):
    writeFile.write(aRow)
    aRow = "%.1f\t%.2E\t%.2E\t%.4f\t%.1f\t%.1f\n" % (T[k]-273.15, A_Igas[k],A_new[k], np.exp(vaPr[k]), MAC[k], lam[k])

writeFile.write(aRow)
writeFile.close()

#plotEnthalpy(invT,vaPr)
plotDeltaEequil(vaPr,T)