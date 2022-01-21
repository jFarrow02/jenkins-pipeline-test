import datetime

"""
Write a program that:

accepts user's birthday as input
and calculates how many days, hours and minutes are remaining till the birthday
prints out the result as a message to the user

"""

def countdown_to_birthday():
    prompt = "Welcome to the birthday countdown!\n"
    prompt += "Please enter your birthdate as MM/DD:\n"

    is_valid_birthdate = False

    while is_valid_birthdate == False:
        try:
            response = input(prompt)
            split_response = response.split("/")
            day = int(split_response[1])
            month = int(split_response[0])
            if (day > 31 or day < 1) or (month > 12 or month < 1):
                raise ValueError
                
            now = datetime.datetime.today()
            this_year = now.year
            birthdate = response + "/" + str(this_year)
            next_birthday = datetime.datetime.strptime(birthdate, "%m/%d/%Y")
            time_until_birthday = next_birthday - now

            hours_diff = 24 - now.hour
            mins_diff = 60 - now.minute

            print(f"There are {time_until_birthday.days} days, {hours_diff} hours, {mins_diff} minutes left until your birthday!")
            is_valid_birthdate = True
        except ValueError:
            print("Invalid birthdate. Please try again.")

    


countdown_to_birthday()