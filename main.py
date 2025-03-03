# Operations on Sets
mySet = {1, 2, 3 ,3 ,3, 4, 4, 4, 5 ,5 ,5 ,5 }
print("Set :" , mySet)

mySet.add(6)
print("Set after adding 6 :" , mySet)

mySet.remove(3)
print("Set after removing 3 :" , mySet)

poppedElement = mySet.pop()
print("Popped Element :" , poppedElement)
print("Set after popping element :" , mySet)


tempSet = mySet.copy()
tempSet.clear()
print("Temporary Set after clearing :" , tempSet)