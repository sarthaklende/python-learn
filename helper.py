def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "not valid unit"


def validate_and_execute(days_and_unit_dictionary):
    try:

        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print ("Sorry, you have entered a 0, so no conversion can be made. Please choose a positive number.")
        else:
            print ("Sorry, you have entered negative, so no conversion can be made. Please choose a positive number.")
    except ValueError:
        print("Sorry, your input is not a valid number so no conversion can be made")

user_input_message = "Hey user, enter number of days and conversion unit!\n"