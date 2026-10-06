# list -->[]
# tuple -->()
# set -->{}
# Set: unique items collection.No duplicate
numbers=[7, 10, 35, 50 ,97, 50, 36, 49, 7, 100]
print(numbers)
numbers_set =set(numbers)
print(numbers_set)
numbers_set.add(55)
numbers_set.add(500)
print(numbers_set)
numbers_set.remove(7)
print(numbers_set)


A={1,2,3,9,5}
B={1,4,2,3,6,7,8,10}

print(A&B)
print(A|B)