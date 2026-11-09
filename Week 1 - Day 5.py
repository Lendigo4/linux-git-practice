## 1 & 2: Create a student class with attributes name and roll number. Add a method to display student details.
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}")

student_1 = Student("Fahaam Ali", "B-28993")
student_1.display()


## 3. Create a Circle class with method to calculate area and circumference.
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

c = Circle(5)
print("Area: ", round(c.area(), 2))
print("Circumference: ", round(c.circumference(), 2))


## 4. Demonstrate constructor and use __str__() method.
class Book:

  def __init__(self, title, author):
    self.title = title
    self.author = author

  def __str__(self):
    return f"'{self.title}' by {self.author}"


b = Book("Japanese for Beginners", "Fahaam Ali")
print(b)


## 5. Create a class with private attributes and use getter/setter.
class Account:
  def __init__(self, pin):
    self.__pin = pin  # Private attribute

  def get_pin(self):
    return self.__pin

  def set_pin(self, new_pin):
    self.__pin = new_pin


acc = Account(1234)
print("Current PIN:", acc.get_pin())
acc.set_pin(5678)
print("Updated PIN:", acc.get_pin())


## 6. Implement single inheritance between Person and Employee.
class Person:
  def __init__(self, name):
    self.name = name

class Employee(Person):
  def __init__(self, name, emp_id):
    super().__init__(name)
    self.emp_id = emp_id

  def show(self):
    print(f"Employee: {self.name}, ID: {self.emp_id}")

e = Employee("Fahaam Ali", "B-28993")
e.show()


## 7. Demonstrate method overriding
class Animal:
  def make_sound(self):
    print("Some random sound")

class Cat(Animal):
  def make_sound(self):  # Overrides parent method
    print("Meow")

c = Cat()
c.make_sound()


## 8. Counting number of objects using a class variable.
class User:
  count = 0  # Class variable

  def __init__(self):
    User.count += 1

u1 = User()
u2 = User()
u3 = User()
print("Total objects created:", User.count)


## 9. Create a BackAccount class (basic version).
class BankAccount:
  def __init__(self, balance=0):
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount
    print(f"Deposited: ${amount}. New Balance: ${self.balance}")

  def withdraw(self, amount):
    if amount <= self.balance:
      self.balance -= amount
      print(f"Withdrawn: ${amount}. New Balance: ${self.balance}")
    else:
      print("Insufficient funds!")


acc = BankAccount(500)
acc.deposit(200)
acc.withdraw(100)


## 10. Create a class Rectangle, check if it's a square or not.
class Rectangle:

  def __init__(self, length, width):
    self.length = length
    self.width = width

  def is_square(self):
    return self.length == self.width

r1 = Rectangle(5, 5)
print("Is R1 a square?", r1.is_square())

r2 = Rectangle(4, 7)
print("Is r2 a square?", r2.is_square())
