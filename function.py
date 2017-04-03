
def compute_surface(radius):
	from math import pi
	return pi*radius*radius
	
i = 0
def increment():
	global i
	i += 1
c = 1
def function(a,b):
	global c
	def inner_function(x):
		print c,x*x*x
		y = x*x*x + c
		#c = c + 1 
		return y
	return inner_function(a) + inner_function(b)

def square(x): return x*x
#print compute_surface(4.3),'\n'
#increment()
#increment()
#increment()
#increment()
#print i,'\n'
#print inner_function(2)
#print inner_function(3)
#print function(2,3)
#print function(2,3)
sq = square
print id(square)
print id(sq)
