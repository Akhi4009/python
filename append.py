thislist = ["apple", "banana", "cherry"]
thislist.append("orange")


thislist1 = ["apple", "banana", "cherry"]
thislist1.insert(1, "orange")
print(thislist1)


thislist2 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist2.extend(tropical)
print(thislist2)

thislist.remove("banana")

thislist.pop(1)
thislist.clear()
del(thislist)
print(thislist)