''' 
Diferenciador numerico de funciones
Diego Alvarez
14104
''' 

from math import *
from prettytable import *

def Function(x):
	#return (-0.1*(x**4)) + (-0.15*(x**3)) - (0.5*(x**2)) - (0.25*x) + 1.2
	return exp(2*x)

def Derivate(x, h, real):
	
	##Obtener valores de atras, medio y adelante
	xa = x-h
	x0 = x
	x1 = x+h
	x2 = (x+2*h)
	
	##Obtener valor de la funcion en valores xa, x0 y x1
	fa = Function(xa)
	f0 = Function(x0)
	f1 = Function(x1)
	f2 = Function(x2)


	##Derivate

	fDerivativeFront = (f1 - f0)/(h)
	fDerivativeFrontError =  abs((real - fDerivativeFront)/real) * 100

	fDerivativeBack = (f0 - fa)/(h) 
	fDerivativeBackError =  abs((real - fDerivativeBack)/real) * 100

	fDerivativeCenter = (f1 - fa)/(2*h)
	fDerivativeCenterError =  abs((real - fDerivativeCenter)/real) * 100

	##Three points
	fDerivativeFrontThreeP = ((-3*f0) - (4*f1) + (3*f2)) / 2
	fDerivativeFrontThreePError =  abs((real - fDerivativeFrontThreeP)/real) * 100


	returnMatrix = [["Metodo", "Valor", "Error"], ["2 Puntos", "", ""], ["Adelante", fDerivativeFront, fDerivativeFrontError], ["Atras", fDerivativeBack, fDerivativeBackError], ["Centrado", fDerivativeCenter, fDerivativeCenterError], ["Tres Puntos", "", ""], ["Adelante", fDerivativeFrontThreeP, fDerivativeFrontThreePError]]

	##Print all Errors and Values
	returnTable = PrettyTable()
	returnTable.set_field_names(returnMatrix[0])

	for row in returnMatrix:
		if row == 0:
			pass
		else:
			returnTable.add_row(returnMatrix[row])

	return returnTable


print Derivate(1.1, 0.1, 18.05)