
#A class that contains one or more abstract methods is called an abstract class.
#A abstract method that method has declaration but does not have implementation




import abc 
  
  
class AbstractClass(metaclass=abc.ABCMeta): 
    def abstractfunc(self): 
        return None
  
  
print(AbstractClass.register(dict)) 