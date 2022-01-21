conversion_units = "minutes"
conversion_calculation = 24 * 60 * 60

def calculate_units_in_days(num_of_days):
    if num_of_days >= 0:
        return (f"There are {num_of_days * conversion_calculation} {conversion_units} in {num_of_days} days")
    else:
        return ("You entered a negative number. Please enter a positive whole number.")

def validate_and_run():
    user_input = ""
    while user_input != "exit":
        user_input = input("Please enter the number of days you wish to convert. Enter \"exit\" to exit:\n")
        if user_input == "exit":
            print("Exiting the application...")
            break
        try:
            result = calculate_units_in_days(int(user_input))
            print(result)
        except:
            print("Bad user input.")


validate_and_run()

