## Input 2 numbers and print their sum:
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Sum:", num1 + num2)


## Check if a number is even or odd:
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")


## Print multiplication table of a number:
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


## Check whether a string is a palindrome:
text = input("Enter a word: ").strip().lower()

if text == text[::-1]:
    print("It's a palindrome")
else:
    print("Not a palindrome")


## Count vowels and consonants in a string:
text = input("Enter a string: ").lower()

vowels = 0
consonants = 0

for char in text:
    if char.isalpha():
        if char in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)


## Find the largest number in a list:
numbers = [14, 67, 23, 89, 5, 42]

largest = max(numbers)
print("Largest number:", largest)


## Convert Celsius to Fahrenheit:
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C = {fahrenheit}°F")


## Function to return factorial of a number:
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter a positive integer: "))
print(f"Factorial of {num}:", factorial(num))


## Program to reverse a given string:
items = [10, 20, 30, 40, 50]

reversed_items = items[::-1]
print("Reversed list:", reversed_items)


## Find whether a number is prime or not:
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not prime")
            break
    else:
        print(f"{num} is prime")
else:
    print(f"{num} is not prime")

