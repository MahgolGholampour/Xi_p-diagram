import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import measurements
import random


Li = 50
Lf = 201
StepL = 50
Pi_axis = []



N = 2
parts = 50
P = np.linspace(0.45, 0.72, parts)
Xi = np.zeros_like(P)
Xis = []
P_axis = []
for m, p in enumerate(P):
	P_axis.append(p)



for l in range(Li, Lf, StepL):
   for  n in range(N):
    randomLattice = np.random.random(size=(l,l))
    for m, p in enumerate(P):
      num_list = []
      lattice = randomLattice < p
      labels , num = measurements.label(lattice)

      for k in range(1 , num):
        s = 0


        for i in range(l):

          for j in range(l):

            if labels[i,j] == k:
              s += 1
          num_list.append(s)

        S = []
        S2 = []

        for q in num_list:

          S.append(q)
          S2.append(q**2)

        sumS = sum(S)

        sumS2 = sum(S2)

        sumS -= max(S)

        sumS2 -= max(S2)

        xi_p = sumS2/ sumS

        Xi[m] += xi_p

	z = Xi/N
	Xis.append(z)

for Xi in Xis:

   plt.plot(P, Xi)

plt.savefig('chi_nd.png')
plt.show()
