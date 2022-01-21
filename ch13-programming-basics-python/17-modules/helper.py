prompt = "Hello! Enter number of days and conversion units, separated by \":\"\n"
separator = ":"
helper_variable = "HELPER VARIABLE"

def parse_input(input):
    split_input = input.split(separator) # OK
    return { "number_of_days": split_input[0], "conversion_units": split_input[1]}

def calculate_units_in_days(num_days, conversion_units):
    if conversion_units == "minutes":
        return num_days * 24 * 60
    elif conversion_units == "hours":
        return num_days * 24
    elif conversion_units == "seconds":
        return num_days * 24 * 60 * 60
    elif conversion_units == "milliseconds":
        return num_days * 24 * 60 * 60 * 1000
    else:
        return "unknown units given"

def validate_and_execute():
    i = input(prompt)

    while i != "exit":
        try:
            if i.find(separator) == -1:
                print("Input must be separated by \":\"")
                i = input(prompt)
            else:
                parameter_pair = i.split(separator)
                if len(parameter_pair) > 2:
                    print("Please provide exactly two parameters")
                    i = input(prompt)
                else:
                    num_days = int(parameter_pair[0])
                    conversion_units = parameter_pair[1]
                    print(calculate_units_in_days(num_days, conversion_units))
                    i = input(prompt)
        except ValueError:
            print('Bad input')
            i = input(prompt)
