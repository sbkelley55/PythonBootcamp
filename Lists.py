# -*- coding: utf-8 -*-
"""
List Data Examples and Operations - sbkelley

"""
# List Data are NOT immutable, unlike string data
testlist = [10,11,13,7,8,3]
print (testlist)
testlist[2] = 14
print (testlist)

# Lists are collections of items - we can put many values in a single variable
dmb = ['dave','tim','leroy','carter','steffan','boyd']
# Lists are surrounded by square brackets, elements in list separatedd by commas
# Can include a mixture of data types
dmbsongs = ['crush', 41,'too much', 'grace is gone','two step']
dmbsongs2 = [[41,'too much','twostep'],['crush','stone','rapunzel'],'grace is gone',(1991,2018)]
# List elements and subelements and be accessed as follows:
print (len(dmbsongs2))
print (len(dmbsongs2[0]))
print (list((range(len(dmbsongs2)))))

for i in dmb:
    print ('Band member:', i)
    
for i in range(len(dmb)) :
    dm = dmb[i]
    # Can we have this count start at 1 instead?  
    print ('Band member:', i, dm)

a = [10,11,13,7,8,3]
b = [17,10,5,4,9,15]

# Concatenating lists
c = a + b
print (c)
  
# List slicing work similarly to string slicing - use index valuess
print (c[1:4])
print (c[5:])

# Review the allowable operations for lists
dir(dmb)

# Here is a major tool in your toolkit and it's made some 
# appearance already - setting an empty list, which you add items to
mylist = []
# Another way
myotherlist = list()
# Now add elements to it. They will stay in the order in which they are added
# New elements go to the end of the list
myotherlist.append('Ants Marching')
myotherlist.append(41)
# Test whether an item is there, but won't modify
41 in myotherlist
41 not in myotherlist

# There are a number of built-in functions that apply to lists
print (len(c))
print (max(c))
print (min(c))
print (sum(c))
print (sum(c)/len(c))

# Working with lists
NVPopulations2017 = [54745,24230,2204079,48309,52649,850,1961,16826,5693,5223,54122,4457,44202,6508,4006,460587,9592]
NVCounties = []
NVcounties = " Washoe, Clark, Lyon, Carson City, Pershing, Douglas, White Pine, Nye, Humboldt, Lincoln, Esmeralda, Mineral, Elko, Storey, Eureka, Churchill, Lander"
# Note the use of a delimeter here - without specifying one, the default is a space
# And multiple spaces are still treated as one delimeter
NVList = NVcounties.split(",")
NVList.sort()

# Add items to an empty list
for i in NVList:
    x = i.strip()
    NVCounties.append(x)
print ("In List Form(!) - that's Nevada!", NVCounties)

# A more compact way to add items to a list
NVCounties2 = [i.strip() for i in NVList]


# Setting counters with lists
total = 0
count = 0
while True :
    inp = input('Enter a number: ')
    if inp == 'done' : break
    forassess = float(inp)
    total = total + forassess     
    count = count + 1

average = total / count
print ('Average:', average)



