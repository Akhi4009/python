#A tuple is a collection which is ordered and unchangeable.

thistuple = ("akhilesh","yadav","manirampur","dharaimafi","amethi")
print(thistuple)
print(len(thistuple))


#Create Tuple With One Item
tuple1 = ("apple",)
print(type(tuple1))
tuple2= ("apple")
print(type(tuple2))

# tuple contructor
thistuple1 = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple1)
y = ("orange",)
thistuple1 += y

print(thistuple1)

# unpacking tuple

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

fruits1 = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits1

print(green)
print(yellow)
print(red)

thistuple4 = ("apple", "banana", "cherry")
for i in range(len(thistuple4)):
  print(thistuple4[i])

print (thistuple4.count("banana"))
print (thistuple4.index("apple"))