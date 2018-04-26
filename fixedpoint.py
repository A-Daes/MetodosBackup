from math import *

def fpf(x):
	#return (sqrt(2*x))
	return ((x**3)-(6*(x**2))+(11*x)-6.1)

"""x0: estimacion inicial de la raiz
es: error esperado
imax: iteraciones maximas """
def fixedpoint(x0, es, imax):
	xr = (x0)
	iteracion = 0
	error = 1000
	while ((es < error) and (iteracion <= imax)):
		xrold = (xr)
		xr = fpf(xrold)
		print xr
		iteracion = iteracion + 1
		if xr != 0:
			error = abs((xr - xrold)/xr) * 100
	print "Iteraciones: " 
	print iteracion
	print "Error: "
	print error
	print "Raiz: " 
	print xr


fixedpoint(2, 0.0001, 10000)