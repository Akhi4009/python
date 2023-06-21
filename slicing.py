s="akhilesh"
print(s[2:5])
print(s[:5])
print(s[2:])
print(s[-5:-1])
print(s.upper())
name="AKHILESH yadav"
print(name.lower())

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

name1="  Akhilesh  "

print(name1.strip())

print(name.replace("A","Z"))

print(name.split(" "))

# string concatination
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#format method

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))