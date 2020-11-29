import sympy as sp
import numpy as np
#print(sp.idiff(y*x**2, x, y))


#def manyArgs(*arg):
#    print "I was called with", len(arg), "arguments:", arg

def L(y, yp, x):
    return (1 + yp**2)**(1/2)

x = sp.Symbol('x')
y = sp.Function('y')(x)
yp = sp.Derivative(y, x)
#L = sp.Function('y', "y'", 'x')
#t = sp.Symbol('t')

#print(sp.Derivative)
#print(sp.idiff(sp.diff(f(y, yp, x), yp), t) 

# sp.idiff() is not what you're looking for: 

#rhs = sp.diff(L(y, yp, x), yp)

# for L = (1 + yp**2)**(1/2): 
# -1.0*(y'(x)**2 + 1)**(-1.5)*y'(x)**2*Derivative(y'(x), x) + 1.0*(y'(x)**2 + 1)**(-0.5)*Derivative(y'(x), x)

print("∂L/∂y       =", sp.diff(L(y, yp, x), y))
print("∂L/∂y'      =", sp.diff(L(y, yp, x), yp))
print("d/dx(∂L/∂y) =", sp.diff(sp.diff(L(y, yp, x), yp), x))

# Have to get python to "define the equation".
#Lagrangian = sp.Eq(sp.diff(L(y, yp, x), y) - sp.diff(sp.diff(L(y, yp, x), yp), x))

#print(sp.idiff(, y, x))