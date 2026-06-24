#class
# class students:
#     pass
# st = students()
# print("object is created")


#constructer is special method that call itself when it is created.
# class students:
#     def __init__(self, name): #self is imp and permanent parameter.
#         self.name = name
#         self.age = 0
#         print("This is constructer")

#     def display(self):
#         print(self.name)

# st = students("JSPM")
# st.age = "101"
# print("object is created: ")
# print(st.name)
# print(type(st.age))
# st.display()


#Single Inheritance
# class Parent:
#     def display(self):
#         print("parent class")

# class Child(Parent):
#     pass

# obj = Child()
# obj.display()


#Multiple Inheritance
# class Father:
#     def display1(self):
#         print("father class")

# class Mother:
#     def display2(self):
#         print("mother class")

# class Child(Father, Mother):
#     pass

# obj = Child()
# obj.display1()
# obj.display2()


#Multilevel Inheritance
# class Grandparent:
#     def display1(self):
#         print("grandparent class")

# class Parent(Grandparent):
#     def display2(self):
#         print("parent class")

# class Child(Parent):
#     pass

# obj = Child()
# obj.display1()
# obj.display2()


#Hierarchical Inheritance
# class Parent:
#     def display1(self):
#         print("parent class")

# class Child1(Parent):
#     def display2(self):
#         print("child1 class")

# class Child2(Parent):
#     def display3(self):
#         print("child2 class")

# obj1 = Child1()#not display3 because it wont have connection with child2(who have display3) or call in parameter
# obj1.display1()
# obj1.display2()
# # obj1.display3()

# obj2 = Child2()#not display2 because it wont have connection with child1(who have display2) or call in parameter
# obj2.display1()
# # obj2.display2()
# obj2.display3()


#Hybrid Inheritance
# class A:
#     def func(self):
#         print("A")

# class B(A):
#     pass

# class C(A):
#     pass

# class D(B, C):
#     pass

# obj = D()
# obj.func()


#Method Overriding
# class Animal:
#     def sounds(self):
#         print("animal sounds")

# class Dog(Animal):
#     def sounds(self):
#         print("bark")

# class cat(Animal):
#     def sounds(self):
#         print("meow")

# a1 = Animal()
# a1.sounds()

# d1 = Dog()
# d1.sounds()

# c1 = cat()
# c1.sounds()


#Polymorphism: 1 function can do multiple forms
# class Dog:
#     def sounds(self):
#         print("bark")

# class cat:
#     def sounds(self):
#         print("meow")

# d1 = Dog()
# d1.sounds()

# c1 = cat()
# c1.sounds()

# animals = [Dog(), cat()]

# for animal in animals:
#     animal.sounds()


#Encapsulation
# class Student:
#     def __init__(self):
#         self.marks=101

#     def getMarks(self):
#         return self.marks
    
# s=Student()
# print(s.getMarks())


#Abstraction
# from abc import ABC, abstractmethod

# class Vehical(ABC):
#     @abstractmethod
#     def start(self):
#         pass
# #example
# class car(Vehical):
#     def start(self):
#         print("car started")

# c = car()
# c.start()