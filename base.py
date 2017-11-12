import sys
class base1:
 def fun(self):
  print "hello, base1"
class derived(base1):
 def fun1(self):
  print "hello,derived"
a = derived()
a.fun()
a.fun1()
