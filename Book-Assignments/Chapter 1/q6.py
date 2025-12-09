my_list = [10,20,30]
print(id(my_list))

my_list.append(40)
print(id(my_list))

# observation:
# The Memory Address is the same before and after appeneding which proves that list in python are mutable objects.
# which means that we can modify the content of an object in-place without creating new objects
# the object keeps its original memory address unlike immutable objects like integers or strings

num = 5
print(id(num))

num = 20
print(id(num))
