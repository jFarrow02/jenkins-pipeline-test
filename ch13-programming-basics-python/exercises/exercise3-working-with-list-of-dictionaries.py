# Using a list of 2 dictionaries:
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
  "age": 99,
  "birthday": "1922-02-21",
  "job": "Developer",
  "address": {
    "city": "Washington DC",
    "country": "USA"
  }
}
]

# write a Python program that:
# * Prints out the name, job, and city of each employee using a loop.
# * The program must work for any number of employees in the list.
# * Prints the country of the second employee inthe list by accessing it
# * directly without the loop

def get_employee_info():
    for employee in employees:
        print(f"Name: {employee['name']}")
        print(f"Job: {employee['job']}")
        print(f"City: {employee['address']['city']}")
        print("-----------------------------")
    
    print(employees[1]["address"]["country"])



get_employee_info()