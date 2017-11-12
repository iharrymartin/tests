import sys
class Complex:
 def __init__(self,real,img):
	self.real = real
	self.img  = img
 def __str__(self):
	return str(self.real)+ '+ i' + str(self.img)
 def add(self,other):
 	real = self.real+other.real
        img= self.img+other.img
        c = Complex(real,img)
        return c
 def mul(self,other):
	real = self.real+other.real-self.img*other.img
        img  = self.real*other.img+self.img*other.real
        d = Complex(real,img)
        return d
a = Complex(1,2)
b = Complex(3,4)
c = a.add(b)
d = a.mul(b)
print c
print d
