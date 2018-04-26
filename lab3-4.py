from math import *
##Ejercicio 4
#Usando Newton-Raphson
#funcion:
def orig(x):
	return (9*(exp(-x))*sin(2*pi*x)) - 3.5



def deriv(x):
	return ( (9*exp(-x) ) * ( ( -sin(2*pi*x) ) + 2*pi*cos(2*pi*x)) )
def nraph(x0, es, imax):
	""" orig: funcion original
		deriv: derivada de esa funcion"""
	xr = x0
	iteracion = 0
	error = 1000
	while (es > error) or (iteracion < imax):
		xrold = xr
		xr = xrold - (orig(xrold)/deriv(xrold))
		iteracion = iteracion+ 1
		if (xr != 0):
			ea = abs((xr - xrold)/ xr) * 100
	return xr

respuestas = []
for a in range(-100,100):
	try: 
		a = nraph(a, 0.0001, 25)
		if (a >= 0):
			respuestas.append(a)
		else:
			pass
	except:
		pass

print "Las respuestas mayores a 0 son: "
print respuestas