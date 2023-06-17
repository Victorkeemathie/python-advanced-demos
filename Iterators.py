# Iterators in Python are objects that represent a countable or sequence of values
# They allow us to traverse through a collection of items one by one
# Iterators provide a way to efficiently process large amounts of data or handle infinite sequences
# We use the "iter()" function to obtain an iterator object
# The "next()" function is then used to retrieve the next item in the iterator

# Example 1:

fruits = ["apple", "banana", "cherry"]

# Get an iterator object
fruit_iterator = iter(fruits)

# Accessing elements using next()
print(next(fruit_iterator))  # Output: "apple"
print(next(fruit_iterator))  # Output: "banana"
print(next(fruit_iterator))  # Output: "cherry"

# Example 2:

text = "Hello, World!"

# Get an iterator object
char_iterator = iter(text)

# Accessing characters using next()
print(next(char_iterator))  # Output: "H"
print(next(char_iterator))  # Output: "e"
print(next(char_iterator))  # Output: "l"
print(next(char_iterator))  # Output: "l"
print(next(char_iterator))  # Output: "o"

# Example 3:
def new_iterator(n):
    # Create an iterator object from the input iterable using the `iter()` function
    my_iterable = iter(n)

    # Enter an infinite loop to iterate over the items in the iterator
    while True:
        try:
            # Retrieve the next item from the iterator using the `next()` function
            # and print it
            print(next(my_iterable))
        except StopIteration:
            # If a `StopIteration` exception is raised, it means there are no more
            # items in the iterator, so break out of the loop
            break

# Call the `new_iterator` function with a tuple as input
new_iterator((10, 20, 30, 40))

# Call the `new_iterator` function with a string as input
new_iterator("I love learning Python")

# Example 4:

# Building Iterator using OOP

class Incrementing:
    def __iter__(self):
        # Initialize the count to 0 when the iterator is created
        self.count = 0
        # Return the instance of the object itself as the iterator
        return self

    def __next__(self):
        if self.count <= 15:
            # Store the current count in a variable
            x = self.count
            # Increment the count for the next iteration
            self.count += 1
            return x
        else:
            # If the count exceeds 15, raise a StopIteration exception to signal the end of iteration
            raise StopIteration

# Create an instance of the Incrementing class
#new_obj = Incrementing()

# Obtain the iterator from the object
#new_iter = iter(new_obj)

# Retrieve and print the next item from the iterator
#print(next(new_iter))

# Iterate over the Incrementing object using a for loop
for num in Incrementing():
    print(num)
