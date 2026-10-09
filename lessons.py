LESSONS = [
    {
        "id": "intro",
        "title": "1. Introduction to Python",
        "level": "Beginner",
        "objective": "Understand what Python is and why it is important.",
        "concept": """
Python is one of the most beginner-friendly programming languages.
It is used in:
- web development
- automation
- data analysis
- AI and ML
- scripting
- software development
""",
        "example": """
print("Hello, World!")
name = "Rahul"
print("Welcome,", name)
""",
        "explanation": """
print() is used to display output.
Variables are used to store values.
""",
        "exercise": "Write a program that prints your name and age.",
    },
    {
        "id": "variables",
        "title": "2. Variables and Data Types",
        "level": "Beginner",
        "objective": "Learn how to store and manage data.",
        "concept": """
Python has different data types such as:
- int
- float
- str
- bool
""",
        "example": """
age = 21
price = 99.5
name = "Aisha"
is_student = True

print(type(age))
print(type(price))
print(type(name))
print(type(is_student))
""",
        "explanation": """
type() tells us what type of data a variable contains.
""",
        "exercise": "Create variables for name, age, and city and print them.",
    },
    {
        "id": "input_output",
        "title": "3. Input and Output",
        "level": "Beginner",
        "objective": "Learn to interact with the user.",
        "concept": """
Use input() to read values from the user.
Use print() to display output.
""",
        "example": """
name = input("Enter your name: ")
print("Hello,", name)
""",
        "explanation": """
input() waits for user input and stores it as a string.
""",
        "exercise": "Ask the user for their city and print a welcome message.",
    },
    {
        "id": "operators",
        "title": "4. Operators",
        "level": "Beginner",
        "objective": "Use arithmetic and comparison operators.",
        "concept": """
Operators help with calculations and comparisons.
Examples:
+, -, *, /, ==, !=, >, <
""",
        "example": """
a = 10
b = 5

print(a + b)
print(a > b)
print(a == b)
""",
        "explanation": """
Operators allow you to work with values logically and mathematically.
""",
        "exercise": "Add two numbers entered by the user.",
    },
    {
        "id": "conditions",
        "title": "5. Conditional Statements",
        "level": "Beginner",
        "objective": "Make decisions in your code.",
        "concept": """
if, elif, and else are used to test conditions.
""",
        "example": """
marks = 75

if marks >= 50:
    print("Pass")
else:
    print("Fail")
""",
        "explanation": """
If the condition is true, the if block runs.
Otherwise, the else block runs.
""",
        "exercise": "Write a program to check whether a number is even or odd.",
    },
    {
        "id": "loops",
        "title": "6. Loops",
        "level": "Beginner",
        "objective": "Repeat actions without writing repetitive code.",
        "concept": """
Loops help do repeated tasks.
- for loop
- while loop
""",
        "example": """
for i in range(1, 6):
    print(i)

count = 1
while count <= 5:
    print(count)
    count += 1
""",
        "explanation": """
Loops are important for automation and repetition.
""",
        "exercise": "Print numbers from 1 to 10 using a for loop.",
    },
    {
        "id": "lists",
        "title": "7. Lists",
        "level": "Beginner",
        "objective": "Store multiple values in one variable.",
        "concept": """
A list is an ordered collection of items.
""",
        "example": """
fruits = ["Apple", "Banana", "Orange"]
print(fruits[0])
print(len(fruits))
fruits.append("Mango")
print(fruits)
""",
        "explanation": """
Lists allow you to store many values in one container.
""",
        "exercise": "Create a list of 5 favorite books.",
    },
    {
        "id": "functions",
        "title": "8. Functions",
        "level": "Beginner",
        "objective": "Write reusable code blocks.",
        "concept": """
A function is a named block of code that performs a task.
""",
        "example": """
def add(a, b):
    return a + b

print(add(5, 3))
""",
        "explanation": """
Functions help you organize code and avoid repetition.
""",
        "exercise": "Write a function to calculate the area of a rectangle.",
    },
    {
        "id": "dictionaries",
        "title": "9. Dictionaries",
        "level": "Intermediate",
        "objective": "Store data as key-value pairs.",
        "concept": """
A dictionary stores values with keys.
""",
        "example": """
student = {"name": "Rahul", "age": 20, "city": "Pune"}

print(student["name"])
print(student.get("city"))
""",
        "explanation": """
Dictionaries are useful for structured data.
""",
        "exercise": "Create a dictionary of a student and print the values.",
    },
    {
        "id": "files",
        "title": "10. File Handling",
        "level": "Intermediate",
        "objective": "Read and write files.",
        "concept": """
Python can work with files.
Common modes:
- r = read
- w = write
- a = append
""",
        "example": """
with open("demo.txt", "w") as file:
    file.write("Python is fun!")

with open("demo.txt", "r") as file:
    print(file.read())
""",
        "explanation": """
File handling is useful when you want to store data permanently.
""",
        "exercise": "Write your favorite subjects into a file.",
    },
    {
        "id": "exceptions",
        "title": "11. Exception Handling",
        "level": "Intermediate",
        "objective": "Handle errors without crashing the program.",
        "concept": """
Use try and except to capture errors safely.
""",
        "example": """
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
""",
        "explanation": """
This prevents the program from crashing unexpectedly.
""",
        "exercise": "Handle invalid input entered by the user.",
    },
    {
        "id": "oop",
        "title": "12. Object-Oriented Programming",
        "level": "Intermediate",
        "objective": "Understand classes and objects.",
        "concept": """
OOP organizes code into classes and objects.
""",
        "example": """
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)

s1 = Student("Aman", 20)
s1.show()
""",
        "explanation": """
Classes are blueprints, and objects are instances of those blueprints.
""",
        "exercise": "Create a class for a Book with title and author.",
    },
]

QUIZ_BANK = {
    "intro": [
        {"question": "Which function prints output?", "options": ["print()", "input()", "show()", "write()"], "answer": "print()"},
        {"question": "What does a variable store?", "options": ["Data", "Loop", "Function", "File"], "answer": "Data"},
    ],
    "variables": [
        {"question": "Which type stores whole numbers?", "options": ["int", "float", "str", "bool"], "answer": "int"},
        {"question": "Which value is a string?", "options": ['"Hello"', "True", "10", "3.14"], "answer": '"Hello"'},
    ],
    "input_output": [
        {"question": "Which function reads user input?", "options": ["input()", "print()", "sum()", "type()"], "answer": "input()"},
        {"question": "What does input() usually return?", "options": ["String", "Integer", "List", "Dictionary"], "answer": "String"},
    ],
    "operators": [
        {"question": "Which operator adds two numbers?", "options": ["+", "-", "*", "/"], "answer": "+"},
        {"question": "Which operator checks equality?", "options": ["==", "=", "!=", ">"], "answer": "=="},
    ],
    "conditions": [
        {"question": "Which keyword starts a decision block?", "options": ["if", "for", "while", "def"], "answer": "if"},
        {"question": "If a condition is false, which block often runs?", "options": ["else", "loop", "function", "class"], "answer": "else"},
    ],
    "loops": [
        {"question": "Which loop is best for fixed repetition?", "options": ["for loop", "if loop", "else loop", "def loop"], "answer": "for loop"},
        {"question": "Which requirement is essential for a while loop?", "options": ["A condition", "A class", "A file", "A dict"], "answer": "A condition"},
    ],
    "lists": [
        {"question": "What is a list?", "options": ["Collection of values", "Function", "Loop", "Variable"], "answer": "Collection of values"},
        {"question": "Which method adds an item to a list?", "options": ["append()", "add()", "push()", "insert()"], "answer": "append()"},
    ],
    "functions": [
        {"question": "What is a function?", "options": ["Reusable block of code", "Data type", "Loop", "File"], "answer": "Reusable block of code"},
        {"question": "Which keyword defines a function?", "options": ["def", "class", "if", "for"], "answer": "def"},
    ],
    "dictionaries": [
        {"question": "A dictionary stores data in what format?", "options": ["key-value pairs", "only numbers", "only strings", "only arrays"], "answer": "key-value pairs"},
        {"question": "Which syntax creates a dictionary?", "options": ['{"name": "Rahul"}', "[1,2,3]", "(1,2,3)", "print()"], "answer": '{"name": "Rahul"}'},
    ],
    "files": [
        {"question": "Which mode opens a file for writing?", "options": ["w", "r", "x", "d"], "answer": "w"},
        {"question": "Which method reads file content?", "options": ["read()", "write()", "print()", "open()"], "answer": "read()"},
    ],
    "exceptions": [
        {"question": "Which block handles errors?", "options": ["except", "if", "for", "else"], "answer": "except"},
        {"question": "Why use exception handling?", "options": ["To avoid crashes", "To delete files", "To create loops", "To print values"], "answer": "To avoid crashes"},
    ],
    "oop": [
        {"question": "What is a class?", "options": ["Blueprint for objects", "Loop structure", "Function name", "Variable"], "answer": "Blueprint for objects"},
        {"question": "What is an object?", "options": ["Instance of a class", "Dictionary", "File", "Keyword"], "answer": "Instance of a class"},
    ],
}

PROJECT_IDEAS = [
    "Calculator App",
    "To-Do List",
    "Student Record System",
    "Expense Tracker",
    "Number Guessing Game",
    "Library Management System",
    "Quiz App",
    "Attendance Tracker",
]
