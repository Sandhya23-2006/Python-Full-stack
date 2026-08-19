# class student:
#     def display(self):
#         print("RadhaKrishna")
# s1=student()
# s1.display()


# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#           print("Name:",self.name)
#           print("Age:",self.age)
# s1=student("Krishna",20)
# s1.display()

# class employee:
#     def __init__(self,name,age,salary,department):
#         self.name=name
#         self.age=age
#         self.salary=salary
#         self.department=department
#     def display(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Salary:",self.salary)
#         print("Department:",self.department)
# e1=employee("Garuda",100,10000,"Manager1")
# e2=employee("Shesha",100,10000,"Manager2")
# e1.display()
# print()
# e2.display()


# class Animal:
#     def eat(self):
#         print("Animal eats")
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")
# d=Dog()
# d.eat()
# d.bark()


# ########################################################
# class grandfather:
#     def age(self):
#         print("grandfather age is 90")
# class father(grandfather):
#     def car(father):
#         print("Father has a car")
# class son(father):
#     def bike(son):
#         print("son has bike")
# s=son()
# s.age()
# s.car()
# s.bike()


# #############################################
# class father:
#     def father_property(self):
#         print("Father's property")
# class son(father):
#     def mother_property(self):
#         print("Mother's property")
# class daughter(father):
#     def son_property(self):
#         print("Son's property")
# s=son()
# s.father_property()
# s.mother_property()

# ################################################

# class car:
#     def move(self):
#         print("Car is moving")
# class boat:
#     def move(self):
#         print("Boat is sailing")
# class plane:
#     def move(self):
#         print("Plane is flying")
# vehicles=[car(),boat(),plane()]
# for vehicle in vehicles:
#     vehicle.move()

# ####################################

# from abc import ABC, abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass
# class Car(Vehicle):
#     def start(self):
#         print("Car starts with a key")
# class Bike(Vehicle):
#     def start(self):
#         print("Bike starts with a button")
# car=Car()
# bike=Bike()
# car.start()
# bike.start()
# ########################################################################
# from abc import ABC,abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def eat(self):
#         pass
# class Rabbit(Animal):
#     def eat(self):
#         print("Rabbit eats carrot")
# class Tiger(Animal):
#     def eat(self):
#         print("Tiger lives in forest")
# rabbit=Rabbit()
# tiger=Tiger()
# rabbit.eat()
# tiger.eat()



# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
# students=student("Krishna",100)
# print(students.name)
# print(students.marks)
# students.marks=98
# print(students.marks)

# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.__marks=marks
#     def get_marks(self):
#         return self.__marks
#     def set_marks(self,marks):
#         if marks>=0 and marks<=100:
#             self.__marks=marks
#         else:
#             print("Inavalid marks.")
# student=student("Balrama",85)
# print(student.get_marks())
# student.set_marks(80)


from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Private attribute

    @property
    def salary(self):
        """Getter method acting like an attribute"""
        return self.__salary

    @abstractmethod
    def calculate_salary(self):
        pass

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.calculate_salary())

class Developer(Employee):
    def calculate_salary(self):
        bonus = self.salary * 0.10
        return self.salary + bonus

class Manager(Employee):
    def calculate_salary(self):
        bonus = self.salary * 0.20
        return self.salary + bonus

# Creating objects
developer = Developer("Rahul", 30000)
manager = Manager("Priya", 50000)


developer.display()
print()
manager.display()


