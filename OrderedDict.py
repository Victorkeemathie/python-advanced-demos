# Now that the built-in `dict` also keeps the keys ordered since Python 3.6, the most common reason to use `OrderedDict` is writing code that is backward-compatible with earlier Python versions.

# The primary difference between `dict` and `OrderedDict` lies in the handling of key-value pair ordering.

# In `OrderedDict`, the equality operation checks for matching order, meaning that two `OrderedDict` instances are considered equal only if they have the same order of key-value pairs.

# Another difference is the `popitem()` method of `OrderedDict`, which has a different signature compared to the regular `dict`. `OrderedDict`'s `popitem()` method accepts an optional argument to specify which item is popped.

# `OrderedDict` provides the `move_to_end()` method, which efficiently repositions an element to an endpoint. This method allows you to move a specific key-value pair to either end of the `OrderedDict`, which can be useful in certain scenarios.

# The regular `dict` was primarily designed to be efficient for mapping operations, where tracking insertion order was secondary. Its focus is on fast lookups and insertions, with the order of insertion being of secondary importance.

# On the other hand, `OrderedDict` was specifically designed to be efficient at reordering operations. While it is also efficient for mapping operations, its main strength lies in its ability to efficiently handle reordering operations, such as moving items or changing their order.

# In terms of design priorities, the regular `dict` prioritizes space efficiency, iteration speed, and the performance of update operations. The order of insertion is not a primary concern.

# In contrast, `OrderedDict` prioritizes efficient reordering operations. Certain trade-offs were made regarding space efficiency, iteration speed, and update performance compared to the regular `dict` to optimize `OrderedDict` for reordering operations.

# Algorithmically, `OrderedDict` performs better than `dict` when it comes to frequent reordering operations. This makes it a suitable choice for scenarios where you need to track recent accesses, such as implementing an LRU (Least Recently Used) cache.

# Example:
from collections import OrderedDict

# Create a regular dictionary with some key-value pairs
new_dict = {'apple': 3, 'Cherry': 7, 'Banana': 8}
print(new_dict)
# Output: {'apple': 3, 'Cherry': 7, 'Banana': 8}

# Create an OrderedDict from the new_dict dictionary
new_ordered_dict = OrderedDict(new_dict)
print(new_ordered_dict)
# Output: OrderedDict([('apple', 3), ('Cherry', 7), ('Banana', 8)])

# Add a new key-value pair to the OrderedDict
new_ordered_dict['Pineapple'] = 5
print(new_ordered_dict)
# Output: OrderedDict([('apple', 3), ('Cherry', 7), ('Banana', 8), ('Pineapple', 5)])

# Update the value of an existing key in the OrderedDict
new_ordered_dict["apple"] = 10
print(new_ordered_dict)
# Output: OrderedDict([('apple', 10), ('Cherry', 7), ('Banana', 8), ('Pineapple', 5)])

# Remove a key-value pair from the OrderedDict using the pop() method
new_ordered_dict.pop("Banana")
print(new_ordered_dict)
# Output: OrderedDict([('apple', 10), ('Cherry', 7), ('Pineapple', 5)])

# Move a specific key-value pair to the end of the OrderedDict using move_to_end() method
new_ordered_dict.move_to_end("apple")
print(new_ordered_dict)
# Output: OrderedDict([('Cherry', 7), ('Pineapple', 5), ('apple', 10)])

# Iterate over the keys of the OrderedDict in reversed order
for item in reversed(new_ordered_dict):
    print(item)
# Output: apple Pineapple Cherry



