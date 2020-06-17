'''
I want to be able to print the area of a circle.
Ideally, I want to print only to the third decimal place.
'''

import math

radius = 3

print(math.pi * radius * radius)

print(f"The area of the circle is {math.pi * radius * radius:.3f}")

'''
Matt's question in help channel:

How to print a floating point number to the third decimal place in python?
import math
radius = 3
print(math.pi * radius * radius)
I am trying to print the area of a circle, but I only want the area to the third decimal place.
Currently, I am getting the following printed to my terminal:
28.274333882308138
Help, please? :please_minion:
'''
