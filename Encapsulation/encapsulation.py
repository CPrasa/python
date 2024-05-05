

# Creating a base class 
class Base: 
	def __init__(self): 

		# Protected member 
		self._a = 2




obj1 = Derived() 

obj2 = Base() 


print("Accessing protected member of obj1: ", obj1._a) 


print("Accessing protected member of obj2: ", obj2._a) 
