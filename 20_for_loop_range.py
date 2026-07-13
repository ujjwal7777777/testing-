# using of "for"
text = "python"
'''for item in sequences
 statement(S)
 '''
for character in text:
   print(character)
################
toppings = ["pepperoni","mushrooms","olives","sausage"]
for topping in toppings:
  print(topping)
###################
new_toppings = ["bacon","peppers","pineapple"]
for topping in new_toppings:
  toppings.append(topping)
print(toppings)
###########################3
languages = ('english', 'hindi', 'punjabi')
for language in languages:
  print(language)

#===========================
#        range function
#===========================
for i in range(5):
  print(i)
#######################
#using range function with 'for'
for count in range(1,5):
  print(count)
##########################
for i in range(2,9,2):
    print(i)
###########################
# make a table using "for" loop
number =int(input("enter the number:"))
for count in range(1,11):
  product = number * count
  print(number, "x", count, "=", product)
########################
# create a program to find the sum of number between 1 to 100 ? result should be equal to result= 1+2+3+....+100
total_sum = 0
for count in range(1,101):
  total_sum = total_sum + count
print("the sum of number between 1 to 100 is:", total_sum)