# Lists are 0-indexed
my_list = [2, 4, 6, 8]
print(my_list[0]) # 2
my_list.append("foo")
print(my_list[4]) # foo

conversion_units = "minutes"
conversion_calculation = 24 * 60 * 60

def calculate_units_in_days(num_of_days):
    if num_of_days >= 0:
        return (f"There are {num_of_days * conversion_calculation} {conversion_units} in {num_of_days} days")
    else:
        return ("You entered a negative number. Please enter a positive whole number.")

def multi_args(*args):
    for arg in args:
        print(arg)

# args = input("Enter some arguments:\n")
# multi_args(args)

def validate_and_run():
    user_input = ""
    while user_input != "exit":
        user_input = input("Please enter the number of days you wish to convert. Enter \"exit\" to exit:\n")
        if user_input == "exit":
            print("Exiting the application...")
            break
        days_list = user_input.split(",")
        for day in days_list:
            if day.isdigit():
                result = calculate_units_in_days(int(day))
                print(result)
            else:
                print("Bad input!")

validate_and_run()

