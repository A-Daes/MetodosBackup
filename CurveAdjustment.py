'''
Pseudocodigo:

	Obtener A1 y A0:
		Obtener sumatoria de x*y S(xiyi)
		Obtener sumatoria de x & y  S(xi)s(yi)
		Obtener sumatoria de x^2 S(xi^2)
		Obtener Promedio de xi & yi, xp & yp
		
		A1:
		Formula: (n*S(xiyi) - S(xi)*S(yi)) / (n*S(xi^2) - S(xi) ^2)
		
		A0: 
		Formula: yp - a1xp

		Y = a1x + a0

		Falta: Desviaciones, plot, convertir strings a listas
'''

import sys
from math import *
import numpy
import matplotlib.pyplot as plt
import Tkinter

def getFirstSums(x,y, cnt):
	'''
	Input:                    || Output:
		x = valores de x (lista) || sXY = Sumatoria de valores de x*y
		y = valores de y (lista) || sX = Sumatoria de valores de x
		cnt = arraysize			 || sY = Sumatoria de valores de y
		                         || sXs = Sumatoria de valores de x^2 (sumXsquared)
								 || avgX = Promedio de valores de x
                                 || avgY = Promedio de valores de y
	Obtiene los valores necesarios para determinar a1 y a0
	'''

	#Obtner la longitud de el arreglo
	#Obtener una lista con x*y
	XY = []
	for n in range(0,len(x)):
		XY.append(x[n]*y[n])

	#Obtener una lista con x^2
	Xs = []
	for n in range (0,len(x)):
		Xs.append(x[n]**2)

	#Sumatorias en orden: XY, X, Y, X^2 
	sXY = sum(XY)
	sX = sum(x)
	sY = sum(y)
	sXs = sum(Xs)

	#Promedios de x y y


	avgX = sX/cnt
	avgY = sY/cnt

	return sXY, sX, sY, sXs, avgX, avgY


def getDeviationSums(ylist, yavg, a0, a1, xlist):
	'''
	input:                               || output:
	ylist: lista de valores de y 		 || sTerm: valor para sY
	yavg: promedio de y          		 || sTerm2: valor para sy/x
	a0, a1: valores obtenidos de a0 y a1 ||
	xlist: lista de valores de x   		 ||
	'''

	sTerm = 0
	sTerm2 = 0
	for n in range(0, len(ylist)):
		sTerm = sTerm + ((ylist[n] - yavg)**2)

	for n in range(0, len(xlist)):
		sTerm2 = sTerm2 + (ylist[n] - a0 - (a1*xlist[n]))**2

	return sTerm, sTerm2



def generateYString(a, b, forma):
	'''
 	Input:     || Output: 
	a = a1     || yString = "y = a1x + a0"
	b = a0     ||
	'''
	if (forma == "lineal"):
		yString = "y = " + str(a) + "x + " + str(b)
	elif (forma == "racional"):
		yString = "y = x /(" + str(b) + "x + " + str(a) + ")"
	else:
		b = (10**b)
		yString = str(a) +"^(x*" + str(b) + ")"
	return yString

def convert2Log(x, y):
	newX = []
	newY = []
	for n in range(0, len(x)):
		a = x[n]
		b = y[n]
		newX.append(log(a, 10))
		newY.append(log(b, 10))

	return newX, newY

def convert2Rational(x, y):
	newX = []
	newY = []
	for n in range(0,len(x)):
		newX.append(1.0/x[n])
		newY.append(1.0/y[n])
	return newX, newY


#raw_xlist = raw_input("Ingrese los valores de x separados por comas: \n ")
#raw_ylist = rw_i,nput("Ingrese los valores de y separados por comas: \n ")

#[Convertir strings a listas de ints]

problema = raw_input("Numero de problema: ")
if (problema == "1"):
	xList = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43]
	yList = [59.82, 67.22,69.71,78.47,77.65,87.33,85.61,87.55,89.2,93.59,94.77,99.77,101.59,107.27,103.83,108.26,108.6,106.84,106,110.09,112.11,111.07,115.97,113.82,118.62,114.38,119.1,114.79,121.44,117.06,116.64,116.21,118.74,118.25,121.74,122.21,126.66,122.09,125.51]
elif (problema == "2"):
	xList = [21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
	yList = [304.09,365.53,443.68,543.8,657.86,813.73,1004.33,1220.92,1491.35,1815.43,2225.37,2728.3,3298.93,4021.31,4954.85,6031.44,7360.93,8987.88,10979.71,13404.31,16382.28,20239.8,24446.47,29604.1,36493.88,44545.08,54457.71,66342.52,80992.85,99219.1]
else:
	xList = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43]
	yList = [4.025820746,2.081185747,7.392335408,3.971411146,11.82938728,8.976311575,10.4214753,12.17353848,17.24062499,19.6303968,26.35011303,30.40667789,38.80668006,38.55642565,46.66196594,51.12912104,53.96350026,58.1705197,67.75541773,75.7232685,84.07899389,88.82737419,100.9730576,104.5205687,119.4743163,123.8386002,132.6176175,141.8154688,154.4361627,164.4836211,178.9616839,190.8741121,207.2245928,215.0167418,231.254107,243.9401716,255.078357,267.6720251,285.7244808]
if (len(xList) != len(yList)):
	print "La cantidad de elementos en x debe ser la misma que los elementos de y"
	sys.exit()

else:

	plt.plot(xList, yList, 'co')
	plt.show()


	forma = str(raw_input("A que tipo de grafica se parecia la anterior? (racional, axb, aex, lineal): "))

	#forma  = "racional"
	if forma == "racional":
		xList, yList = convert2Rational(xList, yList)

	elif forma == "axb":
		xList, yList = convert2Log(xList, yList)

	elif forma == "aex":
		print "ae^x not yet implemented"
		sys.exit()

	elif forma == "lineal":
		pass

	else:
		"Forma incorrecta."
		sys.exit()

	arraySize = len(xList)
	sumXY, sumX, sumY, sumXS, averageX, averageY = getFirstSums(xList, yList, arraySize)
	

	print ((arraySize*(sumXS)))
	print  (sumX**2)
	
	##Formula: (n*S(xiyi) - S(xi)*S(yi)) / (n*S(xi^2) - S(xi) ^2)
	A1 = ( ( (arraySize*sumXY) - (sumX*sumY) ) / ((arraySize*(sumXS)) - (sumX**2)))

	##Formula: yp - a1xp

	A0 = averageY - (A1 * averageX)


	print "A1 = " + str(A1) + "\nA0 = " + str(A0)

	print "Ecuacion: " + generateYString(A1, A0, forma)

	devT1, devT2 = getDeviationSums(yList, averageY, A0, A1, xList)


	stdDev = sqrt(devT1/(arraySize - 1))
	nstdDev = sqrt(devT2/(arraySize - 1))


	rSquared = (stdDev - nstdDev)/stdDev
	print "R^2 = " + str(rSquared)
	if (nstdDev < stdDev):
		print "Ajuste correcto\n Desviacion de estimacion < Desviacion estandar"
		print str(nstdDev) + "<" + str(stdDev)
	else:
		print "Ajuste incorrecto"


