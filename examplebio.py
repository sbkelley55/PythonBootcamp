# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 16:18:38 2019

@author: UNR Math Stat
"""

import pandas
import numpy
import math
from matplotlib import pyplot
from statsmodels.graphics.gofplots import qqplot
import scipy

df = pandas.read_csv('biodata.csv')
data = df.values

print(data[0][0])

NOBSERV = numpy.size(data, 0)
print(NOBSERV)#quantity of patch-year data points

patch = data[:,0]#ID of patch
year = numpy.array([int(data[k,1]) for k in range(NOBSERV)])#years
biomass = data[:,2]
shadow = data[:,3]
value = shadow #this is what we consider now: biomass or shadow

Logvalue = numpy.array([math.log(item) for item in value]) #log scale 

yearLogvalue = [Logvalue[year == k] for k in range(1970, 2010)]#logvalue for current year
#Note how we select among Logvalue elements those with year k+1970


print('mean = ', numpy.mean(yearLogvalue[10]))#average log of shadow in patches observed in 1980 
print('size = ', numpy.size(yearLogvalue[10]))#quantity of patches observed in 1980
qqplot(yearLogvalue[10], line = 's')
pyplot.show()

logvalue = numpy.array([]) #here will be logarithms of value for steps
logchange = numpy.array([]) #increments of logarithms 
interval = numpy.array([]) #increments of years

#next loop collects records from the same patch: initial, change in logs, time interval
for observ in range(NOBSERV-1):
    if patch[observ] == patch[observ+1]:
        logvalue = numpy.append(logvalue, math.log(value[observ]))
        logchange = numpy.append(logchange, math.log(value[observ+1]) - math.log(value[observ]))
        interval = numpy.append(interval, year[observ+1] - year[observ])
       
NCHANGES = numpy.size(logvalue)  #quantity of patch-increment data points
print([numpy.count_nonzero([gap == k for gap in interval]) for k in range(40)])  
#quantity of patches with pairs of observations with interval k years, for k = 0, ..., 39

#testlogbiomass = logbiomass[interval == 5] 

pyplot.plot(logvalue[interval == 7], logchange[interval == 7], 'go')
pyplot.show()#log-log plot of value vs change for gaps of 7 years
print('Histogram')          
pyplot.hist(logchange[interval == 7], bins = 50) 
pyplot.show()#histogram of increments of logarithms for gaps of 7 years
print('QQ')
qqplot(logchange[interval == 7], line='s')#Q-Q plot of the same, to test normality
pyplot.show()
print('mean change for 5 years = ', numpy.mean(logchange[interval == 5]))
print('mean change for 10 years = ', numpy.mean(logchange[interval == 10]))
print('Linear regression of change over initial data for 7 year gap')
print(scipy.stats.linregress(logvalue[interval == 7], logchange[interval == 7]))
#since the second quantity is not 2*the first one, the data is time inhomogeneous