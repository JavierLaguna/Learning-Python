my_tuple = ('one', 'two', 'three')
my_tuple2 = (1, 'two', True)
my_tuple3 = (False, )
my_tuple4 = (False) ## Error

print(type(my_tuple))

print(my_tuple[2])
print(my_tuple[0:2])
print(my_tuple2[-1])

print(len(my_tuple3))
# print(len(my_tuple4)) ## TypeError: object of type 'bool' has no len()

for x in my_tuple:
    print(x)

print(my_tuple + my_tuple2)

print(my_tuple * 2)

count = my_tuple.count('one')
print(count)

index = my_tuple.index('two')
print(index)