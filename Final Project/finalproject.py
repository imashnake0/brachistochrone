import numpy as np
from numpy import loadtxt
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math as mat

#parameters
a = 6

# initial conditions (here, and final)
x1 = 0
y1 = 0
#x2 = 
#y2 = 

def brachistochrone(a, x1, y1):
    def diffeqs(w, t, p):
        [x, y, yd] = w # d matrix
        [a] = p # parameters
        der = [np.sqrt(y/((2*a)-y)), yd, 9.8]
        return der

    # time scale
    t = np.linspace(0, 10, 1000)

    # containing parameters and initial conditions
    p = [a]
    w0 = [x1, y1, 9.8]


    wsol = odeint(diffeqs, w0, t, args = (p, ))

    #plt.figure(figsize=(100, 100))
    #ax = plt.gca() #you first need to get the axis handle
    #ax.set_aspect() #sets the height to width ratio to 1.5. 
    plt.plot(wsol[:, 0], -1*wsol[:, 1], 'k-')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

brachistochrone(a, x1, y1)