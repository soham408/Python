# 1. Counting Positive Numbers

# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

# positive_num_count = 0
# negative_num_count = 0
# for num in numbers:
#     if num > 0:
#         positive_num_count += 1
#     elif num < 0:
#         negative_num_count += 1
# print("final count of positive number: ", positive_num_count)
# print("final count of negative number: ", negative_num_count)


# 2. Sum of Even Numbers Problem: Calculate the sum of even numbers up to a given number n.

# n = 20

# sum_of_even_numbers = 0
# sum_of_odd_numbers = 0

# for i in range(1, n+1):
#     if i % 2 == 0:
#         sum_of_even_numbers += 1
#     else:
#         sum_of_odd_numbers += 1
# print("sum of even numbers is: ", sum_of_even_numbers)
# print("sum of add numbers is: ", sum_of_odd_numbers)
# print(i)


# 3. Multiplication Table Printer Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

# number = 3

# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(number, 'x', i, '=', number * i)


# 4. Reverse a String Problem: Reverse a string using a loop.

# input_string = "soham"
# reversed_str = ""

# for char in input_string:
#     reversed_str = char + reversed_str

# print(reversed_str)

# 5. Find the First Non-Repeated Character Problem: Given a string, find the first non-repeated character.

# input_str = "aaaabbbbbbbcdddde"

# for char in input_str:
#     if input_str.count(char) == 1:
#         print("char is: ", char)
#         break


# 6. Factorial Calculator Problem: Compute the factorial of a number using a while loop.

