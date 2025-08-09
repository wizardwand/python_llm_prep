# days:units -> convert
# 20:hours,45:mins

user_input = '1:hours,1:minutes,1:seconds'
user_input = user_input.split(',')


def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return num_of_days * 24
    elif conversion_unit == "minutes":
        return num_of_days * 24 * 60
    elif conversion_unit == "seconds":
        return num_of_days * 24 * 60 * 60
    else:
        return 0

def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input_number = int(days_and_unit_dictionary['days'])
        if user_input_number > 0 :
            conversion_unit = days_and_unit_dictionary['unit']
            calculated_value = days_to_units(user_input_number, conversion_unit)
            print(f'{user_input_number} days are {calculated_value} {conversion_unit}')
        elif user_input_number == 0:
            print("You entered 0, didn't enter a valid number")
        else:
            print("You entered {user_input_number}, which is negative number")
    except ValueError:
        print("Invalid input")

def process_user_input():
    for element in user_input:
        convert_array = element.split(':')
        days_and_unit_dictionary = {
            'days': convert_array[0], 'unit': convert_array[1]
        }
        print(type(days_and_unit_dictionary))
        validate_and_execute(days_and_unit_dictionary)

process_user_input()