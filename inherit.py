class Person :
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname


    def myName(self):
        print(self.fname+" "+self.lname)

p1=Person("akhiles","yadav")

p1.myName()

class Student(Person):
    def __init__(self,fname,lname,year):
     super().__init__(fname,lname)
     self.graduationyear = year

p2=Student("Deepa","yadav")
p2.myName()