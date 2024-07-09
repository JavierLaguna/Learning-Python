
### Lists ###

# definition
my_list = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
print(type(my_list))
print(my_list)

# list size
print(len(my_list))

my_list = ['red', False, 20, '1000', True]
print(my_list)

# access to data
print(my_list[3])
print(my_list[-2])
print(my_list[1:3])
print(my_list[2:])

# update elements
my_list = [1, 7, 3, 4, 5]
print(my_list)
my_list[1] = 2
print(my_list)

my_list = [1, 7, 8, 4, 5]
print(my_list)
my_list[1:3] = 2, 3
print(my_list)

# insert elements
my_list = [1, 3, 4, 5]
print(my_list)
my_list.insert(1, 2)
print(my_list)

# add elements
my_list.append(6)
print(my_list)

list_weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
print(list_weekdays)
list_weekend = ['Sat', 'Sun']
print(list_weekend)
list_weekdays.extend(list_weekend)
print(list_weekdays)

list_weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
tuple_weekend = ('Sat', 'Sun')
list_weekdays.extend(list_weekend)
print(list_weekdays)

# remove or delete
list_weekdays.remove('Sun')
print(list_weekdays)

list_weekdays.pop(5)
print(list_weekdays)

list_weekdays.pop()
print(list_weekdays)

del list_weekdays[3]
print(list_weekdays)

list_weekdays.clear()
print(list_weekdays)

del list_weekdays
#print(list_weekdays) ## NameError: name 'list_weekdays' is not defined. Did you mean: 'list_weekend'?

# sort items
my_list = ['Nieves', 'Carlos', 'Lydia', 'Sonia']
print(my_list)
my_list.sort()
print(my_list)

my_list = [2, 7, 1, 98, 12, 4]
print(my_list)
my_list.sort()
print(my_list)

my_list = [2, 7, 1, 98, 12, 4]
print(my_list)
my_list.sort(reverse = True)
print(my_list)

my_list = ['nieves', 'carlos', 'Lydia', 'Sonia']
print(my_list)
my_list.sort(key = str.lower)
print(my_list)

my_list = ['nieves', 'carlos', 'Lydia', 'Sonia']
print(my_list)
my_list.reverse()
print(my_list)

# copy the list 
my_list = [1, 2, 3, 4, 5]
list_copy = my_list.copy()
print(list_copy)

# count items
my_list = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'green', 'yellow']
count = my_list.count('green')
print(count)

# element index
index = my_list.index('blue')
print(index)

# operations
my_list = ['blue', 'red', 'yellow', 'green']
print(list(enumerate(my_list)))
