# A Metaclass is a class that creates instances of classes
# When a class is defined, its definition becomes an object controlled by a metaclass
# This built-in metaclass is “type” which creates a class objects
# Custom metaclasses can be defined by inheriting from “type” 
# Metaclasses propagate via inheritance, and they provide extreme control over class definition and creation

# Example:

# Define a metaclass named MyMeta that inherits from type
class MyMeta(type):
    # Override the __new__() method of the metaclass
    def __new__(cls, name, bases, attrs):
        # Add a new attribute called 'message' to the class
        attrs['message'] = "This class was created dynamically."
        # Create the class using the metaclass by calling the parent __new__() method
        return super().__new__(cls, name, bases, attrs)

# Define a class named MyClass and specify MyMeta as its metaclass
class MyClass(metaclass=MyMeta):
    pass

# Create an instance of MyClass
obj = MyClass()

# Print the value of the 'message' attribute of the instance
print(obj.message)  # Output: This class was created dynamically.

