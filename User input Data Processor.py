#Objective: The aim of this assignment is to process and format user input data.

#Task 1: Input Length Validator Write a script that asks for and checks the length of the user's first name and last name.
#  Both should be at least 2 characters long. If not, print an error message.

# NOTE: Ensure that all code in your file is ready to run. 
# This means that if someone opens your file and clicks the run button at the top, all code executes as intended. 
# For example, if there are if statements, print statements, or for loops, they should function correctly and display output in the console as expected. 
# If you have a function, make sure the function is called and runs.


#The goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested.

def enter_name(prompt):
    while True:
        name = input(prompt)
        if len(name) >= 2:
            return name
        else:
            print("Error: Name must be at least 2 characters long.")

first_name = enter_name("Enter your first name: ")
last_name = enter_name("Enter your last name: ")

print(f"Welcome, {first_name} {last_name}!")