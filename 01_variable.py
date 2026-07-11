# vaiable = city = 'shamli' which is literal
city = "shamli"
print(city)
x=10 #number
x="hello" #string
print(x)
# input function to write anything on the output
name = input("enter name:", )
print(name)
#type function to check the type of variable
name =input("enter name:")
print(type(name)) 
''' type basically tells us the data type which shown in the output like 
below down its shown us <class 'str' in the output'''
number =input("enter number:")
print(type(number))
##########
number =int(input("enter number:"))
print(type(number))
number =float(input("enter number:"))
print(type(number))
########
name =input("enter your name: ")
print("your name is" , (name))
#==========================
name =input("enter your name: ")
age =int(input("enter your age: "))
print("your name is" , (name), )
print("your age is" , (age))
#####################
# adding string + integer using explict conversion ( num_string =
# int(num_string)for ex,
num_string = '10'
num_integer = 20
print("data type of num_string before type casting:", type(num_string ))
# explict type conversion
num_string = int(num_string)
print("data type of num_string after type casting:", type(num_string))
num_sum = num_string + num_integer
print("sum of num_string and num_integer:", num_sum)
print("data type of num_sum:", type(num_sum))