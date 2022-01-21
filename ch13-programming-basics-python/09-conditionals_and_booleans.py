calculation_to_units = 24
name_of_units = "hours"

def days_to_units(num_of_days = 0): # You can supply default values for params in Python
    # Return output if number of days is positive
    if(num_of_days > 0):
        return (f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}")
    elif(num_of_days == 0):
        return("There are 0 hours in 0 days, of course")
    else:
        return("Invalid input provided. You must provide a positive integer for number of days.")


def validate_and_execute(x):
    if(x.isdigit()):
        print(days_to_units(int(x)))
    else:
        print("You must enter a positive whole number. Exiting.")

x = input("Input a number of days for conversion to hours:\n")

validate_and_execute(x) 