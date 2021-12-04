import string
import random

letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []

number_of_letters= int(input("How many letters would you like in your password? "))
number_of_symbols = int(input("How many symbols would you like? "))
number_of_numbers = int(input("How many numbers would you like? "))

for i in range(number_of_letters):
    password.append(random.choice(letters))
for i in range(number_of_symbols):
    password.append(random.choice(symbols))
for i in range(number_of_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)
print(f"Generated password: {''.join(password)}")
