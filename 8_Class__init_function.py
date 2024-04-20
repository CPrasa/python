
##The __init__() function is called automatically every time the class is being used to create a new object.

#The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

#It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:


class Person :
  def __init__(self,name,age):
    self.name = name
    self.age = age
    
p1 = Person ("Chathurya",24)

print(p1.age)
print(p1.name)


print(p1)


class Car :
  def __init__(car,color,brand):
    car.color=color
    car.brand=brand
    
  def mycar(car,speed, hight):
    car.speed=speed
    car.hight=hight
    
car1 = Car("Red", "BMW")

car1.mycar(250,10)

print(car1.brand)
print(car1.color)
print(car1.hight)
print(car1.speed)



#Modify Object Properties

car1.brand = "Mustang"
print(car1.brand)

#Delete Object Properties

del car1.brand


#without content create class can be avoid errors using pass key word

class myclass :
  pass


class Chathury:
  pass
  
  
class Bus :
  def __init__(bus,color,brand):
    bus.color=color
    bus.brand=brand
    
    
  def mybus(bus, speed, test):
    bus.speed = speed
    bus.test = test 
      
    
bus1 = Bus('red','TATA')
bus1.mybus('250','green card')
bus1.mybus('255','green card')

print(bus1.speed)
print(bus1.brand) 



class Trees:
  def __init__(tree, type, hight):
    tree.type = type
    tree.hight = hight
    
tree1=  Trees("Short", "252")

print(tree1.hight)   
  
class family:
  def __intit__(father, mother, son, sister):
    pass
  
print(Trees)