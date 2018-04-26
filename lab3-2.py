from math import *
## Ejercicio 2
#Funcion : 
def f(x):
	return ((9.8*x)/14) * (1- exp(-(14/x)*8)) - 35
#Usando Biseccion
maxiter = 100
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

bisection(1.00, 100.00)