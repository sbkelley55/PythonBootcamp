# -*- coding: utf-8 -*-
"""
Spyder Editor

Here are some examples of functions 
Functions are very useful - we can create blocks of code that we want to 
execute on demand whenever we need without having to re-type everything

"""
# Here is a simple function, based on recent events
def truth():
    print ('Maroon 5 may have just taken')
    print ('the mantle of harassment')
    print ('from Nickelback after that halftime show')
    
truth()


# Note some things about the architecture here
# You need the def statement, a name, and then parameters (as needed)
# You often will want to return values for these, as you're often passing
# them off to be used later.  A more relevant example below

x = [10,15,3,4,11,15]
y = [2,20,3,6,7,22]

# xvals, yvals - parameters
def get_means(xvals,yvals):
    xcoords = sum(xvals)/len(xvals)
    ycoords = sum(yvals)/len(yvals)
    return xcoords,ycoords

# x,y - arguments
vals = get_means(x,y)
print ('The mean center is: ' '%.1f' % vals[0],',',vals[1])

# Standard Distance Function 
# First example of calling a library that isn't already loaded
import math

def getsd(xvals,yvals):
    meanx = sum(xvals)/len(xvals)
    meany = sum(yvals)/len(yvals)
    evalx = []
    evaly = []
    for i in xvals:
        xl = (i-meanx)**2
        evalx.append(xl)
    for i in yvals:
        yl = (i-meany)**2
        evaly.append(yl)
    z = math.sqrt((((sum(evalx)/len(evalx)) + (sum(evaly)/len(evaly)))))
    return z

sd = getsd(x,y)
print ('The mean center is: ' '%.2f' % sd)
        