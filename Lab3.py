from MetodosRaices import *



##Funciones de Ejercicio 1
def orig(x):
	return ((x**3)-(6*(x**2))+(11*x)-6.1)
def deriv(x):
	return ((3*(x**2))-(12*x)+11)
##Usando Newton-Raphson
##Ejercicio 1
###Mas peque;a
print nraph(-100, 0.0001, 100)
###Mas grande
print nraph(100, 0.0001, 100)
###Mediana
print nraph(2, 0.0001, 100)

