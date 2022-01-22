# LIBRARIES
import sympy as sp

# FUNCTION
def givemeDE(*args):
   
    #PARAMETERS
    m = 1.0
    l = 1.0
    g = 1.0
    R = 0.2
    w = 0.2

    #LAGRANGIAN
    def L(dvar, dvarp, ivar):
        return (1/2)*m*R*R*w*w + (1/2)*m*l*l*dvarp**2 + m*R*w*l*dvarp*(sp.sin(dvar - w*ivar)) - m*g*R*sp.sin(ivar) + m*g*l*sp.cos(dvar)
    
    if len(args) == 3:
        # AESTHETICS
        def convertEq(x):
            x = x.replace("Eq(", "")
            x = x.replace(", 0)", "")
            x = x + " = 0"
            return x
        # AESTHETICS
        def convertDE(de):
            de_str = str(de)
            de_str = de_str.replace("Derivative(" + args[-2] + "(" + args[-1] + "), (" + args[-1] + ", 2))", args[-3] + "'" + "'")
            de_str = de_str.replace("Derivative(" + args[-2] + "(" + args[-1] + "), " + args[-1] + ")", args[-3] + "'")
            de_str = de_str.replace(args[-2] + "(" + args[-1] + ")", args[-3])
            return de_str

        # DEFINES ASSIGNED SYMBOLS
        ivar = sp.Symbol(args[-1])
        dvar = sp.Function(args[-2])(ivar)
        dvarp = sp.Derivative(dvar, ivar)

        # PRINTS EACH TERM OF THE LAGRANGIAN
        print("∂ℒ/∂" + args[-3] + "        =", convertDE(sp.diff(L(dvar, dvarp, ivar), dvar)))
        print('\n')         
        print("∂ℒ/∂" + args[-3] + "'" + "       =", convertDE(sp.diff(L(dvar, dvarp, ivar), dvarp)))
        print('\n')         
        print("d/d" + args[-1] + "(∂ℒ/∂" + args[-3] + "')" + "  =", convertDE(sp.diff(sp.diff(L(dvar, dvarp, ivar), dvarp), ivar)))

        # FINDS DE USING TERMS ABOVE
        de = sp.simplify(sp.Eq(sp.diff(L(dvar, dvarp, ivar), dvar) - sp.diff(sp.diff(L(dvar, dvarp, ivar), dvarp), ivar), 0))

        print('\n')

        # PRINTS OUT DE
        print("Required DE      :", convertDE(convertEq(str(de))))
        
        #print("Required Solution:", sp.dsolve(de))
# EXECUTE PROGRAM!
givemeDE("φ", "φ", "t")