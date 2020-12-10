import numpy as np
from numpy import loadtxt
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math as mat

#parameters


# initial conditions (here, and final)
#x1 = 0
#y1 = 0
#x2 = 
#y2 = 

def abs(x):
    if x<0:
        return -1*x
    else:
        return x

def brach():
    def diffeqs(w, y, p):
        [x, xp] = w # d matrix
        [] = p # parameters
        der = [xp, -1.0*np.sin(x) + 0.008*np.cos(0.2*y - x)]
        return der

        # time scale
    y = np.linspace(0.0, 20, 100)

    #print(1/((4*C)**(1/2)))

    # containing parameters and initial conditions
    p = []
    w0 = [0.2, 0]

    wsol = odeint(diffeqs, w0, y, args = (p, ))
    plt.plot(y, wsol[:, 0])
# THIS FIXES THE HALF-GRAPHS, IGNORE FOR NOW.
'''
    y1 = []
    for i in range(0, len(wsol[:, 1])):
        if i>2 and wsol[i, 1] != 0:
            y1.append(-1*wsol[i, 1])

    y2 = []
    for i in range(0, len(y1)):
        y2.append(y1[-1*(i+1)])
    
    y1.pop()

    y3 = y1 + y2

    x1 = []
    for i in range(0, len(wsol[:, 0])):
        if i>2 and wsol[i, 0] != 0:
            x1.append(wsol[i, 0])

    x2 = []
    for i in range(0, len(x1)):
        x2.append(-1*x1[-1*(i+1)] + 2*np.pi*a)

    x1.pop()
    x2[0] = np.pi

    x3 = x1 + x2

    #print(x3)
    #print(len(x1), len(y3))
    #print(x1[1993])

    #plt.figure(figsize=(100, 100))
    #ax = plt.gca() #you first need to get the axis handle
    #ax.set_aspect() #sets the height to width ratio to 1.5. 
    
    plt.plot(x3, y3, 'k-')
    #plt.xlabel('x')
    #plt.ylabel('y')
'''
#for a in np.linspace(1, 10, 30): #np.linspace(0, 100, 50):
#for a in range(0, 20):
    #for b in range(0, 20):
brach()

plt.show()