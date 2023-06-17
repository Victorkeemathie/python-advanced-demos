# The `eval()` function in Python is a powerful built-in function that allows you to dynamically evaluate and execute Python code stored in a string.

# Evaluation of Expressions:
# The primary use of `eval()` is to evaluate expressions. An expression can be a mathematical calculation, logical operation, or any other valid Python expression.
result = eval("2 + 3 * 4")
print(result)  # Output: 14

# Execution of Statements:
# `eval()` can also execute Python statements, such as function calls, variable assignments, loops, conditionals, or even complex code blocks.
eval("print('Hello, World!')")
eval("x = 10")
print(x)  # Output: 10

# Namespace Context:
# `eval()` operates within a specified namespace context. By default, it uses the current global and local namespaces. However, you can provide explicit dictionaries for the `globals` and `locals` parameters to control the namespace.
x = 5
y = 2
namespace = {'x': 10, 'y': 3}
result = eval("x * y", namespace)
print(result)  # Output: 30

# Example 1:

# Assigning values to variables
x = 10
y = 5

# Evaluating the expression 'x+y' using the eval() function
# The expression is evaluated within the context of the provided dictionary {'x': x, 'y': y}
result = eval('x+y', {'x': x, 'y': y})

# Printing the result
print(result)

# Example 2:
# Evaluating the expression 'x + y' using the eval() function
# The expression is evaluated with an empty global namespace {} and the provided local namespace {'x': 50, 'y': 100}
result = eval('x + y', {}, {'x': 50, 'y': 100})

# Printing the result
print(result)
