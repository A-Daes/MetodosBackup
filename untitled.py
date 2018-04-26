from math import *
def f(x):
	return ((x**3)-(6*(x**2))+(11*x)-6.1)


maxiter = 1000000
a = 5.00
b = 10.00

def bisection(a, b):
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

regulafalsi(a,b)