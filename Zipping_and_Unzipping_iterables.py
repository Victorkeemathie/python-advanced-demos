# 1. Zipping Iterables
# Zipping iterables combine multiple iterables into a single iterable
# The zip() function is  used for zipping iterables
# It takes multiple iterables to as arguments and returns an iterator of tupples
# Each tupple contains corresponding elements from the input iterables
# If the input iterables have different lentghs, the resulting zipped iterable will have a length equal to the shortest input iterable
# Example:

# Zipping Iterables
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
scores = [90, 85, 95]

# Zip the iterables together
zipped = zip(names, ages, scores)

# Iterate over the zipped object and print the results
for name, age, score in zipped:
    print(f"Name: {name}, Age: {age}, Score: {score}")
# Output:
# Name: Alice, Age: 25, Score: 90
# Name: Bob, Age: 30, Score: 85
# Name: Charlie, Age: 35, Score: 95

# 2. Unzipping
# Unzipping is the process of seperating a zipped iterable back to its original individual iterables
# It allows you to reverse the zipping operation and retrieve the original data from a zipped iterable
# Unzipping can be done using the zip() function in combination with the * operator
# Example:

# Zipped iterable
zipped = [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Unzip the zipped iterable
names, ages = zip(*zipped)

# Print the unzipped iterables
print("Names:", names)  # Output: Names: ('Alice', 'Bob', 'Charlie')
print("Ages:", ages)    # Output: Ages: (25, 30, 35)

Example 2:
  
# Zip two lists together
numbers = [1, 2, 3]
letters = ['x', 'y', 'z']
zipped = zip(numbers, letters)

# Iterate over the zipped iterable
for pair in zipped:
    number, letter = pair
    print(f"Number: {number}, Letter: {letter}")

# Output:
# Number: 1, Letter: x
# Number: 2, Letter: y
# Number: 3, Letter: z

