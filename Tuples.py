# -*- coding: utf-8 -*-
"""
Working with Tuple Data - sbkelley

"""

# Tuples are another common data type, and really well-suited to geographic data storage,
# Especially when storing (x,y) coordinate pairs. Their uses of course extend beyond that

# Tuples are readily identifiable with the () designations,
# while lists are designated by []

# Like lists, they are a sequence of elements and can be indexed starting from pos 0

CarsonRange = ('Rose','Houghton','Tamarack','Relay')
print(CarsonRange[1])
CarsonRange.index('Rose')

# Those all look familiar, but here is the difference:
# Tuples are immutable - meaning you cannot alter them (like strings)
CarsonRange = ('Rose','Houghton','Tamarack','Relay')
CarsonRange[2] = 'Snowflower'
# This line will trip an error message

# Some of the functions we love with lists are not usable here
# .sort(), .append() won't work - the list of allowable operations is shorter
# You'll see only .count(), and .index() as available

# So - why use them?  For one, they aren't modifiable, so that makes them
# simpler, and require less memory to store

# Tuples can be set in the same way as variable names
(a,b,c,d) = ('Rose','Houghton','Tamarack','Relay')
print (b)

# They can be found within dictionaries
dCarsonRange = dict()
dCarsonRange['Tamarack']=9897
dCarsonRange['Rose']=10776
dCarsonRange['Relay']=10338
dCarsonRange['Houghton']=10490

TopFourWashoe = list(dCarsonRange.items())
print (TopFourWashoe)
SortedTopFour = sorted(dCarsonRange.items())

import numpy

# Working with a list of tuples - lat/long coordinate pairs
latlongpairs = [(-119.453,35.9563),(-118.7845,35.34565),(-116.3453,36.7532)]

long = []
lat = []
for i in latlongpairs:
    print (i)
    long.append(i[0])
    lat.append(i[1])
# Then call the lists
numpy.mean(long)
numpy.mean(lat)

# Then put them back together
latlong_again = zip(long,lat)
for i in latlong_again:
    print (i)







