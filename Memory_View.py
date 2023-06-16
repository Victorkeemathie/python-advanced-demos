# Memory Views in Python
# The built-in memoryview class is a shared-memory sequence type that lets you handle clices of arrays without copying bytes
# It was inspired by the NumPy Library

# According to Travis Oliphant, lead author of NumPy, a memoryview is a generalized NumPy array structure in Python itself, that allows you to share memory between data-structures without first copying
# The memoryview object allows accessing the internal memory of an object, such as an array or a buffer, without creating a new copy of the data
# By using memoryview, you can manipulate and access the underlying data of an object more efficiently, especially when dealing with large datasets.
# Example:

# Create a bytes object
x = b'Python Programming'

# Display the type of x
print(type(x))  # Output: <class 'bytes'>

# Create a memoryview object from x
new = memoryview(x)

# Display the type of new
print(type(new))  # Output: <class 'memoryview'>

# Display the original object referred to by new
print(new.obj)  # Output: b'Python Programming'

# Convert the memoryview to a list
print(new.tolist())  # Output: [80, 121, 116, 104, 111, 110, 32, 80, 114, 111, 103, 114, 97, 109, 109, 105, 110, 103]

# Create a bytearray object
p = bytearray("Python is a powerful programming language", "utf-8")

# Display the type of p
print(type(p))  # Output: <class 'bytearray'>

# Create a memoryview object from p
k = memoryview(p)

# Display the memory location of k
print(k)  # Output: <memory at 0x00000125FC874B80>

# Access a specific element at index 4 in the memoryview
print(k[4])  # Output: 111

# Convert the value to a character using chr()
print(chr(k[4]))  # Output: o

