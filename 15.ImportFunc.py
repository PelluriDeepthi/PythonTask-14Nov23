#Write a python program to define a module and import a specific function in that module to another program
from ModuleFunc import greet

# Use the imported function
name = input("Enter your name: ")
message = greet(name)

# Display the result
print(message)