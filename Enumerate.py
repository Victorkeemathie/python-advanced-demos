# Enumerate in Python
# The enumerate() function is a built-in Python function that allows iterating over an iterable while keeping track of the index or position of each element.
# It returns an enumerate object, which contains pairs of index-value pairs.

# Syntax:
# enumerate(iterable, start=0)

# Parameters:
# - iterable: An iterable object to be enumerated.
# - start (optional): An integer value specifying the starting index. By default, it is set to 0.

# Returns:
# - An enumerate object that yields pairs of index-value tuples.

# Example 1: Enumerating a List
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)
# Output:
# 0 apple
# 1 banana
# 2 cherry

# Example 2: Enumerating with a Custom Starting Index
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
# Output:
# 1 apple
# 2 banana
# 3 cherry

# Example 2::
fruits = ['apple', 'banana', 'cherry']

# Create an enumerate object
fruits_enum = enumerate(fruits)

# Use the __next__() method to retrieve the next item in the enumeration
print(fruits_enum.__next__())  # Output: (0, 'apple')
print(fruits_enum.__next__())  # Output: (1, 'banana')
print(fruits_enum.__next__())  # Output: (2, 'cherry')
