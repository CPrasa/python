

class Car():
  def __init__(self,name,color):
    self.name = name
    self.__color = color
    
  def get_color(self):
    return(self.__color)
  
  def set_color(self, x):
    self.__color = x
    
car1 = Car("Mastang","Blue")

print(car1.name)
print(car1.get_color())

car1.set_color("Red")
print(car1.get_color())
  