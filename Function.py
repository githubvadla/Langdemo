calculation_to_sec = 24
number_of_unit = "hours"

def days_to_units(number_of_days):
    conditional_check= number_of_days > 0
    print(type(conditional_check))
    if number_of_days > 0:
        return f"{number_of_days} days are {number_of_days * calculation_to_sec} {number_of_unit}"
    elif number_of_days == 0:
        return "you entered 0"
    else:
        return "you entered wrong value, so no conversion possible"


user_input = input("hey user, enter a number of days \n")
if user_input.isdigit():
    calculated_value = days_to_units(int(user_input))
    print(calculated_value)
else:
    print("You have entered non-digit, Please check ")
