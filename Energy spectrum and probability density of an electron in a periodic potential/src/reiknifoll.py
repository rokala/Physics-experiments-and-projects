def integrFunc(x,k1,k2): # integrFunc evaluates a function that we numerically evaluate.
    return (V0*(np.sin(np.pi*x)**2)*np.exp(complex(0,x*(k1-k2))).real)

def getEkin(k): # Returns expected kinetic energy (for a given value k (N values on a matrix diagonal))
    Ekin=[]
    for k2 in vidd:
        Ekin.append((2.0*np.pi*(k-(k2-N/2.0))**2))
    return np.diag(Ekin)

def getEpot(): # Returns the expected potential energy for a N by N basis
    Epot=[]
    for k2 in vidd:
        EpotCol=[]
        for k1 in vidd:
            EpotCol.append(-1*quad(integrFunc,0,a,args=(k1,k2))[0]) #Calculate the potential Energy 
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
