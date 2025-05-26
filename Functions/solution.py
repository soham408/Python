# 1. Basic Function Syntax Problem: Write a function to calculate and return the square of a number.

def square(number):
    return number ** 2

result = square(5)
print(result)

# 2. Function with Multiple Parameters Problem: Create a function that takes two numbers as parameters and returns their sum.

def add(num1, num2):
    return num1 + num2

print(add(3, 4))

# 3. Polymorphism in Functions Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

def multiply(p1, p2):
    return p1 * p2

print(multiply(3, 4))
print(multiply("Hello", 5))
print(multiply(5, 'a'))


# 4. Function Returning Multiple Values Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math
def circule_stats(radius):
    area = math.pi * radius ** 2
    circumferance = 2 * math.pi * radius
    return area, circumferance

a, c = circule_stats(3)

print("Area: ", round(a,2), "Cirumference: ", round(c,2))


# 5. Default Parameter Value Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.

def greet(name = "user"):
    return "Hello, " + name + " !"

print(greet("python"))
print(greet())


# 6. Lambda Function Problem: Create a lambda function to compute the cube of a number.

cube = lambda x: x ** 3

print(cube(10))

# 7. Function with *args Problem: Write a function that takes variable number of arguments and returns their sum.

# ' * ' allows you to get multiple arguments

def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5))
print(sum_all(1, 2, 3, 4, 5, 6, 7, 8))

# 8. Function with **kwargs Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="soham", surname="bambade")
print_kwargs(name="soham")
print_kwargs(name="soham", surname="bambade", language="python")

# 9. Generator Function with yield Problem: Write a generator function that yields even numbers up to a specified limit.

def even_generator(limit):
    for  i in range(2, limit + 1, 2):
        yield i

for num in even_generator(10):
    print(num)

# 10. Recursive Function Problem: Create a recursive function to calculate the factorial of a number.

def factorial(n):
    if n == 0:
        return 1 
    else:
        return n * factorial(n - 1)
