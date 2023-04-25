# Task 1

import random

numbers_1_10 = list()
numbers_10_30 = list()

for i in range(5):
    numbers_1_10.append(random.randint(1, 10))

for i in range(10):
    numbers_10_30.append(random.randint(10, 30))

print(numbers_1_10, numbers_10_30)


# Task 2

num1 = input('First number: ')
num2 = input('Second number: ')

stroke = num1 + num2
figures = set()

for i in range(len(stroke)):
    figures.add(stroke[i])

print(figures)


# Task 3

numbers = set()

for i in range(50 + 1):
    if (i % 4 == 0) != (i % 3 == 0):
        numbers.add(i)

print(numbers)

# Task 4

numbers = set()

for i in range(1, 100, 4):
    numbers.add((i, i+2))

print(numbers)


# Task 5

# Task 6