x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x,y,z)
a = str(5)
b = int(5)
c = float(5)
# print(a,b,c)
print(type(a))
print(type(b))
print(type(c))

#Variable names are case-sensitive.

                #Multi Words Variable Names

#Camel CAse

myVariableName = "John"

#Pascal Case

MyVariableName = "John"

# Snake Case

my_variable_name = "John"

#Python allows you to assign values to multiple variables in one line:
#Make sure the number of variables matches the number of values, or else you will get an error.
x, y, z, a = "Orange", "Banana", "Cherry", "Akhilesh"
print(x)
print(y)
print(z)
print(a)


#And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)



                #Unpack a Collection

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

def sum():
  print(5 + 5)
sum()


def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)