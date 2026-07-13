my_list = [1,2,3,4]
print(my_list)
type(my_list)

#mised list
my_list =['a string',1,2.2,'3',True]
print(my_list)
####################
# a list of integer
numbers =[1, 2,3, 4.6]
print(numbers)

# mixed list
mixed_list = [1, "hello", 3.14, True]
print(mixed_list)

# empty list
list1 = []
print(list1)

# using len function in list
numbers =[1, 2,3, 4.6]
print(len(numbers))

mixed_list = [1, "hello", 3.14, True]
print(len(mixed_list))
################
my_list = [1,2,3,4]
#modify the list
my_list[0] = 10
print(my_list)
######################
loss_functions =['mean absolute error','mean squared error','huber loss','log loss']
print(loss_functions)
len(loss_functions)
##################
new_list = [1,2,3,4,5,6]
print(sum(new_list))
##################
second_list =[12,323,3.3,23213.2]
print(sum(second_list))
###################
marks = [87,76,95,68,80,83,92,74,79,89]
mean_marks = sum(marks)/len(marks)
print(mean_marks)