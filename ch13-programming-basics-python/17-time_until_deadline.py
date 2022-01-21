import datetime

user_input = input("Enter your goal with a deadline separated by a colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

# unformated_date = "Apr 9 2018"    
# print( datetime.datetime.strptime(unformated_date, "%b %d %Y").strftime('%y-%m-%d') )
# print( datetime.datetime.strptime(unformated_date, "%b %d %Y").strftime('%Y-%m-%d') )

deadline_date = datetime.datetime.strptime(deadline, "%m-%d-%Y")
print(deadline_date)
print(type(deadline_date))
# print(type(print(datetime.datetime.strptime(deadline, "%m-%d-%Y"))))

today_date = datetime.datetime.today()

if today_date >= deadline_date:
    print("Please select a date after today's date for your deadline")
else:
    print(f"Hello User! Time remaining for your goal {goal}: {(deadline_date - today_date).days} days")

