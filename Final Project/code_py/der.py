import sympy as sp
import numpy as np
import math as mat

##################################

def givemeDEEEEEEE(*args): #ivar_str, dvar_str, dvar_str_0):
    
    m = 1.0
    M = 1.0
    l = 1.0
    g = -9.8
    R = 1.0
    w = 0.2

    #LAGRANGIAN
    def L(dvar, dvarp, ivar):
        return (1/2)*M*R*R*w*w + (1/2)*m*l*l*dvarp**2 + m*R*w*l*dvarp*(sp.sin(dvar - w*ivar)) - m*g*R*sp.sin(ivar) - l*sp.cos(dvar)
        #(m/2)*(R*R*w*w + L*L*dvarp**2 + 2*R*w*L*dvarp*sp.sin(dvar - w*ivar)) - m*g*(R*sp.sin(dvar - w*ivar) - L*sp.cos(dvar)) 
        #(1/2)*m*dvarp2**2 + (1/2)*M*dvarp2**2 + (1/2)*M*L*L*dvarp**2 + M*L*davrp*dvarp2*sp.cos(dvar) - (1/2)*k*dvar2**2 + M*g*L*sp.cos(dvar)
    
    if len(args) == 3:
        def convertEq(x):
            x = x.replace("Eq(", "")
            x = x.replace(", 0)", "")
            x = x + " = 0"
            return x

        def convertDE(de):
            de_str = str(de)
            de_str = de_str.replace("Derivative(" + args[-2] + "(" + args[-1] + "), (" + args[-1] + ", 2))", args[-3] + "'" + "'")
            de_str = de_str.replace("Derivative(" + args[-2] + "(" + args[-1] + "), " + args[-1] + ")", args[-3] + "'")
            de_str = de_str.replace(args[-2] + "(" + args[-1] + ")", args[-3])
            return de_str

        print('\n')

        # DEFINED
        ivar = sp.Symbol(args[-1])
        dvar = sp.Function(args[-2])(ivar)
        dvarp = sp.Derivative(dvar, ivar)
        #dvar2 = sp.Function(args[-4])(ivar)
        #dvarp2 = sp.Derivative(dvar, ivar)

        #def EulerLagrange():
        print("∂ℒ/∂" + args[-3] + "        =", sp.diff(L(dvar, dvarp, ivar), dvar))
        print('\n')         
        print("∂ℒ/∂" + args[-3] + "'" + "       =", sp.diff(L(dvar, dvarp, ivar), dvarp))
        print('\n')         
        print("d/d" + args[-1] + "(∂ℒ/∂" + args[-3] + "')" + "  =", sp.diff(sp.diff(L(dvar, dvarp, ivar), dvarp), ivar))
        print('\n')

        de = sp.simplify(sp.Eq(sp.diff(L(dvar, dvarp, ivar), dvar) - sp.diff(sp.diff(L(dvar, dvarp, ivar), dvarp), ivar), 0))

        #print(convertEq(str(de)))
        print("Your differential equation:")
        print(convertDE(convertEq(str(de))))

    #     #sp.solve(de, 1.0*Derivative(phi(t), t))
    #     #print(len(args))
        
        print("____________________________________________________________________________________")
        
givemeDEEEEEEE('ϕ', 'phi', 't') # first argument is the greek symbol, second is "greek -> english" symbol, and the third is the independent variable.
#'ϕ', 'phi',
#'y', 'y',
#urgent convention - L(args = [q2, q2', q1, q1', t])

##################################

# print('\n')
# # EXAMPLE 6.1, PAGE 221
# def L(y, yp, x):
#     return (1 + yp**2)**(1/2)

# x = sp.Symbol('x')
# y = sp.Function('y')(x)
# yp = sp.Derivative(y, x)

# print("∂L/∂y       =", sp.diff(L(y, yp, x), y))
# print("∂L/∂y'      =", sp.diff(L(y, yp, x), yp))
# print("d/dx(∂L/∂y') =", sp.diff(sp.diff(L(y, yp, x), yp), x))

# # VERIFY:
# #   ∂L/∂y = 0
# #   ∂L/∂y' = y'/sqrt(1+y'^2)
# #   d/dx(∂L/∂y') = 

# de = sp.Eq((sp.diff(L(y, yp, x), y) - sp.diff(sp.diff(L(y, yp, x), yp), x)), 0)

# print('\n')

# euLag = str(sp.diff(L(y, yp, x), y) - sp.diff(sp.diff(L(y, yp, x), yp), x))
# euLag_re = euLag.replace("Derivative(y(x), x)", "yd")
# print("d/dx(∂L/∂y') =", euLag_re.replace("Derivative(y(x), (x, 2))", "ydd"))

# sol = sp.solve(euLag, sp.Derivative(y, (x, 2)))

# print(sol)

# print("____________________________________________________________________________________________________")
# ################################################################################

# # print('\n')
# # # EXAMPLE 6.2, PAGE 222
# # def L(x, xp, y):
# #     return ((xp**2 + 1)/(y))**(1/2)

# # y = sp.Symbol('y')
# # x = sp.Function('x')(y)
# # xp = sp.Derivative(x, y)
# # #C = sp.symbol('C')

# # print("∂L/∂x       =", sp.diff(L(x, xp, y), x))
# # print("∂L/∂x'      =", sp.diff(L(x, xp, y), xp))
# # print("d/dy(∂L/∂x') =", sp.diff(sp.diff(L(x, xp, y), xp), y))

# # euLag_1 = str(sp.simplify(sp.diff(L(x, xp, y), xp)))

# # euLag_re = euLag_1.replace("Derivative(x(y), y)", "x'")
# # print("∂L/∂x' =", euLag_re.replace("Derivative(x(y), (y, 2))", "x''"))

# # # VERIFY:
# # #   ∂L/∂x = 0
# # #   ∂L/∂x' = 
# # #   d/dy(∂L/∂x') = 

# # de = sp.Eq(sp.diff(L(x, xp, y), x) - sp.diff(sp.diff(L(x, xp, y), xp), y), 0)

# # print('\n')

# # if sp.diff(L(x, xp, y), x) == 0:
# #     euLag = sp.Eq(sp.diff(L(x, xp, y), xp), )
# #     #sol = sp.solve(euLag, sp.Derivative())
# # if sp.diff(L(x, xp, y), xp) == 0:
# #     euLag = sp.Eq(sp.diff(L(x, xp, y), x), 0)

# # #else:
# # euLag = sp.diff(L(x, xp, y), x) - sp.diff(sp.diff(L(x, xp, y), xp), y)

# # sol = sp.solve(euLag, sp.Derivative(x, (y, 2)))

# # print(sol)

# print("____________________________________________________________________________________________________")
# ##################################################################################

# ##################################################################################

# def L(phi, phip, t): 
#     return (m/2.0)*(R*R*w*w + l*l*phip*phip + 2.0*R*w*l*phip*sp.sin(phi - w*t)) - m*g*(R*sp.sin(w*t) - l*sp.cos(phi))

# t = sp.Symbol('t')
# phi = sp.Function('phi')(t)
# phip = sp.Derivative(phi, t)

# # m = 1
# # R = 1
# # w = 0.2
# # l = 1
# # g = 1

# print("∂L/∂ϕ       =", sp.diff(L(phi, phip, t), phi))
# print('\n')
# print("∂L/∂ϕ'       =", sp.diff(L(phi, phip, t), phip))
# print('\n')
# print("d/dt(∂L/∂ϕ') =", sp.diff(sp.diff(L(phi, phip, t), phip), t))
# print('\n')

# eL1 = str(sp.diff(L(phi, phip, t), phi))

# eL1 = eL1.replace("Derivative(phi(t), t)", "ϕ'")
# print(eL1.replace("phi(t)", "ϕ"))

# eL2 = str(sp.diff(sp.diff(L(phi, phip, t), phip), t))

# eL2 = eL2.replace("Derivative(phi(t), (t, 2))", "ϕ''")
# eL2 = eL2.replace("Derivative(phi(t), t)", "ϕ'")
# print(eL2.replace("phi(t)", "ϕ"))

# de = sp.simplify(sp.Eq(sp.diff(L(phi, phip, t), phi) - sp.diff(sp.diff(L(phi, phip, t), phip), t), 0))
# de_str = str(de)
# de_str = de_str.replace("Derivative(phi(t), (t, 2))", "ϕ''")
# de_str = de_str.replace("Derivative(phi(t), t)", "ϕ'")
# de_str = de_str.replace("phi(t)", "ϕ")
# print(convertEq(de_str))

# #sp.solve(de, 1.0*Derivative(phi(t), t))
