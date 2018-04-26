from math import *
def orig(x):
	return ((x**3)-(6*(x**2))+(11*x)-6.1)
def deriv(x):
	return ((3*(x**2))-(12*x)+11)

def f(x):
	return ((9.8*x)/14) * (1- exp(-(14/x)*8)) - 35

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


def fixedpoint(x0, es, imax):
	""" fpf: funcion original"""
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


def bisection(a, b):
	""" f: funcion original"""
	i = 0
	full = False
	found = False
	while found == False or (i < maxiter):
		c = float((a + b) / 2)
		if f(a) * f(c) <= 0:
			b=float(c)
		else:
			a=float(c)
		p = f(c)

		if(p < 0.001) and (p > -0.001):
			found = True
			break
		else:
			pass
		i= i+1

		if (i == maxiter):
			print "Se llego al maximo numero de iteraciones"
			full = True
			break
		else:
			pass

	if full == False:

		print "El valor es:" 
		print a



def regulafalsi(a, b):
	""" f: funcion original"""
	full = False
	i = 0
	found = False
	while found == False or (i < maxiter):
		c = (a*f(b) - b*f(a))/(f(b) - f(a))
		if (f(a) * f(c)) < 0:
			b = c
		elif (f(a)*f(c)) > 0:
			a = c
		else:
			found = True
		i = i + 1
		if (i == maxiter):
			print "Se alcanzaron todas las iteraciones"
			full = True

			break
		else:
			pass
		print c
		p = f(c)
		if(p < 0.02) and (p > -0.02):
			found = True
			break
		else:
			pass
	if full == False:

		print "El valor es:" 
		print a
