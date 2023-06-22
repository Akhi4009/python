#Arbitrary Arguments are often shortened to *args in Python documentations

def my_function(*kids):
  print("The youngest child is " + kids[1])

my_function("Emil", "Tobias", "Linus")

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# default parameter value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#return 

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


#lambda function

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))