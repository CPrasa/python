class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, school, grade):
        super().__init__(fname, lname)
        self.school = school
        self.grade = grade

    def print_details(self):
        print("Name:", self.firstname, self.lastname)
        print("School:", self.school)
        print("Grade:", self.grade)


x = Person("John", "Doe")
x.printname()

y = Student("Chathurya", "Prasad", "XYZ School", 10)
y.print_details()
