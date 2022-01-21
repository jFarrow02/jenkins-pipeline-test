calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(num_days = 0, message = "No message"):
    return (f"There are {calculation_to_units * num_days} {name_of_unit} in {num_days} days.")


number_of_days = int(input("Input a number of days to find out how many hours there are:\n"))

units_calculation = days_to_units(number_of_days)

print(units_calculation)