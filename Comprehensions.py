# Python List Comprehension
# Python List Comprehension means creating a new list from an existing list based on a given condition
# We can filter the old list to get the required elements and store them in a new list
# Syntax: [expression for item in old_list if condition]

# Example without List Comprehension:
old_list = [1, 2, 3, 4, 5]
new_list = []
# Iterate over the elements in the old list
for item in old_list:
    # Check if the item meets the condition (even numbers)
    if item % 2 == 0:
        # Add the item to the new list
        new_list.append(item)
# Print the new list
print(new_list)

# Example with List Comprehension:
old_list = [1, 2, 3, 4, 5]
# Use list comprehension to create a new list of even numbers
new_list = [item for item in old_list if item % 2 == 0]
# Print the new list
print(new_list)

# Example 1: Squaring Numbers
# Create a new list with squares of numbers from 1 to 10
# Using list comprehension
squares = [x ** 2 for x in range(1, 11)]
# Print the resulting list
print(squares)

# Example 2: Filtering Odd Numbers
# Create a new list with only the odd numbers from an existing list
# Existing list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Using list comprehension to filter odd numbers
odd_numbers = [x for x in numbers if x % 2 != 0]
# Print the resulting list
print(odd_numbers)

# Example 3: Extracting First Characters
# Create a new list with the first character of each word in an existing list
# Existing list of words
words = ["apple", "banana", "cherry", "date"]
# Using list comprehension to extract first characters
first_chars = [word[0] for word in words]
# Print the resulting list
print(first_chars)


# Dictionary Comprehension
# 1. Basic Syntax:
# newDict = {key: value for (key, value) in dictionary.items()}
# Explanation: This syntax pattern creates a new dictionary (newDict) by iterating over the items of an existing dictionary (dictionary).
# For each key-value pair, it assigns the key to the variable key and the value to the variable value.
# The resulting key-value pairs are used to construct the new dictionary.
# Example:
numbers = {1: 'one', 2: 'two', 3: 'three'}
doubled_numbers = {key: value * 2 for (key, value) in numbers.items()}
print(doubled_numbers)  # Output: {1: 'oneone', 2: 'twotwo', 3: 'threethree'}

# 2. Filtering with if Statement:
# newDict = {key: value for (key, value) in dictionary.items() if condition}
# Explanation: This syntax pattern allows you to include an if statement to filter
# the items in the original dictionary before creating the new dictionary.
# Only the key-value pairs that satisfy the condition will be included in the resulting dictionary.
# Example:
numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
filtered_numbers = {key: value for (key, value) in numbers.items() if key % 2 == 0}
print(filtered_numbers)  # Output: {2: 'two', 4: 'four'}

# 3. Conditional Expression:
# newDict = {key: value_if_true if condition else value_if_false for (key, value) in dictionary.items()}
# Explanation: This syntax pattern allows you to use a conditional expression 
# (value_if_true if condition else value_if_false) to determine the value for each key in the new dictionary.
# The condition is evaluated, and if it's true, the value_if_true is assigned; otherwise, the value_if_false is assigned.
# Example:
numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
replaced_numbers = {key: value.upper() if key % 2 == 0 else value.lower() for (key, value) in numbers.items()}
print(replaced_numbers)  # Output: {1: 'one', 2: 'TWO', 3: 'three', 4: 'FOUR'}

# 4. Nested if Statement:
# newDict = {key: value for (key, value) in dictionary.items() if outer_condition if inner_condition}
# Explanation: This syntax pattern allows you to use nested if statements to further filter the items in the original dictionary.
# Both the outer condition and the inner condition need to be satisfied for a key-value pair to be included in the resulting dictionary.
# Example:
numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
filtered_numbers = {key: value for (key, value) in numbers.items() if key % 2 == 0 if len(value) > 3}
print(filtered_numbers)  # Output: {4: 'four'}

# Define a dictionary named 'special_dishes' that contains the names of special dishes in the UK as keys and their corresponding prices in Kenyan Shillings as values
special_dishes = {
    "Fish and Chips": 1500,
    "Full English Breakfast": 1200,
    "Roast Beef with Yorkshire Pudding": 2250,
    "Chicken Tikka Masala": 1800,
    "Cornish Pasty": 900
}

# Print the original 'special_dishes' dictionary
print(special_dishes)

# Create a new dictionary 'my_dict' using a dictionary comprehension, which filters the items from 'special_dishes' based on the condition that the price (y) is greater than or equal to 1500,
# and assigns the dish name (x) as the key and the price (y) converted to an integer as the value
my_dict = {x: int(y) for (x, y) in special_dishes.items() if int(y) >= 1500}

# Print the new dictionary 'my_dict' that contains only the special dishes with prices greater than or equal to 1500
print(my_dict)

# Set Comprehension
# Set comprehension allows creating sets in a concise and expressive manner.
# Syntax:
# {expression for item in iterable if condition}
# Example 1: Creating a set of squares of numbers from 1 to 5
squares = {x ** 2 for x in range(1, 6)}
# Output: {1, 4, 9, 16, 25}
# Example 2: Creating a set of even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = {x for x in numbers if x % 2 == 0}
# Output: {2, 4, 6, 8, 10}
# Example 3: Creating a set of unique characters from a string
message = "hello world"
unique_chars = {char for char in message if char.isalpha()}
# Output: {'e', 'l', 'h', 'r', 'o', 'd', 'w'}
# Example 4: Creating a set of lengths of words in a sentence
sentence = "This is a sample sentence"
word_lengths = {len(word) for word in sentence.split()}
# Output: {1, 2, 4, 7, 8}
# - Set comprehension can be used to filter elements using conditions.
# - The resulting set contains unique elements only.
# - If the expression evaluates to a duplicate value, it will be ignored.
# Set comprehension is a powerful technique for creating sets based on existing iterables and applying filtering conditions. 
# It provides a concise and efficient way to generate sets with specific characteristics.

# Set Comprehension Example
# Create a set of odd numbers from 1 to 100 using set comprehension.
# Syntax:
# {expression for item in iterable if condition}
# Here, we use set comprehension to generate a set of odd numbers.
# We iterate over the range from 1 to 100 and only include the numbers that are not divisible by 2 (i.e., odd numbers).
# Step 1: Define the set using set comprehension.
set1 = {i for i in range(1, 101) if i % 2 != 0}
# Output: {1, 3, 5, 7, 9, ..., 99}
# Step 2: Print the resulting set.
print(set1)

# Tuple Comprehension in Python

# Tuple comprehension is a concise way to create tuples using an iterable and an optional condition. 
# It allows you to define a tuple in a single line by applying an expression to each item in the iterable. 
# Tuple comprehension follows a similar syntax to list comprehension, but instead of square brackets, we use parentheses to create tuples.

# Syntax:
# result_tuple = (expression for item in iterable if condition)

# Notes:
# The 'expression' is applied to each 'item' in the 'iterable'.
# The 'if condition' is optional. It filters the items based on a given condition.

# Example 1: Creating a tuple of squares of numbers
squares = tuple(x ** 2 for x in range(1, 6))
# Output: (1, 4, 9, 16, 25)

# Example 2: Creating a tuple of even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = tuple(x for x in numbers if x % 2 == 0)
# Output: (2, 4, 6, 8, 10)

# Example 3: Creating a tuple of uppercase characters from a string
word = "Hello, World!"
uppercase_chars = tuple(char.upper() for char in word if char.isalpha())
# Output: ('H', 'E', 'L', 'L', 'O', 'W', 'O', 'R', 'L', 'D')

# Example 4: Creating a tuple of lengths of strings
strings = ["apple", "banana", "cherry", "date"]
lengths = tuple(len(s) for s in strings)
# Output: (5, 6, 6, 4)

# Benefits of Tuple Comprehension:
# - Concise and readable way to create tuples.
# - Saves time and reduces the need for writing lengthy for loops.
# - Allows you to perform transformations and filtering on the fly.

# Note: Tuple comprehension is available in Python 2.7 and all later versions.
