# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 09:34:10 2019

@author: sbkelley
Census Data Assignment
"""

from census import Census
#from us import states

# You'll have to install the census package if you don't have it
# 'conda install -c conda-forge census'

Washoe = '031'

#Question - what does the 'E' stand for in the table name
c = Census("7e8401ce249220dcba1ef497a3903ced266c772f")
WashoeTractBike = c.acs.state_county_tract('B08006_014E', 32, Washoe, Census.ALL)
WashoeTractWalk = c.acs.state_county_tract('B08006_015E', 32, Washoe, Census.ALL)

def WalkTotalByTract(walkdata):
    WashoeWalk = []
    for i in walkdata:
        z = list(i.items())
        WalkByTract = z[0][1]
        WashoeWalk.append(WalkByTract)
    return WashoeWalk

def BikeTotalByTract(bikedata):
    WashoeBike = []
    for i in bikedata:
        z = list(i.items())
        BikeByTract = z[0][1]
        WashoeBike.append(BikeByTract)
    return WashoeBike

Walk=WalkTotalByTract(WashoeTractWalk)
Bike=BikeTotalByTract(WashoeTractBike)

print ("The total sum (by tract) of those who walk to work in Washoe County is:", sum(Walk))
print ("The total sum (by tract) of those who bike to work in Washoe County is:", sum(Bike))

import matplotlib.pyplot as plt

n, bins, patches = plt.hist(Walk,10,density=0,facecolor='blue',alpha=0.75)
plt.xlabel('# Commuters')
plt.ylabel('Count - Census Tracts')
plt.title('Frequency Distribution of Commuters')
plt.grid(True)





    
    
