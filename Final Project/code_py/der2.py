import numpy as np
from numpy import loadtxt
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math as mat

#parameters
m = 1
M = 1
L = 1
g = 1
k = 2

def diffeqs(w, t, p):
    [x, phi, xd, phid] = w # d matrix
    [m, M, L, g, k] = p # parameters
    der =   [xd, 
            phid, 
            (M*L*phid*mat.sin(phi) - k*x + M*g*mat.sin(phi)*mat.cos(phi))/((m+M) - M*(mat.cos(phi)*mat.cos(phi))),
            (M*M*mat.cos(phi)*mat.sin(phi)*L*phid*phid - M*mat.cos(phi)*k*x + (M+m)*M*g*mat.sin(phi))/((M*M*L*mat.cos(phi)*mat.cos(phi)) - ((M+m)*M*L))]
    return der

# initial conditions
#x = 0
#phi = 0
#xd = 0 
#phid = 0

# time scale
t = np.linspace(0, 30, 10000)

# containing parameters and initial conditions
p = [m, M, L, g, k]
w0 = [0.1, -mat.sqrt(2)*0.1, 0, 0]


wsol = odeint(diffeqs, w0, t, args = (p, ))

plt.plot(t, wsol[:, 0], 'k-', label = 'x(t)')
#plt.plot(t, wsol[:, 1], 'g-', label = 'ϕ(t)')
#plt.xlabel('t')
#plt.ylabel('f(t)')
#plt.legend(loc = 'best')
plt.show()