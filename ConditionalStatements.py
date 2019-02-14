# -*- coding: utf-8 -*-
"""
Flow Control Example
This program evaluates population changes at the county level in Nevada,
after a simple example first
"""

# Simple Flow Control
x = input('Enter your favorite number:')
if float(x) < 5:
    print ('Go bigger or go home')
elif float(x) < 10:
    print ('Getting better')
else:
    print ('In Double Digits - well done')
    
###

# List of Nevada County Names - unsorted"
NVcounties = " Washoe, Clark, Lyon, Carson City, Pershing, Douglas, White Pine, Nye, Humboldt, Lincoln, Esmeralda, Mineral, Elko, Storey, Eureka, Churchill, Lander"
NVList = NVcounties.split(",")
NVList.sort()
print (NVList)
# Nice trick for getting rid of leading spaces
NVList = [i.strip() for i in NVList]
print (NVList)

Clark = NVList[2]
Washoe = NVList[-2]

#2017 Population Estimates - ACS
NVPopulations2017 = [54745,24230,2204079,48309,52649,850,1961,16826,5693,5223,54122,4457,44202,6508,4006,460587,9592]
#2010 Population - 2010 US Census
NVPopulations2010 = [55274,24822,1951269,46997,48818,783,1987,16528,5775,5345,51980,4772,43946,6753,4010,421407,10030]

ClarkPop17 = NVPopulations2017[2]
WashoePop17 = NVPopulations2017[-2]
ClarkPop10 = NVPopulations2010[2]
WashoePop10 = NVPopulations2010[-2]

print (Clark.strip() + " " + "County Population (2010): ", ClarkPop10)
print (Washoe.strip() + " " + "County Population (2010): ", WashoePop10)
print (Clark.strip() + " " + "County Population (2017): ", ClarkPop17)
print (Washoe.strip() + " " + "County Population (2017): ", WashoePop17)

# Can you clean up the presentation of these average Nevada County Populations??
print ("The average Nevada County Population in 2010 was:", sum(NVPopulations2010)/len(NVPopulations2010))
print ("The average Nevada County Population in 2017 was:", sum(NVPopulations2017)/len(NVPopulations2017))

NVPopChange = zip(NVList, NVPopulations2017, NVPopulations2010)
print (NVPopChange)

# Carson City actually isn't a true "County" - see if you can add something to address this:
 
for i in NVPopChange:
    if i[1] > i[2]:
        print (i[0],'County gained',i[1]-i[2],"residents")
    else:
        print (i[0],'County lost',i[2]-i[1],"residents")


