#tuple()
#tuple is imutable mean we can't modify the tuple
my_tuple =(1,2,3,4,5)
print(my_tuple)
print(type(my_tuple))
###############
#can also mix object types
another_tuple = ('one',2,3.3,'abc')
print(another_tuple)
##################
my_tuple = (1,2,3)
my_tuple_list = list(my_tuple)
my_tuple_list[0] = 'change'
my_tuple = tuple(my_tuple_list)
print(my_tuple)