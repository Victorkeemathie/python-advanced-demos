import time
# Title: Working with Python Date Object
# Explanation: Python provides the 'time' module to work with date and time-related functionality.
# Example 1: Getting the current time in seconds since epoch (Jan 1, 1970, 00:00:00)
current_time = time.time()
print("Current time in seconds since epoch:", current_time)

# Example 2: Getting the current time as a string
current_time_string = time.ctime()
print("Current time:", current_time_string)

# Example 3: Suspending execution of code for a specified number of seconds
print("Start")
time.sleep(2)  # Suspends code execution for 2 seconds
print("End")

# Example 4: Converting seconds to a date and time using localtime()
seconds_since_epoch = time.time()
local_time = time.localtime(seconds_since_epoch)
print("Local time:", local_time)

# Example 5: Accessing specific components of the struct_time object
year = local_time.tm_year
print("Year:", year)

from datetime import date, time, timedelta, datetime
# Title: Working with the datetime module
# Explanation: The 'datetime' module provides classes and methods for working with dates and times in Python.
# Example 1: Working with the date class
custom_date = date(2023, 6, 9)  # Creating a custom date object
print("Custom date:", custom_date)
today_date = date.today()  # Getting the current date
print("Today's date:", today_date)

# Example 2: Working with the time class
custom_time = time(15, 30, 45)  # Creating a custom time object
print("Custom time:", custom_time)

# Example 3: Working with the timedelta class
delta = timedelta(days=7)  # Creating a timedelta object representing a duration of 7 days
print("Timedelta:", delta)

# Example 4: Working with the datetime class
current_datetime = datetime.now()  # Getting the current date and time
print("Current datetime:", current_datetime)

# Explanation:
from time import time, ctime, sleep, localtime
# Importing specific functions and classes from the 'time' module
# - 'time': Function that returns the current time in seconds since epoch
# - 'ctime': Function that returns the current time as a string
# - 'sleep': Function that suspends the code execution for a specified number of seconds
# - 'localtime': Function that converts seconds into a date and time representation

from datetime import date, time, timedelta, datetime
# Importing specific classes and functions from the 'datetime' module
# - 'date': Class that represents a date (year, month, day)
# - 'time': Class that represents a time (hour, minute, second, microsecond)
# - 'timedelta': Class that represents a duration or difference between two dates or times
# - 'datetime': Class that represents a combination of date and time

import time
# Importing the entire 'time' module
# This allows you to use other functions and classes available in the 'time' module as well

# Date Object Examples:
# 1. Python program to display different Date Time formats
from datetime import datetime
# Get the current date and time
current_datetime = datetime.now()
# Display different formats of the current date and time
print("Current Date and Time:")
print("Format 1:", current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
print("Format 2:", current_datetime.strftime("%d/%m/%Y %H:%M:%S"))
print("Format 3:", current_datetime.strftime("%A, %B %d, %Y %H:%M:%S"))

# 2. Python program to display current date and time
from datetime import datetime
# Get the current date and time
current_datetime = datetime.now()
# Display the current date and time
print("Current Date and Time:", current_datetime)

# 3. Python program to get current time in milliseconds
importtime

# Get the current time in milliseconds
current_time_milliseconds = int(time.time() * 1000)
# Display the current time in milliseconds
print("Current Time in Milliseconds:", current_time_milliseconds)

# 4. Python program to determine whether a specific year is a leap year or not
import calendar
# Specify the year to check
year = 2024
# Check if the year is a leap year
is_leap = calendar.isleap(year)
# Display the result
if is_leap:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

# 5. Python program to find age and convert it into years, months, days, hours, minutes, seconds, etc.
from datetime import datetime
# Get the birthdate
birthdate = datetime(1990, 5, 20)
# Get the current date and time
current_datetime = datetime.now()
# Calculate the age
age = current_datetime - birthdate
# Display the age in years, months, days, hours, minutes, and seconds
print("Age:", age)
print("Years:", age.days // 365)
print("Months:", (age.days % 365) // 30)
print("Days:", age.days % 30)
print("Hours:", age.seconds // 3600)
print("Minutes:", (age.seconds % 3600) // 60)
print("Seconds:", age.seconds % 60)

# 6. Python program to find the number of days between two dates
from datetime import date
# Specify the two dates
date1 = date(2023, 6, 1)
date2 = date(2023, 6, 10)
# Calculate the number of days between the two dates
delta = date2 - date1
num_days = delta.days
# Display the result
print("Number of days between", date1, "and", date2, "is", num_days)

# 7. Python program to display yesterday, today, or tomorrow
from datetime import datetime, timedelta
# Get the current date
current_date = datetime.now().date()
# Calculate the previous day, current day, and next day
previous_day = current_date - timedelta(days=1)
next_day = current_date + timedelta(days=1)
# Display the result
print("Yesterday:", previous_day)
print("Today:", current_date)
print("Tomorrow:", next_day)

# 8. Python program to display the previous 10 days starting from today
from datetime import datetime, timedelta
# Get the current date
current_date = datetime.now().date()
# Calculate the previous 10 days
for i in range(10):
    previous_day = current_date - timedelta(days=i+1)
    print(previous_day)

# 9. Python program to subtract 10 seconds from the current time
from datetime import datetime, timedelta
# Get the current time
current_time = datetime.now().time()
# Subtract 10 seconds
new_time = (datetime.combine(datetime.today(), current_time) - timedelta(seconds=10)).time()
# Display the result
print("Current Time:", current_time)
print("New Time:", new_time)

# 10. Python program to display the week number for a specific date
from datetime import date
# Specify the date
date = date(2023, 6, 1)
# Get the week number
week_number = date.isocalendar()[1]
# Display the week number
print("Week Number:", week_number)

# 11. Python program to select all the Mondays from a specified year
import calendar
# Specify the year
year = 2023
# Get the calendar for the specified year
cal = calendar.Calendar()
# Iterate over each month in the year
for month in range(1, 13):
    # Iterate over each day in the month
    for day in cal.itermonthdays2(year, month):
        # Check if the day is Monday (weekday 0)
        if day[0] == 0 and day[1] != 0:
            print(calendar.month_name[month], day[1])
            
from time import time, ctime, sleep, localtime
from datetime import date, time, timedelta, datetime

# Time Module
current_time = time()  # Get current time in seconds since epoch
print("Current time:", current_time)

current_time_string = ctime()  # Get current time as a string
print("Current time string:", current_time_string)

current_year = localtime().tm_year  # Get the current year
print("Current year:", current_year)

sleep(10)  # Sleep for 10 seconds
print("10 seconds passed")

# DateTime Module
custom_date = date(2023, 6, 9)  # Create a custom date object
print("Custom date:", custom_date)

today_date = date.today()  # Get the current date
print("Today's date:", today_date)

current_month = today_date.month  # Get the month of the current date
print("Current month:", current_month)

custom_time = time(10, 23, 24, 411)  # Create a custom time object
print("Custom time:", custom_time)

current_datetime = datetime.now()  # Get the current date and time
print("Current datetime:", current_datetime)

timedelta_obj = timedelta(days=4, weeks=3, hours=23, microseconds=2432, milliseconds=2939)  # Create a timedelta object
print("Timedelta:", timedelta_obj)

change = timedelta(days=4, weeks=3, hours=23) + current_datetime  # Perform timedelta calculation
print("Change:", change)
