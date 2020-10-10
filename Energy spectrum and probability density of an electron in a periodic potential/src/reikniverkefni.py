import numpy as np
from scipy.integrate import quad
from matplotlib import pyplot as plt

#DEFINE CONSTANTS
a0a,alpha,N=0.1,1.0,5.0
Eryd=5.92
a = 1.0/a0a
b=0.2*a
vidd = range(1,int(N+1))                                  #To map elements to array/matrix
Epot,Hmat,Ekin=[[]]*int(N),[[]]*int(N),[]

#FUNCTIONS THAT CALCULATES AN INTEGRAL AND STUFF
phi=[]
def getPhi(x):
    return np.sqrt(2*a0a)*np.sin(k*np.pi*a0a*x)
def integrFunc(x,n,m):                              #A function that we integrate numerically over an interval
    fast = np.pi*a0a
    return 2.0*a0a*np.sin(fast*n*x)*np.sin(fast*m*x)

def getEkin(k):                                     #Returns expected kinetic energy for a given value k
    return (k*np.pi*a0a)**2*Eryd

def getEpot(m):
    EpotCol=[0]*int(N)
    for n in vidd:
        EpotCol[n-1] = -alpha*Eryd*quad(integrFunc,b,(a-b),args=(n,m))[0]   #Calculate the potential Energy
    return EpotCol

def getHmat():                                          #Create the E_potential_energy matrix
    for m in vidd:
        Ekin.append(getEkin(m)) 
        mtmp = m-1
        Hmat[mtmp]= getEpot(m)
        Hmat[mtmp][mtmp] = getEpot(m)[mtmp]+getEkin(m) #Summing the diagonal matrix Ekin with Epot's diagonal 
    return Hmat

def getEigvals(matrix):
    return np.linalg.eigvals(matrix)                    #Find and return the matrices eigenvalues

#HERE WE CALL THE FUNCTIONS ABOVE
eig=getEigvals(getHmat())

#CREATE & DEFINE THE PARAMETERS OF THE PLOT
for incr in range(0,len(eig)):
    plt.plot([0,10],[eig[incr]]*2,linewidth=2.0)                            #Create the plot

plt.ylabel('Energy [meV]',fontsize=16)                                     # Axis labels created
plt.xlabel('Position $x$ [nm]',fontsize=16)
plt.show()
