#class object
class Myclass:
    x = 5
obj = Myclass()
print(obj.x)

#===================
#      class comstructor
#===================
#class is blueprint and object is parts of class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

person1 = Person("John", 36)

print(person1.name)
print(person1.age)
###################
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
p2 = Person("Jack", 25)
print(p1.name,p1.age)
print(p2.name,p2.age) 

#================
#       method
#================
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
        print("hello",self.name)

person = Person("John", 36)
person2 = Person("Jack", 25)
person.greet()
person2.greet()