

def orig(x):
	return ((x**3)-(6*(x**2))+(11*x)-6.1)
def deriv(x):
	return ((3*(x**2))-(12*x)+11)

def nraph(x0, es, imax):
	xr = x0
	iteracion = 0
	error  = 1
	while ((error > es)):
		if (iteracion < imax):
			xrold = xr
			xr = xrold - (orig(xrold)/deriv(xrold))
			iteracion = iteracion + 1
			if (xr != 0):
				error = abs((xr - xrold)/ xr) * 100
		else: 
			break
	return xr, iteracion

##Ejercicio 1
###Mas peque;a
print nraph(-100, 0.0001, 25)
###Mas grande
print nraph(100, 0.0001, 25)
###Mediana
print nraph(2, 0.0001, 25)
