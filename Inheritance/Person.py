class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
    
  def printname(self):
    print(self.firstname, self.lastname)
    
    
  #Use the person class to create an object, and then execute the printname method:
  
x = Person("John","Doe")
x.printname()



class Student(Person):
  def __init__(self, fname, lname, school, grade):
    super().__init__(self, fname, lname)
    self.school = school
    self.grade = grade
    

  
  


y = Student("Chathurya", "Prasad")
y.printname()