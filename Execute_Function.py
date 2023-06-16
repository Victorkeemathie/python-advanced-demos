# Exec Function in Python
# The `exec()` function in Python is a built-in function that dynamically executes Python code stored in a string or a code object.
# It is often used to execute dynamically generated or user-provided code.
# The `exec()` function allows you to execute statements, define functions, classes, and modify the global and local namespaces.
# Syntax:
# `exec(object, globals, locals)`

# Parameters:
# - object: A string or a code object containing the Python code to be executed.
# - globals (optional): A dictionary representing the global namespace for the execution. If not provided, the current global namespace is used.
# - locals (optional): A dictionary representing the local namespace for the execution. If not provided, the current local namespace is used.

# Usage Examples:

# Example 1: Executing Python Statements
code = """
a = 10
b = 20
print(a + b)
"""
exec(code)
# Output: 30

# Example 2: Defining a Function
code = """
def greet(name):
    print(f"Hello, {name}!")
"""
exec(code)
greet("John")
# Output: Hello, John!

# Example 3: Modifying the Global Namespace
code = """
x = 5
y = 3
z = x * y
"""
global_vars = {}
exec(code, global_vars)
print(global_vars["z"])
# Output: 15

# Example 4: Modifying the Local Namespace
code = """
x = 5
y = 3
z = x * y
"""
local_vars = {}
exec(code, {}, local_vars)
print(local_vars["z"])
# Output: 15

# Note:
# - The `exec()` function can execute any valid Python code, including complex statements, loops, conditionals, and more.
# - It is important to exercise caution when using `exec()`, especially with user-provided code, as it can execute arbitrary code and pose security risks if not properly handled.
# - Use `exec()` judiciously and ensure that the code being executed comes from trusted sources.
