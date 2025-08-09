# import datetime

from datetime import datetime

# user_input = input("Please Entry your goal with a deadline separated by colon\n")
# learn python:10.11.2025
user_input = 'learn python:10.9.2025'
input_list = user_input.split(':')
print(input_list)

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, '%d.%m.%Y')
print(deadline_date)       # 2025-01-10 00:11:00
print(type(deadline_date)) # <class 'datetime.datetime'>


# calculate how many days from now till deadline
today = datetime.today()
print(today)
time_remaining_for_goal = deadline_date - today
# print(f'User Time to learn for your {goal} is {time_remaining_for_goal}')
# User Time to learn for your learn python is 32 days, 16:59:18.226043
print(f'User Time to learn for your {goal} is {time_remaining_for_goal.days} days') # 32 days
print(f'User Time to learn for your {goal} is {time_remaining_for_goal.seconds / 60 / 60} hours') # 16.961666666666666
print(f'User Time to learn for your {goal} is {time_remaining_for_goal.seconds // 60 // 60} hours') # 16 hours

