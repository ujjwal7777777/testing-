# logical operators

# logical AND
print(True and True)
print(True and False)

# logical OR
print(True or False)

# logical NOT
print(not True)
###########
x = 5
y =10
z = 5
print((x < y) and (x == z))
print((x > y) or (x ==z))
print(not(x ==z))
################
# AND operator need both the exprasion True
age =22
gpa =3.4
print(age > 18 and gpa >3.2)

# OR operator needs only one be true for ex
exercise = 12
completed = 6
print(exercise > 10 or completed > 8 )

# NOT operator needs nothing true for ex
age = 23
print(not age < 25 )