R      	= 8.3145    			# J K^(-1) mol^(-1)
d      	= 0.01      			# m
planck 	= 6.62607*10**(-34) 	# J s
vLight	= 2.998*10**(8)			# m s^(-1)
kB		= 1.3806488*10**(-23)	# m^2 kg s^(-2) K^(-1)
hc_k   	= (planck*vLight)/kB	# m K 
B0	 	= 3.7315				# m^(-1)
nu0		= 21330.0				# m^(-1)
Phi_rot = hc_k*B0				# K
Phi_vib	= hc_k*nu0				# K
sigma 	= 2.0					# No unit
mmass	= 0.25380894 			# kg mol^(-1)
pie		= 3.141592653589793
cFactor = kB*(2*pie*mmass*kB/planck**2)**(1.5)/(sigma*Phi_rot)
# Data given from Table. 1 for representative phonon frequencies in a I_2 crystal
nuj = [2100.0, 2650.0, 3300.0, 4100.0, 4900.0, 5150.0, 5800.0, 5900.0, 7540.0, 8740.0, 18070.0, 18950.0]	# m^(-1)
Phi_j = [ hc_k*j for j in nuj ]

# Data given from Table. 2 in 'Experiments in physical chemistry' for the Molar Absorption coefficient
givenTemp = [20.0, 30.0, 40.0, 50.0, 60.0,70.0] # °C
givenMAC = [69.1,68.2,67.2,66.3,65.4,64.6]		# m^2 mol^(-1)
