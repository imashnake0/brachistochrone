import numpy as np
from numpy import loadtxt
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math as mat

#parameters
#a = 6

# initial conditions (here, and final)
x1 = 0
y1 = 0
#x2 = 
#y2 = 

def abs(x):
    if x<0:
        return -1*x
    else:
        return x

#def arr_dub(x):
#    x_0 = []
#    for i in range()

def brachistochrone(a, x1, y1):
    def diffeqs(w, y, p):
        [y] = w # d matrix
        [a] = p # parameters
        der = [np.sqrt((1-a*a*y/(a*a*y)))]
        return der
    
    # time scale
    y = np.linspace(0, 100, 50000)

    # containing parameters and initial conditions
    p = [a]
    w0 = [y1]

    wsol = odeint(diffeqs, w0, y, args = (p, ))
    #print(wsol[:, 0])

    # THIS FIXED IT! - or not...
    #for i in range(0, len(wsol[:, 1])):
    #   if wsol[i, 1] > 2*a:
    #        wsol[i, 1] *= -1
    #        wsol[i, 1] += 4*a 
    
    #y_values = []
    #for i in range(0, len(wsol[:, 1])):
    #    if wsol[i, 1] >= 0:
    #        y_values.append(-1*wsol[i, 1])

    #x_values = []
    #for i in range(0, len(y_values)):
    #    x_values.append(wsol[i, 0])

    #print(len(y_values), len(wsol[:, 1]))
    #plt.figure(figsize=(100, 100))
    #ax = plt.gca() #you first need to get the axis handle
    #ax.set_aspect() #sets the height to width ratio to 1.5. 
    plt.plot(y, -1*wsol[:, 0], 'k-')
    plt.xlabel('x')
    plt.ylabel('y')

for a in [1]: #np.linspace(0, 100, 50):
    brachistochrone(a, x1, y1)

plt.show()