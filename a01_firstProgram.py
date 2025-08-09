print(1)
print("Hello World")
print('Hey I am also a string')

# Integer
print(-1)
print(10)

# Float
print(3.14)

# Arithmetic Operators

# How many mins in 20 days
print(20 * 24 * 60)
print("20 days are " + str(20 * 24 * 60) + " minutes")
# only difference is add f at the start of string
# it will format it for me
print(f"20 days are {20 * 24 * 60} minutes")

# variables
cal_to_seconds = 24 * 60
name_of_unit = "minutes"

print(f"20 days are {20 * cal_to_seconds} {name_of_unit}")
print(f"30 days are {30 * cal_to_seconds} {name_of_unit}")
print(f"40 days are {40 * cal_to_seconds} {name_of_unit}")
print(f"100 days are {100 * cal_to_seconds} {name_of_unit}")


# Functions
def days_to_units():
    # this will not override the global variable
    # only changed in the function
    name_of_unit = "seconds"
    print(f"20 days are {20 * cal_to_seconds} {name_of_unit}")
    print("All good!")


days_to_units()


# Function with parameters
def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days * cal_to_seconds} {name_of_unit}")
    print("All good!")


days_to_units(20)
days_to_units(45)
days_to_units(0)


# User Input
# user_input = input("Give me numbers of days, and I will convert them to hours!\n")
# if user_input.isdigit():
#     days_to_units(int(user_input))

# Return value from function
def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * cal_to_seconds} {name_of_unit}"


number_of_days20_to_mins = days_to_units(-120)
print(number_of_days20_to_mins)


# Validate input
def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * cal_to_seconds} {name_of_unit}"
    else:
        return "number of days has to be greater than 0"


#     default is None if I don't return anything
number_of_days20_to_mins = days_to_units(-120)
print(number_of_days20_to_mins)

# Check the datatype of variable
num_of_days = 0
condition_check = num_of_days > 0
print(type(num_of_days))  # <class 'int'>
print(type(condition_check))  # <class 'bool'>
print(type('Hello World'))  # <class 'str'>
print(type("a"))  # <class 'str'>
print(type(11))  # <class 'int'>
print(type(11.1))  # <class 'float'>

# Exception Handling

num_of_days = 1
def validate(num_of_days):
    try:
        if num_of_days.isDigit() & num_of_days > 0:
            return days_to_units(num_of_days)
    except:
        print("Invalid input")
        return None


validate(num_of_days)

# is_of_voting_age
def is_of_voting_age(age):
    if age < 0:
        print(f"{age} must be greater than 0")
    # elif age > 0 and age <= 18:
    elif age < 18:
        print(f"{age} age must be greater than 18")
    else:
        print(f"{age} Eligible to Vote")

is_of_voting_age(-1)
is_of_voting_age(1)
is_of_voting_age(18)

# is_number_even_odd
def is_number_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is even number")
    else:
        print(f"{num} is odd number")

is_number_even_odd(1)
is_number_even_odd(2)


