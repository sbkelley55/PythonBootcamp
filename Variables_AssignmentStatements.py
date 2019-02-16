# -*- coding: utf-8 -*-
"""
Variables, Assignment Statements
"""
# If you want to check your current working directory, enter this command
import os
cwd = os.getcwd()
print (cwd)
# If you ever need to change your working directory, you can refer back to this
# and do so as follows - no need to now in this workshop, but it may come up 
# in your future work
os.chdir('set the directory here')

# Data Basics - Constants

# You can set a constant value that is assigned to a variable, as follows
# Numeric Constants are entered by entering either float or integer data

# Print statements are also your friends - they report what's happening
# at certain points in your code, report outputs for users, and 
# they help you diagnose what's going on in your code wherever you like.  
# In 3.x, they require parenthesis, but this is not the case with 2.7
# So, if you're using arcpy/Python 2.7, you can say 
####  print my_var ####
#per below

my_var = 2
print (my_var)

my_other_var = 2.5
print (my_other_var)

# You can call a constant that is a string - these are designated
# by EITHER single or double quotes

true = "This is the best way to spend a Saturday"
alsotrue = 'This is the best way to spend a Saturday'

# You can work with different data types in print statements. Commas can be used
# to separate values, but this does carry consequences
print (true,alsotrue)
print (alsotrue,".", my_var, "times as much fan as anything else I would be otherwise doing today.")
print (alsotrue, " " true) # Good editors will catch syntax errors like this for you
# This might look better, but requires a conversion
print (alsotrue + ". " + str(my_var) + " times as much fan as anything else I would be otherwise doing today.")

# The operation above involved concatenation of strings in a print statement :
print (true + ". " + alsotrue)

# A variable, of course, is a named place in memory where we
# store data and later retrieve the data using the variable asssigned name
# You can call the variable whatever you want, but choose a name that makes sense
# However, variables must start with a letter or underscore
# They also are case-sensitive
# Don't use Python's reserved words either (if, else, and, etc.)

x = 2
X = 3

print (x, X)
# Python does get fussy about concatenating string and numeric data
print (x + "," + X)
# But you can convert between data types if you want to concatenate, as above
print (str(x) + ", " + str(X))
y = (str(x) + ", " + str(X))

# You can also overwrite existing variable values
x = 2
x = x * 5
print (x)

# You can assign multiple variable names at once:
a, b, c = 'Nirvana', 'Pearl Jam', 10

# Right-hand side is an experession - once evaluated, will be assigned to variable
x = 5
x = 17*3*(1-x)
x







