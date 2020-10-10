import numpy as np
import functools as fu
import operator as op
from fastar import *
import matplotlib.pyplot as plt

def lineRegression(x,y,degree):
	coeff = np.polyfit(x, y, degree)
	yFit = np.polyval(coeff,x)
	return yFit,coeff
	
def PhiProduct(temperatureList):
	prods=[]
	for currT in temperatureList:
		listi = np.sqrt(1.0-np.exp(-np.array(Phi_j)/currT))
		prods.append(fu.reduce(op.mul, listi ,1))
	return prods
	
def lnPminuStuff(lnP,T):
	return (lnP - np.log(T**(3.5)*PhiProduct(T)/(1.0-np.exp(-Phi_vib/T))))
	
def crystalEntropy(T):
	Ss = []
	for Te in T:
		jPhi_T = np.array(Phi_j)/Te
		Ss.append(0.5*sum((jPhi_T/(np.exp(jPhi_T)-1.0))-np.log(1.0-np.exp(-jPhi_T))))
	return Ss

def getDeltaE0(lnP,T):
	return T*R*(np.log(cFactor)-lnPminuStuff(lnP,T))

def gasEntropy(T,p):
	vibPhi_T = Phi_vib/T
	DeltaE0minusMuGas_T = np.log((cFactor*T**3.5)/(p*(1.0-np.exp(-vibPhi_T))))
	return (DeltaE0minusMuGas_T + 3.5 + vibPhi_T/(np.exp(vibPhi_T)-1.0))
	
def statisticsDeltaHsub(p,T): 
	return T*R*(gasEntropy(T,p)-crystalEntropy(T))
	
def plotEnthalpy(iT,lnP):
	#----- Plot & obtain information about the results -----#
	plt.grid(True)
	bestMACfit, studlar = lineRegression(iT,lnP,1) # 1 is the polynomial degree
	print("Hallatala (Enthalpy of sublimation): %.1f [J/kg K]\n" % (-R*studlar[0]))
	plt.plot(iT,bestMACfit,'b-')
	plt.errorbar(iT,lnP,xerr=2.5*iT**2,fmt='ko')
	plt.xlabel(r'$1/T$ [K$^{-1}$]', fontsize=16)
	plt.ylabel(r'$\ln(P)$ [$\ln$ Pa]', fontsize=16)
	plt.show()
	
def plotDeltaEequil(lnP,T):
	#----- Crystal/Gas equilibrium -----#
	mumu = lnPminuStuff(lnP,T)
	bestDeltaE0fit, derp = lineRegression((1.0/T),mumu,1)
	print(-R*derp[0])
	print(derp[1])
	plt.grid(True)
	plt.plot((1.0/T),bestDeltaE0fit,'b-')
	plt.errorbar((1.0/T), mumu,xerr=2.5/T**2,fmt='ko')
	plt.xlabel(r'$1/T$ [K$^{-1}$]', fontsize=16)
	plt.ylabel(r'Dimensionless', fontsize=16)
	plt.show()

def plotStatisticsDeltaHsub(p,T): #Not working...
	E0 = (2.0/(R*1000.0))*statisticsDeltaHsub(p,T)
	plt.grid(True)
	plt.plot((1.0/T),E0)
	plt.show()