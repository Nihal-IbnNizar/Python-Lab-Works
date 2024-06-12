class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname,self.lastname)
        
x = Person("Muhammed","Nihal")
x.printname()
    
class Student(Person):
    def __init__(self,fname,lname,age):
        super().__init__(fname,lname)
        self.age = age

x = Student("Majo","Augustine",22)
x.printname()
print(x.age)