# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 16:54:25 2019

@author: UNR Math Stat
"""

import numpy
import pandas
from matplotlib import pyplot
import math
from scipy import stats

frame = pandas.read_csv('findata.csv')
dataframe = frame.set_index('Date')
data = dataframe.values


SP500index = data[:, 0]#S&P 500 index, inflation-adjusted
PEratio = data[:, 1]#Trailing price-to-earnings ratio for 1-year earnings
ShillerPEratio = data[:, 2]#Trailing price-to-earnings ratio with 10-year earnings, Shiller version
T = numpy.size(SP500index)#number of months
print('Number of months = ', T)
print('meanPE = ', numpy.mean(PEratio))
#mean for array with N/A values
print('meanShillerPE = ', numpy.nanmean(ShillerPEratio))

horizon = 60 #5 year horizon
Change = [math.log(SP500index[k+horizon]) - math.log(SP500index[k]) for k in range(T-horizon)]
#logarithm of month-to-month change
pyplot.hist(Change, bins = 50)#histogram
pyplot.show()
#plot of change vs PE ratio
pyplot.plot(Change, PEratio[:T-horizon], 'go')
pyplot.show()
#plot of change vs Shiller PE ratio
pyplot.plot(Change, ShillerPEratio[:T-horizon], 'ro')
pyplot.show()

#regression every 5 years, data cannot overlap
indep_steps = int(T/horizon)
sampled = PEratio[0::horizon]
print(stats.linregress(sampled[:-1], Change[0::horizon]))

#10Y = [math.log(SP500index[k+120]) - math.log(SP500index[k]) for k in range(T-120)]
#
#matplotlib.pyplot.hist(10Y, bins = 50)
#pyplot.show()
#
#matplotlib.pyplot.plot(10Y, PEratio[:T-120], 'go')
#pyplot.show()
#
#matplotlib.pyplot.plot(10Y, ShillerPEratio[:T-120], 'go')
#pyplot.show()



#print(data[:, 0])
#print(data[3, 4])




