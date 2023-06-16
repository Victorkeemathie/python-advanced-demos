# Args and Kwargs in Python

# 1. Args:
# args is a special syntax in Python used to pass a variable number of positional arguments to a function.
# It allows you to pass any number of arguments without explicitly specifying their names.
# Inside the function, *args collects the arguments into a tuple.

def concatenate(*args):
    result = ""
    for arg in args:
        result += arg
    return result

print(concatenate("Hello", " ", "World"))
# Output: Hello World

# Example 2:
# Function to add variable number of arguments
def addition(*args):
    # Initialize the result to 0
    result = 0
    
    # Iterate over each argument in args
    for x in args:
        # Add the current argument to the result
        result = result + x
    
    # Print the final result
    print(result)

# Call the addition function with multiple arguments
addition(10, 20, 30)
# Output: 60


# 2. Kwargs:
# kwargs is a special syntax in Python used to pass a variable number of keyword arguments to a function.
# It allows you to pass key-value pairs as arguments without explicitly specifying their names.
# Inside the function, **kwargs collects the arguments into a dictionary.

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="John", age=25, city="New York")
# Output:
# name: John
# age: 25
# city: New York
