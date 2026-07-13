empty_set =set()
print(type(empty_set))
##############
non_empty_set = {1,6,4,'abcc'}
#mutability in set
non_empty_set = non_empty_set | {1,7}
print(non_empty_set)
print(type(non_empty_set))
#len(non_empty_set)
################
my_set ={1,1,2,2,3,33,4}
print(my_set)
#cast as set to get unique values/ do not repeat the same values
#we cannot use list in the set becoz its muatable
#we can add tuple in the set becoz its immutable