# Logging in Python:
# Logging is a built-in module in Python that allows you to record useful information, warnings, errors, and debugging messages during the execution of a program.
# It provides a flexible and standardized way to track events and activities within your code, making it easier to diagnose issues and monitor the application's behavior.
# The logging module provides various log levels, allowing you to categorize messages based on their severity, such as DEBUG, INFO, WARNING, ERROR, and CRITICAL.

# Building a Logger in Python:

# Step 1: Import the logging module:
   import logging

# Step 2: Configure the logging settings (optional):
# You can customize the logging format, level, output location, and more.
# For example:
     logging.basicConfig(
         filename='app.log',
         level=logging.DEBUG,
         format='%(asctime)s - %(levelname)s - %(message)s'
     )

# Step 3: Create a logger instance:
   logger = logging.getLogger('my_logger')

# Step 4: Add handlers to the logger:
#    Handlers define where the log messages should be sent, such as the console, file, or external services.
#    For example, to log messages to the console:
#    console_handler = logging.StreamHandler()
#    logger.addHandler(console_handler)

#  Step 5: Log messages using different log levels:
   - Example log statements:
     logger.debug('Debug message')
     logger.info('Info message')
     logger.warning('Warning message')
     logger.error('Error message')
     logger.critical('Critical message')

# Step 6: Use placeholders and variables in log messages:
# You can include dynamic information in log messages using placeholders.
# Example:
     name = 'John'
     logger.info('User %s logged in', name)

# Step 7: Handle exceptions with logging:
# Logging can help you capture and report exceptions within your code.
# Example:
     try:
         # Some code that may raise an exception
     except Exception as e:
         logger.exception('An error occurred: %s', e)

# Step 8:  Close the logger (optional):
# If you have finished using the logger, you can close it to release any resources.
# Example:
     logging.shutdown()

# Remember to import the logging module in any modules where you want to use logging.

# Logging Levels:
# The logging module provides several predefined levels to categorize log messages based on their severity. These levels help you control which messages are displayed or recorded.

import logging

# Set up logging configuration
logging.basicConfig(level=logging.WARNING)

# Create a logger object
logger = logging.getLogger()

# DEBUG level
logger.debug("This is a debug message")

# INFO level
logger.info("This is an informational message")

# WARNING level
logger.warning("This is a warning message")

# ERROR level
logger.error("This is an error message")

# CRITICAL level
logger.critical("This is a critical message")


# Example:

# Building Logger
# Importing Logging Module
import logging

# Build and config logger
# Configure the logger to write logs to a file named "main.log"
# Set the log message format to include the timestamp and the message itself
# Use filemode "w" to overwrite the existing log file on each run
logging.basicConfig(filename="main.log", format="%(asctime)s %(message)s", filemode="w")

# set an object for the logger
# Create a new logger object
new_logger = logging.getLogger()

# set threshold to debug
# Set the logging threshold level to DEBUG
# This means all log messages with a severity level of DEBUG and above will be recorded
new_logger.setLevel(logging.DEBUG)

# Messages for that log
# Generate log messages using different severity levels

# DEBUG level log message
new_logger.debug("This is a harmless debug message")

# INFO level log message
new_logger.info("Information Message")

# WARNING level log message
new_logger.warning("A warning Message")

# ERROR level log message
new_logger.error("An error Message")

# CRITICAL level log message
new_logger.critical("No Internet, Internet is down now")



