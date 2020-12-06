import sympy as sp
import numpy as np

#print(sp.idiff(y*x**2, x, y))

#def manyArgs(*arg):
#    print "I was called with", len(arg), "arguments:", arg

###

#L = sp.Function('y', "y'", 'x')
#t = sp.Symbol('t')

#print(sp.Derivative)
#print(sp.idiff(sp.diff(f(y, yp, x), yp), t) 

# sp.idiff() is not what you're looking for: 

#rhs = sp.diff(L(y, yp, x), yp)

# for L = (1 + yp**2)**(1/2): 
# -1.0*(y'(x)**2 + 1)**(-1.5)*y'(x)**2*Derivative(y'(x), x) + 1.0*(y'(x)**2 + 1)**(-0.5)*Derivative(y'(x), x)

###

#Sol = sp.solve(Eq, sp.diff(sp.diff(y, x), x))
#print(sp.integrate(sp.diff(sp.diff(y, x), x), x))
#print(sp.integrate(sp.integrate(sp.diff(sp.diff(y, x), x), x), x))

# Have to get python to "define the equation".

###

#euLagd = euLag.subs(sp.Derivative(y, (x, 2)), "ydd")

###

#print(sp.dsolve(de, y))

print('\n')
# EXAMPLE 6.1, PAGE 221
def L(y, yp, x):
    return (1 + yp**2)**(1/2)

x = sp.Symbol('x')
y = sp.Function('y')(x)
yp = sp.Derivative(y, x)

print("∂L/∂y       =", sp.diff(L(y, yp, x), y))
print("∂L/∂y'      =", sp.diff(L(y, yp, x), yp))
print("d/dx(∂L/∂y') =", sp.diff(sp.diff(L(y, yp, x), yp), x))

# VERIFY:
#   ∂L/∂y = 0
#   ∂L/∂y' = y'/sqrt(1+y'^2)
#   d/dx(∂L/∂y') = 

de = sp.Eq((sp.diff(L(y, yp, x), y) - sp.diff(sp.diff(L(y, yp, x), yp), x)), 0)

print('\n')

euLag = sp.diff(L(y, yp, x), y) - sp.diff(sp.diff(L(y, yp, x), yp), x)

sol = sp.solve(euLag, sp.Derivative(y, (x, 2)))

print(sol)

print("____________________________________________________________________________________________________")
################################################################################

print('\n')
# EXAMPLE 6.2, PAGE 222
def L(x, xp, y):
    return ((xp**2 + 1)/(y))**(1/2)

y = sp.Symbol('y')
x = sp.Function('x')(y)
xp = sp.Derivative(x, y)
#C = sp.symbol('C')

print("∂L/∂x       =", sp.diff(L(x, xp, y), x))
print("∂L/∂x'      =", sp.diff(L(x, xp, y), xp))
print("d/dy(∂L/∂x') =", sp.diff(sp.diff(L(x, xp, y), xp), y))

euLag_1 = str(sp.simplify(sp.diff(L(x, xp, y), xp)))

euLag_re = euLag_1.replace("Derivative(x(y), y)", "x'")
print("∂L/∂x' =", euLag_re.replace("Derivative(x(y), (y, 2))", "x''"))

# VERIFY:
#   ∂L/∂x = 0
#   ∂L/∂x' = 
#   d/dy(∂L/∂x') = 

de = sp.Eq(sp.diff(L(x, xp, y), x) - sp.diff(sp.diff(L(x, xp, y), xp), y), 0)

print('\n')

#if sp.diff(L(x, xp, y), x) == 0:
#    euLag = sp.Eq(sp.diff(L(x, xp, y), xp)), C)

#if sp.diff(L(x, xp, y), xp)) == 0:
#    euLag = sp.Eq(sp.diff(L(x, xp, y), x), 0)

euLag = sp.diff(L(x, xp, y), x) - sp.diff(sp.diff(L(x, xp, y), xp), y)

sol = sp.solve(euLag, sp.Derivative(x, (y, 2)))

print(sol)

print("____________________________________________________________________________________________________")
##################################################################################

print('\n')

l = 1.0
m = 1.0
w = 0.2
g = 1.0
R = 0.2

def L(phi, phip, t): 
    return (m/2.0)*(R*R*w*w + l*l*phip*phip + 2.0*R*w*l*phip*sp.sin(phi - w*t)) - m*g*(R*sp.sin(w*t) - l*sp.cos(phi))

t = sp.Symbol('t')
phi = sp.Function('phi')(t)
phip = sp.Derivative(phi, t)

print("∂L/∂ϕ       =", sp.diff(L(phi, phip, t), phi))
#print('\n')
print("∂L/∂ϕ'       =", sp.diff(L(phi, phip, t), phip))
#print('\n')
print("d/dt(∂L/∂ϕ') =", sp.diff(sp.diff(L(phi, phip, t), phip), t))
#print('\n')

de = sp.simplify(sp.Eq(sp.diff(L(phi, phip, t), phi) - sp.diff(sp.diff(L(phi, phip, t), phip), t), 0))

#phidd = Derivative(phi(t), (t, 2))
#phid = Derivative(phi(t), t)
#phi = phi(t)
#sp.classify_ode(de)

sp.solve(de, 1.0*Derivative(phi(t), t))