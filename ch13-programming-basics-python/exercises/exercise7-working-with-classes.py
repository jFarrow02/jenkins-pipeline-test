"""
Imagine you are working in a university and need to write a program, which handles 
data of students, professors and lectures. To work with this data you create classes 
and objects:

a) Create a Student class

with properties:

first name
last name
age
lectures he/she attends
with methods:

can print the full name
can list the lectures, which the student attends
can add new lectures to the lectures list (attend a new lecture)
can remove lectures from the lectures list (leave a lecture)
"""
class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def print_full_name(self):
         print(f"{self.first_name} {self.last_name}")

class Student(Person):

    def __init__(self, first_name, last_name, age, lectures):
        super().__init__(first_name, last_name, age)
        self.lectures = lectures

    def list_lectures(self):
        for l in self.lectures:
            print(l)

    def add_lecture(self, new_lecture):
        new_list = self.lectures[:]
        new_list.append(new_lecture)
        self.lectures = new_list

    def remove_lecture(self, lecture_name):
        self.lectures.remove(lecture_name)


"""
b) Create a Professor class

with properties:

first name
last name
age
subjects he/she teaches
with methods:

can print the full name
can list the subjects they teach
can add new subjects to the list
can remove subjects from the list
"""
class Professor(Person):
    
    def __init__(self, first_name, last_name, age, subjects_taught):
        super().__init__(first_name, last_name, age)
        self.subjects_taught = subjects_taught

    def list_subjects(self):
        for s in self.subjects_taught:
            print(s.name)

    def add_subject(self, subject):
        self.subjects_taught.append(subject)

    def remove_subject(self, subject):
        self.subjects_taught.remove(subject)


"""
c) Create a Lecture class

with properties:

name
max number of students
duration
list of professors giving this lecture
with methods:

printing the name and duration of the lecture
adding professors to the list of professors giving this lecture
"""

class Lecture:
    
    def __init__(self, name, max_student_capacity, duration, professors_list):
        self.name = name
        self.max_student_capacity = max_student_capacity
        self.duration = duration
        self.professors_list = professors_list

    def print_name_and_duration(self):
        print(f"Lecture Name: {self.name} -- Duration: {self.duration}")

    def add_professor(self, professor):
        self.professors_list.append(professor)

lecture1 = Lecture("Intro to Computer Science", 200, "120 days", [])
lecture2 = Lecture("Statistics 101", 150, "120 days", [])
lecture3 = Lecture("Data Structures 1", 50, "90 days", [])

professor1 = Professor("James", "Bond", 40, [lecture1, lecture3])
professor2 = Professor("Anusha", "Jain", 32, [lecture2, lecture1])

lecture1.add_professor(professor1)
lecture1.add_professor(professor2)
lecture2.add_professor(professor2)
lecture3.add_professor(professor1)

professor1.list_subjects()
professor2.list_subjects()