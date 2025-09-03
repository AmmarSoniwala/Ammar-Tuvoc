# class Parent:
#     def __init__(self, fname, mname, lname):
#         self.firstname = fname
#         self.middlename = mname
#         self.lastname = lname
#     def __str__(self):
#         return f"{self.firstname} {self.middlename} {self.lastname}"
# class Child(Parent):
#     def __init__(self, fname, parent):
#         super().__init__(fname, parent.firstname, parent.lastname)
#     def __str__(self):
#         return f"Child's name is: {self.firstname} {self.middlename} {self.lastname}"

# x = Parent("Vasim", "Iqbal", "Soniwala")
# y = Child("Ammar", x)
# print(y)

class Grandparent:
    def __init__(self, fname, mname, lname):
        self.firstname = fname
        self.middlename = mname
        self.lastname = lname
    def __str__(self):
        return f"{self.firstname} {self.middlename} {self.lastname}"
class Parent(Grandparent):
    def __init__(self, fname, gparent):
        self.firstname = fname
        self.middlename  = gparent.firstname
        self.lastname = gparent.lastname
    def __str__(self):
        return f"Child's name is: {self.firstname} {self.middlename} {self.lastname}"
class Child(Parent):
    def __init__(self, fname, parent):
        super().__init__(fname, parent)
    def __str__(self):
        return f"GrandChild's name is: {self.firstname} {self.middlename} {self.lastname}"

x = Grandparent("Vasim", "Iqbal", "Soniwala")
y = Parent("Ammar", x)
z= Child("Subham", y)
print(x)
print(y)
print(z)

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def __str__(self):
        return f"Vehicle Brand: {self.brand}, Model: {self.model}"
    def move(self):
        print("Car is Moving")
class Car(Vehicle):
    pass
class Boat(Vehicle):
    def move(self):
        print("Boat is Sailing")
class Plane(Vehicle):
    def move(self):
        print("Plane is Flying")
v1 = Car("Ford", "Mustang")
v2 = Boat("Yamaha", "Touring")
v3 = Plane("Boeing", "747")

for x in (v1, v2, v3):
    print(x)
    x.move()