# Automatic Handling of Missing Keys
# Sometimes it is convinient to have mappings that return some made-uo value when a missing key is searched
# There are two approaches to this: one is to use defaultdict  instead of a plain dict. 
# The other is to subclass dict or any other mapping type and add a _missing_ method. 
# When instatiating a defaultdict, you provide a callable to produce a default value whenever _getitem_ is passed a nonexistent key argument
# The callable that produces the default values is held in an instance attribute named default_factory
#  Unlike a regular dictionary, it never raises a KeyError when accessing or modifying a nonexistent key


# Example 1:
from collections import defaultdict  # Importing defaultdict from the collections module

new_defaultdict = defaultdict(set)  # Creating a defaultdict called 'new_defaultdict' with a default value of an empty set

new_defaultdict['Five'].add(5)  # Adding the key 'Five' to the defaultdict and adding the value 5 to its corresponding set
new_defaultdict['Ten'].add(10)  # Adding the key 'Ten' to the defaultdict and adding the value 10 to its corresponding set
new_defaultdict['Five'].add(5)  # Adding the value 5 again to the existing key 'Five' in the defaultdict
new_defaultdict['Ten'].add(10)  # Adding the value 10 again to the existing key 'Ten' in the defaultdict
new_defaultdict['Fifteen']  # Accessing the key 'Fifteen' in the defaultdict (which doesn't exist)

print(dict(new_defaultdict.items()))  # Converting the defaultdict to a regular dictionary using dict() and printing its items


# Example 2:
from collections import defaultdict  # Importing defaultdict from the collections module

# Define a list of fruits
fruits = ['apple', 'banana', 'cherry', 'apple', 'banana', 'apple']

# Create a defaultdict with a default value of 0
fruit_count = defaultdict(int)

# Count the occurrences of each fruit
for fruit in fruits:
    fruit_count[fruit] += 1

# Accessing keys that don't exist
fruit_count['mango'] += 1

# Accessing the counts of different fruits
print(fruit_count['apple'])   # Output: 3
print(fruit_count['banana'])  # Output: 2
print(fruit_count['cherry'])  # Output: 1
print(fruit_count['mango'])   # Output: 1

# Printing the entire fruit_count defaultdict
print(dict(fruit_count))

