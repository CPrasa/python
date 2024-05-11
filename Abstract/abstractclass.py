
#A class that contains one or more abstract methods is called an abstract class.
#A abstract method that method has declaration but does not have implementation

#we need to import module of abc


from abc import ABC, abstractclassmethod

class Phone(ABC):
  @abstractclassmethod
  def func(self):
    pass
  
  
#obj1 = Phone()

class Samsung(Phone):
  def func(self):
    pass

obj2 = Samsung()