# without comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# with comprehension

newlist = [x for x in fruits if "a" in x]
newlist1=[y for y in fruits if "b" in y]

print (newlist)
print (newlist1)
newlist2 = [x for x in range(10)]
print (newlist2)
newlist3= [x for x in range(10) if x < 5]
print (newlist3)
newlist4 = [x.upper() for x in fruits]
print (newlist4)