## 1. Write a program that takes user input for daily temperatures for a week and returns average temperature.
temps = []

for i in range(1, 8):
    temp = int(input(f"Enter day {i} temperature: "))
    temps.append(temp)

avg_temp = sum(temps) / 7
print("Average temperature:", round(avg_temp, 2))


## Build a simple login system (username/password verification).
saved_username = "admin"
saved_password = "password123"

user = input("Username: ")
pwd = input("Password: ")

if user == saved_username and pwd == saved_password:
    print("Login successful!")
else:
    print("Invalid username or password.")


## 2. Create a basic ATM simulation (deposit, withdraw, balance check).
balance = 1000.0

while True:
    print("\n1. Check Balance | 2. Deposit | 3. Withdraw | 4. Exit")
    choice = input("Select an option (1-4): ")

    if choice == "1":
        print(f"Current Balance: ${balance}")
    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print(f"Deposited successfully. Balance: ${balance}")
    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrawn successfully. Balance: ${balance}")
        else:
            print("Insufficient funds.")
    elif choice == "4":
        print("Session ended.")
        break
    else:
        print("Invalid choice.")


## 3. Design a grade calculator for students based on marks and give grades A, B, C, F.
marks = float(input("Enter student marks (0-100): "))

if marks >= 85:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "F"

print(f"Assigned Grade: {grade}")


## 4. Create a program to manage a grocery list (add, remove, display items).
groceries = []

while True:
    print("\n1. Add | 2. Remove | 3. Display | 4. Exit")
    action = input("Select action: ")

    if action == "1":
        item = input("Enter item name: ")
        groceries.append(item)
        print(f"'{item}' added.")
    elif action == "2":
        item = input("Enter the item you want to remove: ")
        if item in groceries:
            groceries.remove(item)
            print(f"{item} removed.")
        else:
            print("Item not found.")
    elif action == 3:
        print("Current list of groceries: ", groceries)
    elif action == "4":
        break
    else:
        print("Invalid action.")
print()


## 5. Read a CSV file (simulated as a list of strings), extract and display only students who passed (marks >= 50).
csv_data = [
    "Ali,78",
    "Sara,45",
    "Zain,89",
    "Hamza,32",
    "Ahmad,50"
]

print("Students who passed (marks >= 50):")
for row in csv_data:
    name, score = row.split(",")
    if int(score) >= 50:
        print(f"- {name}: {score}")
    break


## 6. Write a bill calculator that takes item price, quantity and calculates total, tax, and final amount.
price = float(input("Enter item price: "))
quantity = float(input("Enter quantity: "))
tax = 5.0

total = price * quantity
tax_amount = total * (tax / 100)
final = total + tax_amount

print(f"\nTotal: ${round(final, 2)}")
print(f"Tax: ${round(tax_amount, 2)}")
print(f"Final: ${round(total, 2)}")


## 7. Create a BMI calculator that takes weight and height and tells category (underweight, healthy, overweight).
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = round(weight / (height ** 2), 2)

if bmi < 18.5:
    status = "underweight"
elif bmi <= 24.9:
    status = "healthy"
else:
    status = "overweight"

print(f"BMI: {bmi} ({status})")


## 8. Create a quiz app (MCQs) using dictionary, take answers from user and show score. Keys store the question and choices; values store the correct answer
quiz = {
    "What is the capital of Japan?\n(a) Osaka\n(b) Tokyo": "b",
    "Which data type is immutable in Python?\n(a) List\n(b) Tuple": "b",
    "What does CPU stand for?\n(a) Central Processing Unit\n(b) Core Power Unit": "a"
}

score = 0
for question, answer in quiz.items():
    print("\n" + question)
    user_choice = input("Your answer: ").strip().lower()
    if user_choice == answer:
        score += 1

print(f"\nFinal Score: {score} out of {len(quiz)}")


## 9. Make a program to track expenses: user enters daily expenses, at the end of the week it shows total and average.
daily_expenses = [float(input(f"Enter expense for day {i + 1}: ")) for i in range(7)]

total = sum(daily_expenses)
average = round(total / 7, 2)

print(f"\nTotal Weekly Expenses: ${total}")
print(f"Average Daily Expense: ${average}")

