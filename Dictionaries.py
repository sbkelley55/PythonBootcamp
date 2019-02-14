# -*- coding: utf-8 -*-
"""
Working with Dictionaries in Python - sbkelley
"""

# Dictionaries are a common format you'll see when accessing data from
# external locations. It allows us to store multiple types of values with a 
# single object. Lists do that, too, but they are always accessed sequentially
# Dictionaries contain a label for a value or values

# Some have argued that Dictionaries are Python's most powerful data collection
# They allow us to index and access values quickly

# In lists, there is an index that is based on the position in the list,
# But in dictionaries, there isn't necessarily an order, the index is made
# in a dictionary with a "lookup tag" - they use keys instead of numbers

mtns = dict()
mtns['elevation'] = 7533
mtns['prominence'] = 1813
print (mtns)
mtns['prominence'] = 1853
print (mtns)
#Can also create a new one by:
mtns = {}

# You'll see that dictionaries use {} as designators, and use a key:value pair
gc_summits = {'brahma temple': 7551,'vishnu temple': 7533, 'coronado butte': 7110}

# Searching for items in dictionaries
print ('vishnu temple' in gc_summits)
print ('temple' in gc_summits)

# Accessing items in dictionaries with definite loops
# Two iteration variables to print (key,value) pairs
for i,j in gc_summits.items():
    print (i,j)

# You can convert to list, but with some additional considerations 
list(gc_summits)
# Access items in a dictionary
print (gc_summits.keys())
print (gc_summits.values())
# You will see this generates tuples (key,value)
print (gc_summits.items())

# Populating a dictionary with counts. Here, the 'team' is the key, and values will be the counts
SBcounts = dict()
SB_Since_2010 = ['New Orleans','Green Bay','New York Giants','Baltimore','Seattle','New England','Denver','New England','Philadelphia','New England']
for team in SB_Since_2010:
    if team not in SBcounts:
        SBcounts[team] = 1
    else:
        SBcounts[team] = SBcounts[team] + 1
print (SBcounts)
# Gross, isn't it? Unless you're a Patriots fan

# Using the .get() command to accomplish the same  This assumes a default vlaue of zero if key 
# isn't in dictionary, then adds per occurrence
SBcounts = dict()
SB_Since_2010 = ['New Orleans','Green Bay','New York Giants','Baltimore','Seattle','New England','Denver','New England','Philadelphia','New England']
for team in SB_Since_2010 :
    SBcounts[team] = SBcounts.get(team, 0) + 1
print (SBcounts)

NVcounties = " Washoe, Clark, Lyon, Carson City, Pershing, Douglas, White Pine, Nye, Humboldt, Lincoln, Esmeralda, Mineral, Elko, Storey, Eureka, Churchill, Lander"
NVPopulations2017 = [54745,24230,2204079,48309,52649,850,1961,16826,5693,5223,54122,4457,44202,6508,4006,460587,9592]
NVList = NVcounties.split(",")
NV = [i.strip() for i in NVList]
NV.sort()

# Set unique ID key for NV counties, sorted alphabetically
# The i+1 ensures that the ID starts at 1, not 0
dictNV = {i+1 :NV[i] for i in range (0,len(NV))}

# Converted a zipped object to a dictionary
zipNV = zip(NV,NVPopulations2017)
dictNVPop = dict(zipNV)

# Sort by descending order of population, by accessing the Values
# The lambda function passes a key function that returns the element 
# in position [1] - in our case, the population value, reverse=true ensures descending order
sorted(dictNVPop.keys())   
CountyTuples = sorted(dictNVPop.items() , reverse=True, key=lambda x: x[1])
for county in CountyTuples:
    print(county[0],county[1]) 
    
# Now we can query this as needed - what's the population of Mineral County?
dictNVPop['Mineral']

# You can add items to a dictionary pretty readily. 
# I think this population count is pretty close to accurate...
dictNVPop['Black Rock City'] = 60000






    
