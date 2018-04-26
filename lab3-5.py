from math import *

##usando punto fijo
#Funcion G(x)
def fpf(x):
	return (( (6*(x**2)) - 11*x + 6.1))**(1.0/3.0)


def fixedpoint(x0, es, imax):
	""" fpf: funcion original"""
	xr = (x0)
	iteracion = 0
	error = 1000
	while ((es < error) and (iteracion <= imax)):
		xrold = xr
		xr = fpf(xrold)
		iteracion = iteracion + 1
		if xr != 0:
			error = abs((xr - xrold)/xr) * 100
	print "Iteraciones: " 
	print iteracion
	print "Error: "
	print error
	print "Raiz: " 
	print xr

fixedpoint(3.00, 0.0001, 25)
fixedpoint(1.00, 0.0001, 25)
fixedpoint(2.00, 0.0001, 25)