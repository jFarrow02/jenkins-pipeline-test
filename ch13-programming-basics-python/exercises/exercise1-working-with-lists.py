# Write a program that prints out all the elements of the list that
# are higher than or equal to 10.

from multiprocessing.sharedctypes import Value


my_list = [1, 2, 2, 4, 4, 5, 6, 8, 10, 13, 22, 35, 52, 83]

for number in my_list:
    if number >= 10:
        print(number)

# Instead of printing the elements one by one, make a new list that has
# all the elements >= 10 and print out the new list
new_list = []
for number in my_list:
 if number >= 10:
     new_list.append(number)

print(new_list)
# Ask the user for a number as input and return a list that contains only
# those elements from my_list that are > than the user's input

def build_number_list():
    prompt = "Hello! Please enter a number, or 'exit' to quit: "
    user_input = ""
    while user_input != "exit":
        user_input = input(prompt)
        try:
            number_list = []
            selection = int(user_input)
            for n in my_list:
                if n > selection:
                    number_list.append(n)
            print("Returning your list...")
            #return number_list
            print(number_list)
        except ValueError:
            if user_input == "exit":
                print("Exiting application...")
            else:
                print("Invalid input. Please enter an integer.")



build_number_list()