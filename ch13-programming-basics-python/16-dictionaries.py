class InputException(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

prompt = "Hello! Enter number of days and conversion units, separated by \":\"\n"
separator = ":"

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
    input_is_valid = False

    while i != "exit":
    # while input_is_valid != True:
        try:
            if i.find(separator) == -1:
                print("Input must be separated by \":\"")
                i = input(prompt)
            else:
                parameter_pair = i.split(separator)
                if len(parameter_pair) > 2:
                    print("Please provide exactly two parameters")
                    i = input(prompt)
                # else:
                #     for p in parameter_pair:
                #         if(p.isdigit() == False):
                #             raise ValueError
                    
                #     input_is_valid = True
                #     parameter_dictionary = {"number_of_days": parameter_pair[0], "conversion_units": parameter_pair[1]}
                #     print(parameter_dictionary)
                #     print(parameter_dictionary["conversion_units"])
                #     print(parameter_dictionary["number_of_days"])
                #     i = input(prompt)
                else:
                    num_days = int(parameter_pair[0])
                    conversion_units = parameter_pair[1]
                    print(calculate_units_in_days(num_days, conversion_units))
                    i = input(prompt)
        except ValueError:
            print('Bad input')
            i = input(prompt)


validate_and_execute()

