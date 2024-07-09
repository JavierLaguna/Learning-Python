
### Tuples ###

# definition
my_tuple = ('one', 'two', 'three')
my_tuple2 = (1, 'two', True)
my_tuple3 = (False, )
my_tuple4 = (False) ## Error

print(type(my_tuple))

# access to data
print(my_tuple[2])
print(my_tuple[0:2])
print(my_tuple2[-1])

# tuple size
print(len(my_tuple3))
# print(len(my_tuple4)) ## TypeError: object of type 'bool' has no len()

# iterate over
for x in my_tuple:
    print(x)

# operate with tuples
print(my_tuple + my_tuple2)
print(my_tuple * 2)

# count items
count = my_tuple.count('one')
print(count)

# element index
index = my_tuple.index('two')
print(index)

# operations
my_tuple = ('one', 'two', 'three', 'four')
print(list(enumerate(my_tuple)))