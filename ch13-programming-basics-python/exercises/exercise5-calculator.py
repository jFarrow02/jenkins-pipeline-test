"""Write a simple calculator program that:

takes user input of 2 numbers and operation to execute
handles following operations: plus, minus, multiply, divide
does proper user validation and give feedback: only numbers allowed
Keeps the Calculator program running until the user types “exit”
Keeps track of how many calculations the user has taken, and when the user exits the calculator 
program, prints out the number of calculations the user did """

def calculate():
    selection = ""
    prompt = "Welcome to Calculator! Please enter a calculation in the following format: \n"
    prompt += "x <operator> y \n"
    prompt += "where x and y are numbers, and <operator> is any of +, -, *, or /. \n"
    prompt += "Enter 'exit' to quit.\n"

    calculation_count = 0

    while selection != "exit":
        selection = input(prompt)
        selection_as_array = selection.split()
        if selection != "exit":
            try:
                operand1 = float(selection_as_array[0])
                operand2 = float(selection_as_array[2])
                operator = selection_as_array[1]
                result = 0

                match operator:
                    case "+":
                        result = operand1 + operand2
                    case "-":
                        result = operand1 - operand2
                    case "*":
                        result = operand1 * operand2
                    case "/":
                        if operand2 != 0:
                            result = operand1 / operand2
                        else:
                            print("Division by zero is undefined")
                            continue
                    case _:
                        print("Unknown operation.")
                        continue
                    
                print(f"{operand1} {operator} {operand2} = {result}\n")
                calculation_count += 1

            except ValueError:
                print("Please enter integer or decimal values only.")
        else:
            print(f"You performed {calculation_count} calculations. Exiting...")

calculate(10,11)
