thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

list4 = ["abc", 34, True, 40, "male"]

print(type(list4))

#list contructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

  thislist[1] = "blackcurrant"
print(thislist)
thislist1 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist1[1:3] = ["blackcurrant", "watermelon"]
print(thislist1)