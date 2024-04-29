# import math
# import converters
# from converters import kg_to_lbs
# from utils import find_max
# from ecommerce.shipping import calc_shipping
import random
from pathlib import Path

# print("Enoch Kambale")
# print("0----")
# print(" ||||")
# print("*" * 10)

# price = 10
# price = 20
# rating = 4.9
# name = "Enoch"
# is_published = True
# print(price)

# patient_name = "John Smith"
# patient_age = 20
# is_new_patient = True

# name = input("What is your name? ")
# fav_color = input("What is your favorite color? ")
# print(name + " likes " + fav_color)

# birth_year = input('Birth year: ')
# print(type(birth_year))
# age = 2024 - int(birth_year)
# print(type(age))
# print(age)

# weight_in_pounds = input("Weight (lbs): ")
# weight_in_kg = float(weight_in_pounds) * 0.45
# print("You weigh " + str(weight_in_kg) + "kg")

# course = 'Python for Beginners'
# duplicate_course = course[:]
# item = "Enoch's computer"
# message = '''
# Hi Enoch,

# Welcome to Python.

# '''

# print(message)
# print(course[0])
# print(course[-1])
# print(course[-2])
# print(course[0:3])
# print(course[1:])
# print(course[:5])
# print(course[:])
# print(duplicate_course)

# name = 'Jennifer'
# print(name[1:-1])

# first = 'John'
# last = 'Smith'

# msg = f'{first} [{last}] is a coder'
# print(msg)

# course = 'Python for Beginners'
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.find('o'))
# print(course.replace('Beginners', 'Absolute Beginners'))

# print('Python' in course)

# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3)
# print(10 // 3)
# print(10 % 3)
# print(10 ** 3)

# x = 10
# x = x + 3
# x += 3
# x -= 3


# x = 10 + 3 * 2
# print(x)

# x = 2.9
# print(round(x))
# print(abs(-2.9))
# print(math.ceil(2.9))
# print(math.floor(2.9))


# is_hot = False
# is_cold = False

# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")

# print("Enjoy your day")

# price_of_house = 1000000
# good_credit = True

# if good_credit:
#     down_payment = 0.1 * price_of_house
# else:
#     down_payment = 0.2 * price_of_house

# print(f"The down payment is ${down_payment}")

# has_high_income = False
# has_good_credit = True
# has_criminal_record = False

# if has_high_income and has_good_credit:
#     print("Eligible for loan")

# if has_good_credit and not has_criminal_record:
#     print("Eligible for loan")

# temperature = 35

# if temperature == 30:
#     print("It's a hot day")
# else:
#     print("It's not a hot day")

# name = "J"

# if len(name) < 3:
#     print("Name must be at least 3 characters")
# elif len(name) > 50:
#     print("Name must be a maximum of 50 characters")
# else:
#     print("Name looks good")


# i = 1

# while i <= 5:
#     print('*' * i)
#     i = i + 1
# print("\nDone!")

# for item in 'Python':
#     print(item)

# for item in ['Enoch', 'Matt', 'Kelvin']:
#     print(item)

# for item in range(10):
#     print(item)

# for item in range(5, 10):
#     print(item)

# for item in range(5, 10, 2):
#     print(item)

# prices = [10, 20, 30]
# total_price = 0

# for price in prices:
#     total_price += price
# print("Total Price is", total_price)


# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')

# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += 'x'
#     print(output)

# numbers = [2, 2, 2, 2, 5]
# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += 'x'
#     print(output)

# names = ['John', 'Bob', 'Enoch', 'Sarah', 'Mary']
# print(names[:])

# numbers = [8, 20, 1, 5, 7]

# largest_number = numbers[0]

# for number in numbers:
#     if number > largest_number:
#         largest_number = number
# print('Largest Number is', largest_number)


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(matrix[0][1])

# for row in matrix:
#     for number in row:
#         print(number)


# numbers = [5, 7, 2, 1, 7, 5, 4]
# numbers.append(13)
# numbers.insert(0, 10)
# numbers.remove(5)
# numbers.pop()

# print(numbers.index(7))
# print(50 in numbers)
# print(numbers.count(7))
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)

# for number in numbers:
#     if numbers.count(number) > 1:
#         numbers.remove(number)
# print(numbers)

# numbers = (1, 2, 3, 4, 5)
# numbers[2] = 10
# print(numbers)

# coordinates = (1, 2, 3)

# x, y, z = coordinates
# print(x, y, z)

# customer = {
#     "name": "Enoch Kambale",
#     "age": 20,
#     "is_verified": True
# }

# print(customer["age"])
# print(customer.get("birthdate"))
# print(customer.get("birthdate", "Mar 31 2004"))

# numbers = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
#     "5": "Five",
#     "6": "Six",
#     "7": "Seven",
#     "8": "Eight",
#     "9": "Nine",
#     "0": "Zero"
# }

# output = ""

# phone = input("Phone: ")

# for digit in phone:
#     output += numbers.get(digit, "!") + " "

# print(output)


# def greet_user(first_name, last_name):
#     print(f"Hi there {first_name} {last_name}!")
#     print("Welcome aboard!")


# greet_user(last_name="Enoch", first_name="Kambale")

# def square(number):
#     return number * number

# print(square(4))

# try:
#     age = int(input("Age: "))
#     income = 20000
#     risk = income / age
#     print(age)
# except ZeroDivisionError:
#     print("Age cannot be 0")
# except ValueError:
#     print("Invalid value")


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def move(self):
#         print("move")

#     def draw(self):
#         print("draw")


# point1 = Point(10, 20)
# print(point1.x, point1.y)
# point1.draw()
# point1.move()

# point2 = Point(30, 40)
# print(point2.x, point2.y)


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def talk(self):
#         print(f"Hi, I am {self.name}")


# person1 = Person('Enoch')
# person1.talk()


# class Mammal:
#     def walk(self):
#         print("walk")


# class Dog(Mammal):
#     def bark(self):
#         print("bark")


# class Cat(Mammal):
#     def be_annoying(self):
#         print("annoyiiiiiiiiing")
#     pass


# dog1 = Dog()
# dog1.walk()

# cat1 = Cat()
# cat1.be_annoying()


# print(converters.kg_to_lbs(70))
# print(kg_to_lbs(70))

# numbers = [10, 3, 6, 2]
# maximum = find_max(numbers)
# print(f"Largest number is {maximum}")

# print(max(numbers))

# calc_shipping()

# for i in range(3):
#     print(random.random())
#     print(random.randint(10, 20))

# members = ['John', 'Mary', 'Bob', 'Enoch']
# leader = random.choice(members)

# print(leader)

# path = Path("emails")
# path.mkdir()
# path.rmdir()
# print(path.exists())

path = Path()
for file in path.glob('*'):
    print(file)
