# -*- coding: utf-8 -*-
"""
Working With Integer and Float Data
"""

# Python does have some considerations with these data types
# First, it works under the PEMDAS workflow
# Second, here are your operators

# +, -, *, /, **, %
# addition, subtraction, multiplication, division, exponent, remainder
a = 5 + 11 ** 2 / (3 * 5)
print (a)

remain = 20 % 3
print (remain)

# Use parenthesis to your advantage to head off a potential soruce of logical error

# Be aware that in Python 2.7, integer division produces an integer:
# e.g., 10/3 = 3. This changed in 3.x. You can change to an integer if you want
print (10/3)
d = (10/2)
int(d)

x = 11/7
type(x) # The type function is helpful to use to assess data type, and therefore, allowable operations
print (str(x)) # You can convert, but it may not look great
print ('%.1f' % x) # This is a string formatting operator
# Another version
print ('%.3f' % x)

# Addition, subtraction, and multiplication of integers produce integers, though
y = 4 + 7
type(y)
z = 4 * 7
type (z)

# You can also get user input as follows using the input function
x = input('Enter an elevation in meters:')
feet = int(x) * 3.28084
print ('Feet: ' '%.1f' % feet)

############  
# Accessing Index Values
###########

# This is a pretty handy way to get at elements within data

x = 'This is my sentence'

print (x[0]) # This index position is the first in the ordered sequence
print (x[-1]) # This gets at the last value
print (x[4]) # Note that any character counts, including spaces

# You can also call a range of values
print (x[0:4]) # Of note - the upper boundary is NOT included in the return
print (x[-8:-1]) # That matters when accessing logical sequences
print (x[-8:]) # That's better - this includes all characters past the 'slice'
print (x[:4]) # Same in the other direction

# You can also couple these with some basic definite loops:
# Keep this in mind re: string data
for i in x:
    print (i)
    
# Now with a different data type - lists, which we'll review more in a bit
NV = ['Reno','Sparks','Hawthorne','Carson City']
for i in NV:
    print (i)
print (NV[0])
print (NV[-1])

    






