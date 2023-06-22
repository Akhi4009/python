#A set is a collection which is unordered, unchangeable*, and unindexed.

set1 = {"akhilesh", "yadav", "manirampur", "dharaimafi", "amethi"}
print(set1) 

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)
print(len(set1))

thisset1 = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset1)

for x in thisset1 :
    print(x)

print("banana" in thisset1)    

thisset1.add("orange")
print(thisset1)

thisset2= {"a","b"}
thisset1.update(thisset2)
print(thisset1)
#Once a set is created, you cannot change its items, but you can add new items.


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)