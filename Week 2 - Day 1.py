## 1. Design a Library class with methods to add, remove and lend books.
class Library:
  def __init__(self):
    self.books = []

  def add_book(self, book_name):
    self.books.append(book_name)
    print(f"'{book_name}' added to the library.")

  def remove_book(self, book_name):
    if book_name in self.books:
      self.books.remove(book_name)
      print(f"'{book_name}' removed from the library.")
    else:
      print(f"'{book_name}' is not in the library.")

  def lend_book(self, book_name):
    if book_name in self.books:
      self.books.remove(book_name)
      print(f"'{book_name}' has been successfully lent out.")
    else:
      print(f"Sorry, '{book_name}' is currently unavailable.")

  def show_books(self):
    print("Available books:", self.books)


my_lib = Library()
my_lib.add_book("Diary of a Wimpy Kid")
my_lib.add_book("Inferno")
my_lib.show_books()

my_lib.lend_book("Inferno")
my_lib.show_books()


## 2. Create a ShoppingCart class where items can be added, removed, and total calculated.
class ShoppingCart:
  def __init__(self):
    self.items = {}

  def add_item(self, name, price):
    self.items[name] = price
    print(f"Added '{name}' (Rs.{price}) to the cart.")

  def remove_item(self, name):
    if name in self.items:
      del self.items[name]
      print(f"Removed '{name}' from the cart.")
    else:
      print(f"'{name}' not found in the cart.")

  def calculate_total(self):
    return sum(self.items.values())

cart = ShoppingCart()
cart.add_item("Sneakers", 150)
cart.add_item("Hoodie", 550)

print("Total:", round(cart.calculate_total(), 2))

cart.remove_item("Hoodie")
print("New Total:", round(cart.calculate_total(), 2))


## 3. Create a Vehicle superclass and child classes like Car, Bike, with specific methods.
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def start_engine(self):
    print(f"The {self.brand} {self.model}'s engine is running.")

class Car(Vehicle):

  def __init__(self, brand, model, doors):
    super().__init__(brand, model)
    self.doors = doors

  def open_trunk(self):
    print(f"The {self.doors}-door trunk is now open.")


class Bike(Vehicle):

  def __init__(self, brand, model, gear_count):
    super().__init__(brand, model)
    self.gear_count = gear_count

  def do_wheelie(self):
    print(f"The {self.brand} bike is popping a wheelie!")


my_car = Car("Toyota", "Corolla", 4)
my_car.start_engine()
my_car.open_trunk()

my_bike = Bike("BMW", "A5", 6)
my_bike.start_engine()
my_bike.do_wheelie()


## 4. Design an inventory management system class that stores products and their quantities.
class Inventory:

  def __init__(self):
    self.stock = {}

  def add_item(self, name, quantity):
    if name in self.stock:
      self.stock[name] += quantity
    else:
      self.stock[name] = quantity
    print(f"Added {quantity} of '{name}'. Total: {self.stock[name]}")

  def remove_item(self, name, quantity):
    if name in self.stock:
      if self.stock[name] >= quantity:
        self.stock[name] -= quantity
        print(f"Removed {quantity} of '{name}'. Remaining: {self.stock[name]}")
        if self.stock[name] == 0:
          del self.stock[name]
      else:
        print(f"Not enough stock for '{name}'!")
    else:
      print(f"'{name}' not found in inventory.")

  def show_inventory(self):
    print("\nCurrent Inventory:", self.stock)

store = Inventory()
store.add_item("Hoodies", 15)
store.add_item("Sneakers", 8)
store.add_item("Hoodies", 5)  # Updates existing count

store.show_inventory()

store.remove_item("Sneakers", 3)
store.show_inventory()


## 5. Build a HotelRoom class that can check-in and check-out guests with booking dates.
class HotelRoom:

  def __init__(self, room_number):
    self.room_number = room_number
    self.guest_name = None
    self.check_in_date = None
    self.check_out_date = None
    self.is_occupied = False

  def check_in(self, guest_name, check_in_date, check_out_date):
    if not self.is_occupied:
      self.guest_name = guest_name
      self.check_in_date = check_in_date
      self.check_out_date = check_out_date
      self.is_occupied = True
      print(
          f"Room {self.room_number} booked for {self.guest_name} from"
          f" {self.check_in_date} to {self.check_out_date}."
      )
    else:
      print(
          f"Room {self.room_number} is already occupied by"
          f" {self.guest_name}!"
      )

  def check_out(self):
    if self.is_occupied:
      print(f"Room {self.room_number} checked out for {self.guest_name}.")
      self.guest_name = None
      self.check_in_date = None
      self.check_out_date = None
      self.is_occupied = False
    else:
      print(f"Room {self.room_number} is already empty.")

  def show_status(self):
    if self.is_occupied:
      print(
          f"Room {self.room_number}: Occupied by {self.guest_name} | Dates:"
          f" {self.check_in_date} to {self.check_out_date}"
      )
    else:
      print(f"Room {self.room_number}: Available")

room = HotelRoom(302)
room.show_status()

room.check_in("Ali", "2026-10-10", "2026-10-15")
room.show_status()

room.check_out()
room.show_status()


##. 6. Create a WeatherApp class to store temperature data and calculate weekly average.
class WeatherApp:

  def __init__(self):
    self.temperatures = []

  def add_temperature(self, temp):
    self.temperatures.append(temp)
    print(f"Added temperature: {temp}°C")

  def calculate_weekly_average(self):
    if not self.temperatures:
      return 0
    return sum(self.temperatures) / len(self.temperatures)

weather = WeatherApp()

weekly_temps = [28.5, 30.0, 27.5, 29.0, 31.2, 26.8, 29.5]
for t in weekly_temps:
  weather.add_temperature(t)

avg = weather.calculate_weekly_average()
print("\nWeekly Average Temperature:", round(avg, 2), "°C")


##> 7. Design a simple OnlineCourse class for managing enrolled students, lessons, and attendance.
class OnlineCourse:

  def __init__(self, course_name):
    self.course_name = course_name
    self.students = []
    self.lessons = []
    self.attendance = {}  # Maps student name to a list of attended lessons

  def enroll_student(self, student_name):
    if student_name not in self.students:
      self.students.append(student_name)
      self.attendance[student_name] = []
      print(f"'{student_name}' enrolled in {self.course_name}.")
    else:
      print(f"'{student_name}' is already enrolled.")

  def add_lesson(self, lesson_title):
    self.lessons.append(lesson_title)
    print(f"Lesson '{lesson_title}' added to the course.")

  def mark_attendance(self, student_name, lesson_title):
    if student_name in self.students and lesson_title in self.lessons:
      if lesson_title not in self.attendance[student_name]:
        self.attendance[student_name].append(lesson_title)
        print(f"Attendance marked for '{student_name}' in '{lesson_title}'.")
      else:
        print(f"Attendance already marked for '{student_name}' in '{lesson_title}'.")
    else:
      print("Invalid student name or lesson title!")

  def show_summary(self):
    print(f"\n--- Course Summary: {self.course_name} ---")
    print("Students:", self.students)
    print("Lessons:", self.lessons)
    print("Attendance:", self.attendance)


# Quick test
course = OnlineCourse("AI & Machine Learning")
course.add_lesson("Intro to Python")
course.add_lesson("Python Basics")

course.enroll_student("Ali")
course.enroll_student("Sara")

course.mark_attendance("Ali", "Intro to Python")
course.show_summary()


## 8. Build a TicketBooking system (bus/movie) that books, cancels, and displays available seats.
class TicketBooking:

  def __init__(self, total_seats):
    # Track seat status using a dictionary (Seat Number: Status)
    self.seats = {i: "Available" for i in range(1, total_seats + 1)}

  def display_seats(self):
    print("\nCurrent Seat Status:")
    for seat, status in self.seats.items():
      print(f"Seat {seat}: {status}")

  def book_ticket(self, seat_number):
    if seat_number in self.seats:
      if self.seats[seat_number] == "Available":
        self.seats[seat_number] = "Booked"
        print(f"Success! Seat {seat_number} has been booked.")
      else:
        print(f"My bad, seat {seat_number} is already booked.")
    else:
      print("That seat doesn't exist!")

  def cancel_ticket(self, seat_number):
    if seat_number in self.seats:
      if self.seats[seat_number] == "Booked":
        self.seats[seat_number] = "Available"
        print(f"Booking for seat {seat_number} has been cancelled.")
      else:
        print(f"Seat {seat_number} is already available.")
    else:
      print("That seat doesn't exist!")

bus_booking = TicketBooking(5)
bus_booking.display_seats()

bus_booking.book_ticket(3)
bus_booking.book_ticket(3)

bus_booking.cancel_ticket(3)
bus_booking.display_seats()


## 9. Implement a RestaurantOrder system that stores table orders and calculates bill with tax.
class RestaurantOrder:
  def __init__(self, table_number):
    self.table_number = table_number
    self.order_items = {}

  def add_item(self, item_name, price):
    self.order_items[item_name] = price
    print(f"Added '{item_name}' (${price}) to Table {self.table_number}.")

  def calculate_bill(self, tax_percent=5.0):
    subtotal = sum(self.order_items.values())
    tax_amount = subtotal * (tax_percent / 100)
    final_amount = subtotal + tax_amount
    print(f"\n--- Bill for Table {self.table_number} ---")
    print(f"Subtotal: ${subtotal}")
    print(f"Tax ({tax_percent}%): ${tax_amount}")
    print(f"Final Total: ${final_amount}")
    return final_amount

order = RestaurantOrder(4)
order.add_item("Burger", 8.50)
order.add_item("Cold Drink", 2.00)

order.calculate_bill()


## 10. Make a SmartHomeDevice class that simulates turning lights/fans on/off based on input.
class SmartHomeDevice:
  def __init__(self, name, device_type):
    self.name = name
    self.device_type = device_type
    self.is_on = False

  def turn_on(self):
    self.is_on = True
    print(f"{self.name} ({self.device_type}) is now ON.")

  def turn_off(self):
    self.is_on = False
    print(f"{self.name} ({self.device_type}) is now OFF.")

  def show_status(self):
    state = "ON" if self.is_on else "OFF"
    print(f"{self.name} is currently {state}.")

room_light = SmartHomeDevice("Bedroom Light", "Light")
room_light.show_status()

room_light.turn_on()
room_light.show_status()

room_light.turn_off()

