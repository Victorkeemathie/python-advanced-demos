# The collections ".namedtuple function" is a factory that builds subclasses of tuple enhnaced with field names, a class name, and an informative _repr_
# Example: how we could define a named tuple to hold information about a city:
from collections import namedtuple  # Importing the namedtuple class from the collections module

city = namedtuple('City', 'name, country, population, coordinates')  # Creating a named tuple class called 'City' with fields: name, country, population, coordinates

tokyo = city('Tokyo', 'JP', 36.933, (35.68922, 139.691667))  # Creating an instance of the 'City' named tuple class called 'tokyo' with the provided values

tokyo  # Output: City(name='Tokyo', country='JP', population=36.933, coordinates=(35.68922, 139.691667))

tokyo.population  # Output: 36.933

tokyo.coordinates  # Output: (35.68922, 139.691667)

city._fields  # Output: ('name', 'country', 'population', 'coordinates') - Returns the field names of the 'City' named tuple class

delhi_data = ('Delhi NCR', 'IN', 21.935, Coordinate(28.613889, 77.208889))  # Creating a tuple called 'delhi_data' with the provided values

delhi = city._make(delhi_data)  # Creating an instance of the 'City' named tuple class called 'delhi' using the '_make' method and passing 'delhi_data' as arguments

delhi._asdict()  # Output: {'name': 'Delhi NCR', 'country': 'IN', 'population': 21.935, 'coordinates': Coordinate(lat=28.613889, lon=77.208889)} - Returns the named tuple as an OrderedDict

import json  # Importing the json module

json.dumps(delhi._asdict())  # Output: '{"name": "Delhi NCR", "country": "IN", "population": 21.935, "coordinates": {"lat": 28.613889, "lon": 77.208889}}' - Serializes 'delhi._asdict()' into a JSON formatted string


# Two parameters are required to create a named tuple: a class name. and, a list of fields, which can be given iterable of strings or as a single space-delimited sttring
# Field values must be passed as seperate positionaö arguments to the constructor(in contrast, the tuple constructor takes a singöe iterable)
# You can access the fields by name or position
# As a tuple subclass, City inherits useful methods such as _eq_ and the special methods for comparison operators - including _it_ which allows sorting lists of City instances
# ._fields is a tuple with field names of the class
# ._make() builds City from an iterable; City(*delhi_data) would do the same
# ._asdict() returns a dict built from the named tuple instance
# a_asdict() is useful to serialize the data in JSON format, for example


from collections import namedtuple  # Importing the namedtuple class from the collections module

Coordinate = namedtuple('Coordinate', 'lat lon reference', defaults=['WGS84'])
# Creating a named tuple class called 'Coordinate' with fields: lat, lon, reference.
# The 'defaults' argument is used to set a default value for the 'reference' field, which is 'WGS84'.

Coordinate(0, 0)
# Output: Coordinate(lat=0, lon=0, reference='WGS84')
# Creating an instance of the 'Coordinate' named tuple class called 'Coordinate' with the provided values.
# Since the 'reference' field is not provided, it takes the default value of 'WGS84'.

Coordinate._field_defaults
# Output: {'reference': 'WGS84'}
# Accessing the '_field_defaults' attribute of the 'Coordinate' named tuple class.
# This returns a dictionary with the field names as keys and their default values (if any) as values.

# Example 2:
from collections import namedtuple  # Importing the namedtuple class from the collections module

Point_2d = namedtuple('Point_2D', ['x', 'y'])
# Creating a named tuple class called 'Point_2d' with fields: x, y

new_point = Point_2d(50, 100)
# Creating an instance of the 'Point_2d' named tuple class called 'new_point' with the provided values

print(new_point)
# Output: Point_2D(x=50, y=100)
# Printing the 'new_point' named tuple instance

print(isinstance(new_point, Point_2d))
# Output: True
# Checking if 'new_point' is an instance of the 'Point_2d' named tuple class using the 'isinstance' function

print(isinstance(new_point, tuple))
# Output: True
# Checking if 'new_point' is an instance of the built-in 'tuple' class using the 'isinstance' function

x, y = new_point
print(f"{x}, {y}")
# Output: 50, 100
# Unpacking the values of 'new_point' into variables 'x' and 'y' and then printing their values

x = new_point[0]
y = new_point[1]
print(f"{x}, {y}")
# Output: 50, 100
# Accessing the values of 'new_point' using indexing and assigning them to variables 'x' and 'y', and then printing their values

for item in new_point:
   








