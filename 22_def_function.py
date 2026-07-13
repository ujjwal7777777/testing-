def fun(fname):
    print(fname)
fun("ammy")
###############
#       greet function
#=========================
# using of greet
def greet():
  print("hello")
  print("how are you?")
greet()
greet()
greet()
# we can use greet for repetng any function.
###################
def greet(name):
  print("Hello!", name)
  print("How are you?")

greet("Jack")
######################
def student(name):
    print("Hello!",name)
student("Jhony")
student("Ammy")
student("Ujjwal")
#######################
def student(name,classes):
    print("Hello!",name +" " + classes)
student("Jhony","1")
student("Ammy","2")
student("Ujjwal","nur")
########################
def add_numbers(n1, n2):
  result = n1 + n2
  print("the sum is", result)

add_numbers(5, 10)
#########################
def add_numbers(n1= 100, n2=1000):
  sum = n1 + n2
  return sum
# here we add the def arguments value in the def function below
result = add_numbers(5.4)
print(result)

#=========================
#    arbitrary arguments
#=========================
def fun(*name):
    print(name)
fun("ammy","shukla")
fun("john","cena")
#########################
def fun(*name):
    print(name[0])
fun("ammy","shukla")
fun("john","cena")
#########################
def fun(*name):
    print(name[3])
fun("ammy","shukla","john","cena")

#==========================
#    keyords/key value type of arguments
#=========================
def fun(child3,child1,child2):
    print(child1,child2,child3)
fun(child1="john",child2="mark",child3="big")

#=========================
#    arbitrary keyword arguments
#=========================
#now u have to use of two '**'
def fun(**childs):
    print(childs)
fun(child1="john",child2="mark",child3="big")

#=========================
#    passing list as an arguments
#=========================
def fun(food):
    print(food)
fruits = ["apple","banana","cherry"]
fun(fruits)
##################
def fun(food):
    for x in food:
     print(x)
fruits = ["apple","banana","cherry"]
fun(fruits)

#========================
#     return
#========================
def add(a,b):
    return a+b
print(add(10,20))
####################
def add(a,b):
    return a+b
c = add(10,20)
print(c)

#======================
#     pass
#======================
#we can use pass for passing the funtion for future use
def fun():
    pass

#======================
#     lambda
#======================
x = lambda a : a + 10
print(x(5))
################
x = lambda a, b : a + b
print(x(10,5))
################
def add(x,y):
    return x + y
result = add(3,4)
print(result)

#lambda
add = lambda x,y : x + y
result = add(3,4)
print(result)
##############
divide = lambda x,y : "undefined" if y==0 else x / y
print(divide(10,2))
print(divide(10,0))

#===================
#      filter
#==================
numbers = [1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda x : x % 2 == 0, numbers))
print(even)

#====================
#     map
#====================
numbers = [1,2,3,4,5]
def fun(x):
    return x*x
sq_num = list(map(fun,numbers))
print(sq_num)
##################
#map(function,iterable)
numbers = [1,2,3,4,5,6,7,8,9,10]
squared = list(map(lambda x : x ** 2, numbers))
print(squared)
