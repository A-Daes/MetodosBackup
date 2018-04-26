from numpy import *

def funcI(x,y):
	return 2*x - cos(y)

def funcII(x,y):
	return 2*y - sin(x)

def Determinant(x,y):
	return 4+ cos(x)*sin(y)

def getJmulF(Jac, F):
	return matmul(Jac, F)

def Newton(x,y):
	##xn  = x - 1/D * [JacX(cambiados)] * [F]
	xn = x - 1/Determinant(x,y) * getJmulF(Jac, F)[0][0]
	yn = y - 1/Determinant(x,y) * getJmulF(Jac, F)[1][0]
	return xn, yn,


Newton(1,1)