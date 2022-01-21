# Using the following dictonary:

from operator import delitem


employee = {
  "name": "Tim",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer"
}

# Write a Python Script that:
# * updates the job to Software Engineer
# * removes the age key form the dictionary
# * Loops through the dictionary and prints the key:value pairs one by one

def update_employee():
    employee["job"] = "Software Engineer"
    del employee["age"]
    for key, val in employee.items():
        print(f"{key} : {val}")


# update_employee() # OK

# Using the following 2 dictionaries:
dict_one = {'a': 100, 'b': 400} 
dict_two = {'x': 300, 'y': 200}

# Write a Python script that:
# * merges these two dictionaries into 1 new dictionary
# * sums up all the values in the new dictionary and prints out sum
# * prints the max and min values of the dictionary

def merge_dictionaries():
    merged = {}
    merged.update(dict_one)
    merged.update(dict_two)

    sum = 0
    max = merged["a"]
    min = merged["a"]

    for val in merged.values():
        sum+= val
        if val > max:
            max = val
        if val < min:
            min = val

    print(f"Sum: {sum}")
    print(f"Max: {max}")
    print(f"Min: {min}")
    
    return merged

print(merge_dictionaries())

    