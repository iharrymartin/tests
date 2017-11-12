import math
def my_sin(x):
	b = 0
        c = 50
	for i in range(c):
	 e = math.factorial(2*i+1)
	 f = x**(2*i+1)
	 if i % 2 == 0:	
	  b = b + f/e
	 else:
	  b = b - f/e
	return b
print 'sin(1.2)' 
print my_sin(1.2)
if __name__ == "__my_sin__":
 my_sin(a)
