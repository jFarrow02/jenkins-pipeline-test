calculation_to_units = 24
name_of_unit = "hours"


# Define functions using the "def" keyword. Indicate the beginning
# of the function body with a ":". All lines of the function body
# must be indented beneath the "def" line
# def days_to_units():
#     print(f"20 days are {20 * calculation_to_units} {name_of_unit}")

# Invoke the function
# days_to_units()

# Function parameters
def days_to_units(num_of_days = 0,  custom_message = "No message provided"): # You can supply default values for params in Python
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
    print(custom_message)

days_to_units(5, "Calculation complete")
days_to_units()

# Variable scopes:
# - Global scope: variable is available from within any scope
# - Local scope: variables created inside a function can be used only in that function

def scope_check():
    print(name_of_unit)
    # print(num_of_days) # This won't work because num_of_days is scoped to days_to_units
    num_of_days = 999 # This new num_of_days is locally scoped to scope_check
    print(num_of_days)


scope_check()