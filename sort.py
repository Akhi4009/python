thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
thislist.sort(reverse = True)
print(thislist)


thislist1 = [100, 50, 65, 82, 23]
thislist1.sort(reverse=True)

def myFun(n):
   return abs(n-50)

thislist1.sort(key = myFun)

print(thislist1)

thislist2 = ["banana", "Orange", "Kiwi", "cherry"]
thislist2.sort(key = str.lower)
print(thislist2)

list1=thislist2.copy()
print(list1)

list2=list (thislist2)
print(list2)