from math import *

def expm(x, n):
	a = 0
	i = 0
	while (i <= n):
		a = a + ((x**n)/(factorial(n)))
		print a
		i = i+1 
	return a

x, n = float(raw_input("x: ")), float(raw_input("n: "))

print expm(x,n)
print "tru"
print exp(x)