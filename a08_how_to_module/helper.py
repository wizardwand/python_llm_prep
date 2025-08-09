from a07_dictionary_map_in_java import user_input


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

user_input_message = "Please enter a valid number"