class MyClass:
  x = 5

p1=MyClass()
print(p1.x)


class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
                
                
  def myFun(self):
      print("my name is " + self.name)

p1=Person("Jhon",36)    
print(p1.name)
print(p1.age)
p1.myFun() 


class Person1:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person1("John", 36)

print(p1)