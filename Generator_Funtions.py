# Generators are functions in Python that behave like iterators
# They allow you to generate a sequence of values dynamically
# The “yield” keyword is used to return a value from the generator function and pause its execution, preserving its internal state
#  A generator object is created when the generator function is called, and its code doesn't start executing immediately
# The execution is triggered when we iterate over the generator object using the next() function or a for loop
# The function execution is suspended at each yield statement, and the yielded value is returned

# Example 1:
def even_numbers(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_gen = even_numbers(numbers_list)
for num in even_gen:
    print(num)

# Example 2:
# Define a generator function
def new_generator():
    x = 0  # Initialize a variable x to 0
    print("Our first point here")  # Print a message indicating the first point
    yield x  # Yield the current value of x and suspend the function's execution
    x += 1  # Increment x by 1
    print("Our second point here")  # Print a message indicating the second point
    yield x  # Yield the updated value of x and suspend the function's execution
    x += 1  # Increment x by 1
    print("Our third point here")  # Print a message indicating the third point
    yield x  # Yield the final value of x and suspend the function's execution

# Create a generator object
new_ob = new_generator()

# Obtain and print the first yielded value from the generator
print(f"The value of x is {next(new_ob)}")

# Obtain and print the second yielded value from the generator
print(f"The value of x is {next(new_ob)}")

# Obtain and print the third yielded value from the generator
print(f"The value of x is {next(new_ob)}")
