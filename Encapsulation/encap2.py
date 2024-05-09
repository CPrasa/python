class Base: 
    def __init__(self): 
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"
        
    def get_c(self):
      return self.__c
  
# Creating a derived class 
class Derived(Base): 
    def __init__(self): 
  
        # Calling constructor of 
        # Base class 
        Base.__init__(self) 
        print("Calling private member of base class: ") 
        print(self.__c) 
  
  
# Driver code 
obj1 = Base() 
print(obj1.a)




class Perant:
    def __init__(self, name, age, child, salary):
        self.name = name
        self.age = age
        self.child = child
        self.__salary = salary
    def get_salary(self):
        return self.__salary

class son(Perant):
    def __init__(self):
        pass
    
a = Perant("Chathu","24","Son1","200000")
print(a.age)

print(a.get_salary())
        
              