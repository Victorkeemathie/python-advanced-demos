# 1. QUEUES
# Queue is a linear structure that follows the First-In-First-Out (FIFO) structure
# Elements are added to the rear(enqueue) and are removed from the front(dequeue) of the queue
# The queue module in Python provides the Queue class to implement queues.
# Some of the operations include:
# Enqueue - Adding an element to the rear using the put method
# Dequeue - Removing and returning the element from the front of the queue using the get method
# Size - Checking the size of the elements using the the qsize method
# Empty - Checking if the queue is empty using the empty method
# Front - Accessing the element at the front without removing it using the queue[0] syntax

# Queue Example:
from queue import Queue

# Create a new queue
queue = Queue()

# Check if the queue is empty
is_empty = queue.empty()
print("Is the queue empty?", is_empty)  # Output: True

# Enqueue elements to the queue
queue.put(10)
queue.put(20)
queue.put(30)
queue.put(40)
queue.put(50)

# Get the size of the queue
size = queue.qsize()
print("Size of the queue:", size)  # Output: 5

# Access the element at the front of the queue without removing it
front_element = queue.queue[0]
print("Element at the front of the queue:", front_element)  # Output: 10

# Dequeue elements from the queue
dequeued_element = queue.get()
print("Dequeued element:", dequeued_element)  # Output: 10

# Check the size of the queue after dequeue
size = queue.qsize()
print("Size of the queue after dequeue:", size)  # Output: 4

# Enqueue another element
queue.put(60)

# Get all elements of the queue
all_elements = list(queue.queue)
print("All elements in the queue:", all_elements)  # Output: [20, 30, 40, 50, 60]

# Dequeue all elements from the queue
while not queue.empty():
    element = queue.get()
    print("Dequeued element:", element)

# Check if the queue is empty after dequeueing all elements
is_empty = queue.empty()
print("Is the queue empty?", is_empty)  # Output: True


# 2. DEQUES
# Deque Basics
# A deque is a double-ended queue that allows fast insertions and removals from both ends.
# It can be used as a stack (Last-In-First-Out) or a queue (First-In-First-Out).
# Example:
from collections import deque  # Importing the deque class from the collections module

# Creating a deque
my_deque = deque()

# Adding elements to the deque
my_deque.append(1)  # Add an element to the right end
my_deque.appendleft(2)  # Add an element to the left end
# The deque now contains [2, 1]

# Removing elements from the deque
last_element = my_deque.pop()  # Remove and return the rightmost element (1)
first_element = my_deque.popleft()  # Remove and return the leftmost element (2)
# The deque is now empty

# Working with a Fixed-Length Deque
fixed_deque = deque(maxlen=3)  # Create a deque with a fixed maximum length of 3
fixed_deque.append(1)
fixed_deque.append(2)
fixed_deque.append(3)
fixed_deque.append(4)  # Adding a fourth element automatically removes the leftmost element (1)
# The deque now contains [2, 3, 4]

# Rotating Elements in a Deque
my_deque = deque([1, 2, 3, 4, 5])
my_deque.rotate(2)  # Rotate the deque to the right by 2 positions
# The deque is now [4, 5, 1, 2, 3]
my_deque.rotate(-1)  # Rotate the deque to the left by 1 position
# The deque is now [5, 1, 2, 3, 4]

# Other Useful Operations
# There are additional operations available for deques, such as extending from both ends.
my_deque.extend([6, 7, 8])  # Add elements to the right end of the deque
# The deque is now [5, 1, 2, 3, 4, 6, 7, 8]
my_deque.extendleft([4, 3, 2])  # Add elements to the left end of the deque
# The deque is now [2, 3, 4, 5, 1, 2, 3, 4, 6, 7, 8]

# Note: Deques can also perform other operations like indexing, counting, and reversing elements.

# Summary:
# Deques are double-ended queues that allow fast insertions and removals from both ends.
# They can be used as stacks or queues.
# Deques can be fixed-length, and when full, adding new elements automatically removes the oldest elements.
# Deques provide methods like append, appendleft, pop, popleft, rotate, extend, extendleft, and more.
# They are useful for scenarios where you need efficient insertions and removals from both ends.



