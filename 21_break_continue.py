# using of break to breakdown the loop where we wanted
for item in range(1, 10):
   if item == 6:
     break
   print(item)
print("the end")
###################
for i in range(2,10):
    if i % 2 != 0:
      continue
    print(i)
###################
while True:
  number =float(input("enter a number"))
  if number < 0:
    break
    print(number)
##################
for i in range(5):
     number = float(input("enter a number:"))
     print(number)
##################
for i in range(5):
  number = float(input("enter a number:"))
  if number < 0:
    continue
    print(number)
###############
# make a dictonary using my_dict={'name':thor,}
my_dict ={'name':'thor','age':13,'power':'hammer','weapon':'hammer'}
print(my_dict)