import collections

# Counters are a subclass of the dictionary class.
# Counters are mappings that hold an integer count for each key.
# They are commonly used to count the occurrences of elements in a collection.

# Initializing a Counter
ct = collections.Counter('abracadabra')
print(ct)
# The Counter object `ct` is initialized with the string 'abracadabra'.
# The output would be: Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# Updating a Counter
ct.update('aaaazzzzaaz')
print(ct)
# The update method is used to add the counts of additional elements to the existing Counter.
# In this case, the string 'aaaazzzzaaz' is added to `ct`.
# The output would be: Counter({'a': 10, 'z': 4, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# Most Common Items in a Counter
common_letters = ct.most_common(3)
print(common_letters)
# The most_common method returns an ordered list of tuples containing the n most common items and their counts.
# In this case, it returns the three most common items in `ct`.
# The output would be: [('a', 10), ('z', 4), ('b', 2)]
# It shows the most common item 'a' with a count of 10, followed by 'z' with a count of 4, and 'b' with a count of 2.


from collections import Counter
# Counters can be initialized in 3 different ways:
# 1. with a sequence of items
#    Example: print(Counter(['A', 'B', 'C', 'A', 'C']))
#    This creates a counter object that counts the occurrences of each item in the sequence.
#    The output would be: Counter({'A': 2, 'C': 2, 'B': 1})
#    It counts 'A' twice, 'C' twice, and 'B' once.

# 2. with a dictionary
#    Example: print(Counter({'A': 3, 'B': 4, 'C': 5}))
#    This creates a counter object directly from a dictionary.
#    The output would be: Counter({'C': 5, 'B': 4, 'A': 3})
#    It counts 'C' five times, 'B' four times, and 'A' three times.

# 3. with keyword arguments
#    Example: print(Counter(A=3, B=4, C=5))
#    This creates a counter object using keyword arguments.
#    The output would be: Counter({'C': 5, 'B': 4, 'A': 3})
#    It counts 'C' five times, 'B' four times, and 'A' three times.

# Update Function
coun = Counter()  # Initializes an empty counter

# To add data into it, we use the update function
coun.update([1, 2, 3, 4, 5, 6, 7])
# This updates the counter object `coun` by adding the elements from the given list.
# The counter now contains the counts of numbers from 1 to 7.

# We can use the subtract function to find the difference between one counter and another:
c1 = Counter(A=4, B=6, C=19)
c2 = Counter(A=3, B=4, C=9)

c2.subtract(c1)
# The subtract method subtracts the counts of elements in `c1` from the corresponding elements in `c2`.
# After subtracting, `c2` will have the updated counts based on the difference.

# Accessing elements
z = ['blue', 'green', 'blue', 'red', 'green', 'purple']
col_count = Counter(z)
print(col_count)
# The Counter function can be used to count the occurrences of elements in a list.
# In this case, `col_count` contains the counts of each element in the `z` list.
# The output would be: Counter({'blue': 2, 'green': 2, 'red': 1, 'purple': 1})
# It counts 'blue' twice, 'green' twice, 'red' once, and 'purple' once.

col = ['blue', 'red', 'green', 'yellow', 'purple']
for colour in col:
    print(colour, col_count[colour])
# This loop iterates over the elements in the `col` list and prints each element along with its count in `col_count`.
# It retrieves the count of each color in `col_count` and displays it.

coun = Counter(a=2, b=4, c=8)
print(coun)
# Another counter object `coun` is created with counts specified using keyword arguments.
# The output would be: Counter({'c': 8, 'b': 4, 'a': 2
