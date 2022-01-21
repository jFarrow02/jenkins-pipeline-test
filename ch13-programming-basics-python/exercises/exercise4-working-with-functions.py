# Write a function that accepts a list of dictionaries with employee age (see example list from the Exercise 3) and prints out the name and age of the youngest employee.

employees = [{
  "name": "Tina",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer",
  "address": {
    "city": "New York",
    "country": "USA"
  }
},
{
  "name": "Tim",
  "age": 35,
  "birthday": "1985-02-21",
  "job": "Developer",
  "address": {
    "city": "Sydney",
    "country": "Australia"
  },
},
{
  "name": "Foo",
  "age": 19,
  "birthday": "2003-02-21",
  "job": "Developer",
  "address": {
    "city": "Washington DC",
    "country": "USA"
  }
}
]

def find_youngest_employee(employees_list):
    youngest_employee = employees_list[0]

    for e in employees_list:
        if e["age"] < youngest_employee["age"]:
            youngest_employee = e

    print(f"Youngest Employee: {youngest_employee['name']} Age: {youngest_employee['age']}")

# find_youngest_employee(employees) # OK

# Write a function that accepts a string and calculates the number of upper case letters and lower case letters.
def count_uppers_and_lowers(input_string):
  if isinstance(input_string, str) == False:
    return "Input must be a string."

  upper_count = 0
  lower_count = 0

  for l in input_string:
    char = str(l)
    if char.isalpha():
      if char.isupper():
        upper_count += 1
      else:
        lower_count += 1

  return { upper_count: upper_count, lower_count: lower_count }
  
input_string = "The rain in Spain falls mainly on the plain."

# print(count_uppers_and_lowers(input_string))  # OK

# Write a function that prints the even numbers from a provided list.
def find_even_numbers(nums):
  
  for n in nums:
    try:
      number = int(n)
      if number % 2 == 0:
        print(number)
    except ValueError:
      continue


nums = [ 2, 33, 9, 10, 25, 1008, 42, 3.14159, "foo", 0 ]
find_even_numbers(nums)

# For cleaner code, declare these functions in its own helper Module and use them in the main.py file