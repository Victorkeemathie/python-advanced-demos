# Map Function in Python

# The map() function is a built-in Python function that applies a specified function to each item of an iterable and returns an iterator containing the results.

# Syntax:
# map(function, iterable)

# Parameters:
# - function: A function or lambda expression that defines the operation to be performed on each item of the iterable.
# - iterable: An iterable object (e.g., list, tuple, string) whose elements will be passed to the function.

# Returns:
# - An iterator that yields the results of applying the function to each item of the iterable.

# Example 1: Squaring Numbers using map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))
# Output: [1, 4, 9, 16, 25]

# Example 2: Converting Celsius to Fahrenheit using map()
celsius_temperatures = [22.5, 30.8, 15.2, 10.7]
fahrenheit_temperatures = map(lambda c: c * 9/5 + 32, celsius_temperatures)
print(list(fahrenheit_temperatures))
# Output: [72.5, 87.44, 59.36, 51.26]

# Example 3: Concatenating Strings using map()
names = ['Alice', 'Bob', 'Charlie']
greetings = map(lambda name: 'Hello, ' + name, names)
print(list(greetings))
# Output: ['Hello, Alice', 'Hello, Bob', 'Hello, Charlie']

# Example 4: Mapping Multiple Iterables
numbers = [1, 2, 3]
squares = [1, 4, 9]
cubes = [1, 8, 27]
result = map(lambda x, y, z: x + y + z, numbers, squares, cubes)
print(list(result))
# Output: [3, 14, 39]

# Note:
# - The number of arguments passed to the function should match the number of iterables provided.
# - The map() function stops producing values as soon as any of the input iterables is exhausted.

# Additional Considerations:
# - The map() function returns an iterator, so we convert it to a list or iterate over it using a loop to obtain the desired results.
# - In Python 3, map() returns a map object, which is an iterator. In Python 2, it returns a list.
# - The map() function can also accept multiple iterables, and the provided function should have the corresponding number of arguments to handle the values from each iterable.

# The map() function is a powerful tool for applying a function to multiple items in an iterable, offering a concise and efficient way to process data.

# Example 5:
list1 = ['apple', 'banana', 'cherry']
list2 = ['dog', 'elephant', 'fox']

# Use the zip() function to pair corresponding elements from both lists, and concatenate them
concatenated_lists = map(lambda pair: pair[0] + ' ' + pair[1], zip(list1, list2))

# Print the concatenated lists
print(list(concatenated_lists))
# Output: ['apple dog', 'banana elephant', 'cherry fox']

# Example 6:
strings = ['hello', 'world', 'python']

# Use a lambda function to reverse each string in the list
reversed_strings = map(lambda s: s[::-1], strings)

# Print the reversed strings
print(list(reversed_strings))
# Output: ['olleh', 'dlrow', 'nohtyp']
