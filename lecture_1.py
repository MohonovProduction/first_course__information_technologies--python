# no more 10 elements, no bigger then 4096

# Task 1

second_degrees = list()
for i in range(1, 20):
    second_degrees.append(2 ** i)

print(second_degrees)


# Task 2

div_5 = list()
for i in range(1, 10):
    number = 5 * i + 3
    div_5.append(number)

print(div_5)
div_5.reverse()
print(div_5)


# Task 3

import random

random_numbers = list()

for i in range(1, 11):
    random_numbers.append(random.randint(0, 4096))

def odd(a):
    if a == 0: return False
    else: return a % 2 == 0

def even(a):
    return not odd(a)

odd_numbers = list(filter(odd, random_numbers))
even_numbers = list(filter(even, random_numbers))

odd_numbers.sort()
even_numbers.sort(reverse=True)

print(odd_numbers + even_numbers)


# Task 4

import random

random_numbers = list()

for i in range(1, 11):
    random_numbers.append(random.randint(0, 4096))

for i in range(0, len(random_numbers) * 2 - 2, 2):
    el1 = random_numbers[i]
    el2 = random_numbers[i+1]
    sum = el1 + el2
    random_numbers.insert(i+1, sum)

print(random_numbers)


# Task 5 (Homework)
# 1

import random

matrix = list()

for i in range(10):
    matrix.append(list())
    for j in range(10):
        matrix[i].append(random.randint(0, 4096))

def remove_col_row(row, col, matrix):
    matrix.pop(row)
    for i in range(len(matrix)):
        matrix[i].pop(col)
    return matrix

row = int(input('Enter number of row: '))
col = int(input('Enter number of col: '))

print(*remove_col_row(row, col, matrix), sep='\n')

# 2
