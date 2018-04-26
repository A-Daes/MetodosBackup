from math import *
from sympy import *
def obtenerXM():
	x = 1.00
	xm = x
	print (x > 0)
	while (x > 0):
		x = x/2
		print x
		xm = x
	return xm

print "Ejercicio 1"
print obtenerXM()


def EjercicioDos():
	h = lambda x,y,z: x**2 + 3*y + 4*(3*z-y)
	k = lambda x,y,z: 3*x + 3*y -2*z

	r = h(3,2,1) - k(1,2,3)

	print r

print "Ejercicio 2"
EjercicioDos()

print "Ejercicio Tres"
value = float(input("Ingrese un numero (puede ser flotante) entre 0 y 100: "))

def EjercicioTres(x):
	if (x < 0 or x > 100):
		print "Valor erroneo"
	else:
		if (x <= 25):
			print "x esta dentro de [0, 25]"
		elif (x > 25) and (x <= 50):
			print "x esta dentro de (25, 50]"
		elif (x > 50) and (x <= 75):
			print "x esta dentro de (50, 75]"
		elif (x > 75):
			print "x esta dentro de (75, 100]"

EjercicioTres(value)

print "Ejercicio Cuatro"
vla, vlb, vlc = input("Ingrese a "), input("Ingrese b "), input("Ingrese c ")
def EjercicioCuatro(a, b, c):
	result = ((2*(a**2)) + cos(b) - 5*(a*(8*c)))
	if (result > 0):
		print "El resultado es mayor a 0"
	else: 
		print "El resultado es menor o igual a 0"
EjercicioCuatro(vla, vlb, vlc)


def f(x):
	return ((9.8*(65)/x))*(1-e**(-(x/65)*5)) - 45

maxiter = 25
a = 1.00
b = 5.00

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
		print "Se realizaron "
		print i
		print "iteraciones para encontrar la respuesta."
		print p

print "Ejercicio 6"
bisection(a, b)

x = symbols("x")
expr = ((9.8*(65)/x))*(1-e**(-(x/65)*5)) - 45

def NR(invalue, error, maxiter):
	xr = invalue
	iter = 0
	currentError = 1000
	while (currentError > error) or (iter < maxiter):
		xrold = xr
		xr = xrold - (f(xrold)/diff(expr, xrold))
		iter = iter + 1
		if xr != 0:
			currentError = Abs((xr - xrold)/xr) * 100
		print xr
NR(2, 0.001, 25)