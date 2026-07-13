age = 17
if age >= 18:
  print("you are eligible ")
else:
  print("you are not eligible")
######################
age = int(input("enter your age:"))
if age >= 18:
  print("you are eligible to vote")
#####################
a = 10;
b =10;
if a > b:
  print("a is greater than b")
elif a == b:
  print("a is equal to b")
else:
  print("a is less than b")
######################
# suppose u r an student and u need 50 or >50 marks to pass the exam so if ur marks is more than
#50 u passed the exam so here we can make the program to to identify that u r passed in the exam or not?
# using 'if' syntax
score = int(input("enter your score: " ))

if score >= 50:
   print("you passed the exam")
   print("congratulation")
if not score >= 50:
   print("you failed the exam")

#=========================
#   if else syntax
#=========================
score = 90
if  score >=50:
  print("you have passed the exam " + "(congratulations)")
else:
  print("sorry you failed the exam")

#==========================
# if else elif syntax
#=========================
# if, elif and else statement
score = int(input("enter your score:"))
if score > 100 or score < 0:
   print("score is invalid")
elif score >= 50:
   print("you have passed the exam")
   print("congratulation")
else:
  print("sorry you failed the exam")
#####################
number = float(input("enter the number:"))
if number > 0:
  print("the number is postive")
elif number < 0:
  print("the number is negative")
else:
    print("the number is zero")