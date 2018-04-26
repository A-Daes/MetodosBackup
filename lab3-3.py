from math import *
##Ejercicio 3

#Funcion:
def f(x):
	return 10 * (1 - exp(-0.04*x)) - 4*exp(-0.04*x) - 9.3

#Usando Biseccion
maxiter = 10000000

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

bisection(0.001, 100.00)