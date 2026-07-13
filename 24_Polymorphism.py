class Animal:
  def make_sound(self):
    print("unkown sound")
class Dog(Animal):
  def make_sound(self):
    print("Bark")
class Cat(Animal):
    def make_sound(self):
     print("Meow")
dog = Dog()
cat = Cat()
goat = Animal()
dog.make_sound()
cat.make_sound()
goat.make_sound()
######################
class shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Square(shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side * self.side
class Rectangle(shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
class Circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

square = Square(5)
rectangle = Rectangle(3,4)
circle = Circle(2)
print("Area of square :", square.area())
print("Area of rectangle :", rectangle.area())
print("Area of circle :", circle.area())
########################
class Vechile:
    def __init__(self,name,max_speed):
        self.name = name
        self.max_speed = max_speed
    def move(self):
        print("Move")
class Car(Vechile):
    def move(self):
        print("Drive")
class Boat(Vechile):
    def move(self):
        print("Sail")
class Plane(Vechile):
    def move(self):
        print("Fly")
car = Car("Car", 200)
boat = Boat("Boat", 100)
plane = Plane("Plane", 500)
for x in (car, boat, plane):
    print(x.name, x.max_speed)
    x.move()
#============================
#     inheritance and supar
#============================
class Vechile:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def start_engine(self):
            print("starting engine")
class Car(Vechile):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors
    def drive(self):
            print("driving the car")
vechile = Vechile("Toyota", "Camry", 2022)
car = Car("Toyota", "Camry", 2022, 4)
vechile.start_engine()
car.start_engine()
car.drive()