marks =[78, 67, 29, 22, 30]
length = len(marks)
marks_sum = sum(marks)
marks_average= marks_sum/length
print("average is:", marks_average)


if marks_average >= 80:
  print("grade A")
elif marks_average >= 60:
  print("grade B")
elif marks_average >= 40:
  print("grade C")
elif marks_average >= 33:
    print("grade D")
else:
   print("grade f")

############################
############################

# function to find the average marks
def find_average_marks(marks):
  sum_of_marks = sum(marks)
  length_of_marks = len(marks)
  average_marks = sum_of_marks/length_of_marks
  return average_marks

 # calculate the grade and return it
def compute_grade(average_marks):
  if average_marks >= 80:
    grade = "A"
  elif average_marks >= 60:
      grade = "B"
  elif average_marks >= 40:
      grade = "C"
  else:
      grade = "F"
  return grade

marks = [87, 93, 39, 78, 89]
average_marks = find_average_marks(marks)
print("your average marks is:", average_marks)

grade = compute_grade(average_marks)
print("your grade is:", grade)

#########################
#########################
# LIST
# indexing  in the list
languages=["python", "java", "c++", "c"]
print(languages[1])

# negating indexing
print(languages[-1])

# slicing in the list
print(languages[0:3])

###########################
###########################
# list is mutable element which we can modify
languages=["python", "java", "c++", "c"]
languages[1]= "ruby"
print(languages)

languages[2:3]=["c#", "c"]
print(languages)

# in function in the list we can use this to check the item is in the list or not
languages=["python", "java", "c++", "c"]
print("python" in languages)
print("rust" in languages)

# for in the list function or iterting in the list
for language in languages:
  print(language)

 # list method
languages= ["python", "java", "c++", "c"]

languages.append("rust")
print(languages)

#using insert we can insert the element anywhere in the list with give it a index no.
languages.insert(2, "ruby")
#if we want remove anthing from the list
languages.remove("java")
print(languages)

######################
######################
# tuple is un mutable we can't modify them
numbers =(3, 536, 78, 88, -78)
print(numbers)
print(numbers[1])
print(numbers[2:4])

#####################
# defferance in the list[] and tuple()
languages= ('python', 'java', 'c++', 'c', 'riby' )
print(languages)

########################
mixed_list=["hello", "-34", "java", "true"]
print("1.", mixed_list[-1])

mixed_list[1]="hi"
print("2.", mixed_list)

mixed_tuple=(1,2,3,4)
mixed_tuple[1]==100
print("3.", mixed_tuple)

########################
#=======================
########################
# string
# string is unmutable
text = "he said whats there"
print(text)

text ="he said, \"what's there\""
print(text)

text = "python is fun"
print(text[0])

text ="python is fun"
print(text[0:6])

text ="PYTHON IS FUN"
print(text[-1])