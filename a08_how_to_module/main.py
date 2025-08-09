# import helper # gets all the functions, to use we have to do helper.validate_and_execute
# import helper as h , then use as h.validate_and_execute
# from helper import validate_and_execute # this will get specific function I want
from helper import validate_and_execute, user_input_message

user_input = '1:hours,1:minutes,1:seconds'
user_input = user_input.split(',')

def process_user_input():
    print(user_input_message)
    for element in user_input:
        convert_array = element.split(':')
        days_and_unit_dictionary = {
            'days': convert_array[0], 'unit': convert_array[1]
        }
        validate_and_execute(days_and_unit_dictionary)

process_user_input()