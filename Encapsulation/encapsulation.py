
class  Base:
  def __init__(self):
    
    #protected member
    self._a = 2
    
#creating a derived class

class Derived(Base):
  def __init__(self):
    
    #calling constructor of Base class
    
    Base.__init__(self)
    print("Calling protected member of base class: " self._a)
    
    