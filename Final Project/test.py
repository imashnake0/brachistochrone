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

def brachistochrone(a, x1, y1):
    def diffeqs(w, y, p):
        [x, y] = w # d matrix
        [a] = p # parameters
        if y/((2*a)-y) >= 0:
            der = [np.sqrt(abs((y/((2*a)-y)))), 1]
        else:
            der = [np.sqrt(abs((y/((2*a)-y)))), 1]
        return der

    # time scale
    t = np.linspace(0, 100, 50000)

    # containing parameters and initial conditions
    p = [a]
    w0 = [x1, y1]


    wsol = odeint(diffeqs, w0, t, args = (p, ))
    #print(len(wsol[:, 1]))
    for i in range(0, len(wsol[:, 1])):
        if (wsol[i, 1] >= 2*a):
            wsol[i, 1] *= -1
            wsol[i, 1] += 4*a

    y_values = []
    for i in range(len(wsol[:, 1])):
        if wsol[i, 1] >= 0:
            y_values.append(-1*wsol[i, 1])  

    x_values = []
    for i in range(len(y_values)):
        x_values.append(wsol[i, 0])


    #plt.figure(figsize=(100, 100))
    #ax = plt.gca() #you first need to get the axis handle
    #ax.set_aspect() #sets the height to width ratio to 1.5. 
    plt.plot(x_values, y_values, 'k-')
    plt.xlabel('x')
    plt.ylabel('y')

for a in np.linspace(1, 20, 100): #np.linspace(0, 100, 50):
    brachistochrone(a, x1, y1)

plt.show()