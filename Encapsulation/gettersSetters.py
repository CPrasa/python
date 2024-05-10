

class Car():
  def __init__(self,name,color):
    self.name = name
    self.__color = color
    
  def get_color(self):
    return(self.__color)
    
car1 = Car("Mastang","Blue")

print(car1.name)
print(car1.get_color())
  