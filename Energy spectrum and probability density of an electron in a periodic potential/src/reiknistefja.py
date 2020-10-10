import numpy as np
from scipy.integrate import quad
from matplotlib import pyplot as plt

#DEFINE PARAMETERS
N = input('Pick the dimension of your basis, N = ')
V0 = input('Pick the amplitude of the periodic potential, V_0 = ') 
a = 1.0
kmaxDa=1.0
vidd = range(1,int(N+1)) #To map elements to array/matrix
stepsize=100

#FUNCTIONS THAT CALCULATES AN INTEGRAL AND STUFF
def integrFunc(x,k1,k2): # integrFunc evaluates a function that we numerically evaluate.
    return (V0*(np.sin(np.pi*x)**2)*np.exp(complex(0,2.0*np.pi*x*(k1-k2))).real)

def getEkin(k): # Returns expected kinetic energy (for a given value k (N values on a matrix diagonal))
    Ekin=[]
    for k2 in vidd:
        Ekin.append(((k-(k2-N/2.0))**2))
    return np.diag(Ekin)

def getEpot(): # Returns the expected potential energy for a N by N basis
    Epot=[]
    for k2 in vidd:
        EpotCol=[]
        for k1 in vidd:
            EpotCol.append(quad(integrFunc,0,a,args=(k1,k2))[0]) #Calculate the potential Energy 
        Epot.append(EpotCol)
    return Epot

def getHmat(k): # Returns a matrix representing the Hamiltonian (= getEkin + getEpot)
    Hmat=[]
    Kinetic = getEkin(k)
    for v in vidd:
        Hmat.append(map(sum, zip(Potential[v-1],Kinetic[v-1])))
    return Hmat

def getEigs(matrix): # Takes in a square matrix and returns its eigenvalues & eigenvectors.
    return np.linalg.eigh(matrix)

def getWavefunction(x,k,state): # Returns absolut value of the probabilty density squared for a given energystate, position x and wave vector k.
    probDens = 0.0
    for n in vidd:
        probDens = probDens + EigVec[n-1,state]*np.exp(complex(0,2.0*np.pi*(k-N/2.0-float(n))*x))
    return abs(probDens)**2

def makeMatrix(N): #Defines an array that contains N empty arrays.
    Fylki = []
    for incr in range(0,int(N)):
        Fylki.append([])
    return Fylki

#ax = plt.axes( ylim=(0.0,4.0))
#x_label=['$0$','$a/5$','$2a/5$', '$3a/5$','$4a/5$','$a$']
#ax.set_xticklabels(x_label, fontsize=15)

Potential = getEpot()
kHnit = np.linspace(-kmaxDa,kmaxDa,stepsize)
yHnit = makeMatrix(N)
for k in kHnit:
    EigVal,EigVec = getEigs(getHmat(k))
    for g in vidd:
        yHnit[g-1].append(EigVal[g-1])

xHnit = np.linspace(0,1,stepsize)
states=range(0,3)
#for state in states:
#    psi=[]   
#    for b in range(0,len(xHnit)):
#        psi.append(getWavefunction(xHnit[b],0.5,state))
#    plt.plot(xHnit,psi)
  
#CREATE & DEFINE THE PARAMETERS OF THE PLOT
for incr in range(0,10):
    plt.plot(kHnit,yHnit[incr],linestyle='', markersize=2,marker='o',color='black')                            #Create the plot
#plt.legend(['Ground State','1st Excited', '2nd Excited'],loc=1)
plt.ylabel('$H$',fontsize=16)                                     # Axis labels created
plt.xlabel('$k$',fontsize=16)
plt.ylim(0,25.0)
plt.grid(True)
#plt.xlim(-kmaxDa,kmaxDa)
plt.show()
