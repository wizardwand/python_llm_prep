# Loops

# While loop

# infinite
# while True:

i = 0
while i < 10:
    print(i)
    i = i + 1

print("#########################")

# Q print n * n star
# ****
# ****
# ****
# ****

def print_n_by_n(n):
    output = ""
    for i in range(n):
        for j in range(n):
            output +="*"
        output +="\n"
    return output

print(print_n_by_n(4))

# print following
# *
# * *
# * * *
# * * * *

def print_lower_triangle(n):
    output = ""
    for i in range(1,n+1):
        for j in range(i):
            output += "*"
        output += "\n"
    return output
print(print_lower_triangle(4))

# print following
# 1
# 12
# 123
# 1234
# 12345
def print_lower_triangle_with_number(n):
    output = ""
    for i in range(1,n+2):
        for j in range(1,i):
            output += str(j)
        output += "\n"
    return output
print(print_lower_triangle_with_number(5))

# print following
# 1
# 22
# 333
# 4444
# 55555
def print_lower_triangle_with_row_number(n):
    output = ""
    for i in range(1,n+1):
        for j in range(1,i+1):
            output += str(i)
        output += "\n"
    return output

print(print_lower_triangle_with_row_number(5))

# print following
# 12345
# 1234
# 123
# 12
# 1
def print_upper_triangle_with_number(n):
    output = ""
    for i in range(1,n+1):
        for j in range(1,(n+2)-i):
            output += str(j)
        output += "\n"
    return output
print(print_upper_triangle_with_number(5))

# print following
# *****
# ****
# ***
# **
# *
def print_upper_triangle_with_stars(n):
    output = ""
    for i in range(1,n+1):
        for j in range(1,(n+2)-i):
            output += "*"
        output += "\n"
    return output
print(print_upper_triangle_with_stars(5))

# print following
# ....*
# ...**
# ..***
# .****
# *****
def print_upper_triangle_with_space_lower_triangle_with_stars(n):
    output = ""
    for i in range(1,n+1):
        for j in range(1,(n+1)-i):
            output += "."
        for j in range((n+1)-i,(n+1)):
            output += "*"
        output += "\n"
    return output
print(print_upper_triangle_with_space_lower_triangle_with_stars(5))


# Q Write a function to count the number of digits in an integer
def count_number_of_digits_in_a_number(n:int) -> str:
    ogn = n
    count = 0
    while n > 0:
        count += 1
        n = int(n/10)
    return f"{ogn} has {count} digits"

print(count_number_of_digits_in_a_number(123))
print(count_number_of_digits_in_a_number(100))
print(count_number_of_digits_in_a_number(77))

# Q Write a function to check if a number is a palindrome
def number_is_palindrome(n):
    ogn = n
    reverse_n = 0
    while n > 0:
        rem = n % 10
        reverse_n = reverse_n * 10 + rem
        # n = int(n/10)
        n  = n // 10
    return reverse_n == ogn

print(number_is_palindrome(123))
print(number_is_palindrome(101))
print(number_is_palindrome(1221))