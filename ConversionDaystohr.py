calculation_to_sec = 24
number_of_unit = "hours"


def days_to_units(number_of_days):
    return f"{number_of_days} days are {number_of_days * calculation_to_sec} {number_of_unit}"


def validate_execute():
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number >0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a 0, please enter a valid positive number")
        else:
            print("you entered negative number")
    except ValueError:
        print("your input is not a valid, dont ruin my program")


user_input = ""
while user_input != "exist":
    user_input = input("Hey user, enter a number of days and conversion unit \n")
    print(user_input)
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": "hours"}
    print(days_and_unit_dictionary)
    validate_execute()


