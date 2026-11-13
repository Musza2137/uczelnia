"""
A program that calculates the distance to the horizon
from a height given in meters from the keyboard.

i. Height 1.78 m -> distance: 4.76 km
ii. Height 20 m -> distance: 15.97 km
"""

import math

h = float(input("Enter height in meters: "))
d = 3.57 * math.sqrt(h)
print("Distance to the horizon:", d, "km")
