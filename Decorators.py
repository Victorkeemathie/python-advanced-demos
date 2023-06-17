# Python Decorators

# Decorators are a powerful feature in Python that allow you to modify the behavior of functions or classes.
# A decorator is a function that takes another function as input and returns a modified or enhanced version of that function.
# Decorators are denoted using the '@' symbol followed by the decorator name, placed directly above the function definition.
#  Decorators provide a way to add functionality to existing functions without modifying their code directly.
# They are commonly used for tasks such as logging, timing, authorization, caching, and more.
# Decorators work by wrapping the original function with another function, allowing you to execute code before and after the original function is called.
# This wrapping process can be done using nested functions or by utilizing class-based decorators.
# By using decorators, you can keep your code modular, reusable, and maintainable.
# Python provides a built-in decorator called '@property' that allows you to define getter, setter, and deleter methods for class attributes.
# You can also create your own custom decorators to suit your specific needs.
# Decorators can be chained, allowing multiple decorators to be applied to a single function.
# Decorators are resolved and applied at the time of function definition, not at runtime.

# Example 1:

# Define a decorator function named 'new_capital'
def new_capital(new_func):
    # Define a nested function named 'new_inner'
    def new_inner():
        # Call the original function 'new_func' and store its result in 'the_func'
        the_func = new_func()
        # Convert the result to uppercase and store it in 'upper_case'
        upper_case = the_func.upper()
        # Return the modified result
        return upper_case
    
    # Return the nested function 'new_inner' as the decorated version of the function
    return new_inner

# Define a function named 'greeting'
def greeting():
    # Return a greeting message
    return "Hi, Python Programming"

# Create a decorated version of the 'greeting' function using the 'new_capital' decorator
new_decorating = new_capital(greeting)

# Call the decorated function and print the result
print(new_decorating())

# Alternatively, use the decorator syntax '@new_capital' to decorate the function directly
@new_capital
def greeting():
    return "Hi, Python Programming"

# Call the decorated function and print the result
print(greeting())

# Example involving Closure:

# Closure

def new_message(text):
    "Outer Message"  # Function definition comment

    def another_message():
        "Our nested message"  # Nested function definition comment
        print(text)  # Print the 'text' variable from the outer scope

    another_message()  # Call the nested function

new_message("Hello, this is a random Message")  # Call the outer function with a text argument

# Example involving higher-order functions:

def adding(num):
    def adding_one(num):  # Define a nested function called adding_one
        return num + 1  # Add 1 to the input number

    total = adding_one(num)  # Call the nested function with the input number
    return total  # Return the result

print(adding(20))  # Output: 21

# Example:

def adding(num):
    return num + 1  # Add 1 to the input number and return the result

def calling(new_func):
    new_number = 10  # Assign the value 10 to the variable new_number
    return new_func(new_number)  # Call the input function with new_number as the argument

print(calling(adding))  # Output: 11



