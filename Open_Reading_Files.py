# -*- coding: utf-8 -*-
"""
Opening Files and Reading Data - sbkelley
"""

# The open() function is the basic ticket to reading in and accessing data
# This function returns a file handler

# Note - there are other more concise and advanced ways to do this, and you'll
# get your chance in Dr. Sarantsev's activities later, but let's start from the basics

# You'll need to point this file location to one on your directory
NVData = open("D:/Teaching/Nevada/PythonClass/NV_Cities.txt","r")

# Read the lines of the file to see its contents
# The output is a sequence of strings
linelist = []
for line in NVData:
    print (line)
    linelist.append(line)
print (linelist)

# Set a line read counter
NVData = open("D:/Teaching/Nevada/PythonClass/NV_Cities.txt","r")
counter = 0
for line in NVData:
    counter = counter + 1    
    print ('Line Count:', counter)

# Looping through lines helps to see what's there, but use the .read() command
NVData = open("D:/Teaching/Nevada/PythonClass/NV_Cities.txt","r")
NVdata = NVData.read()
# Each new line in the file is desginated by the \n character
NVDataSplit = NVdata.split('\n')
# Notice that it returns a single string
NVDataSplit[1]

# We can conditionally read in lines, too. This one gets at the first row
fhand = open("D:/Teaching/Nevada/PythonClass/NV_Cities.txt","r")
for line in fhand:
    if line.startswith('City') :
        print (line)

# Access the city names and put them in a list of their own 
#Use the 'r' - read command, then leverage what we know about the \n and \t characters
txtfile = open("D:/Teaching/Nevada/PythonClass/NV_Cities.txt","r")
cityname = []
for line in txtfile:
    sline = line.strip('\n')
    row = sline.split('\t')
    city = row[0]
    cityname.append(city)
cityname.pop(0)
print (cityname)

# Accessing csv files - note the change in delimeter
csvfile = open("D:/Teaching/Nevada/PythonClass/NVCities.csv","r")
citynamecsv = []
for line in csvfile:
    sline = line.strip('\n')

    # What would be the delimeter in this case?  Fill it in!
    
# Access the csv module for more functions specific to csv files
# Notice this is a bit more compact
import csv
with open("D:/Teaching/Nevada/PythonClass/NVCities.csv",newline='') as csvfile:
    cities = []
    NVreader = csv.reader(csvfile, delimiter=',')
    for line in NVreader:
        city = line[0]
        cities.append(city)
    cities.pop(0)
    print (cities)

# More elegantly(?)...but same output as above
import csv
cities = []
with open("D:/Teaching/Nevada/PythonClass/NVCities.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    RowNum = 0
    for line in reader:
        if RowNum >= 1:
            cities.append(line[0])
        RowNum = RowNum + 1
print (cities)
    
# Using the CSV writer
with open("D:/Teaching/Nevada/PythonClass/Other_Cities.csv", "r",newline='') as csvfile:
    NVwriter = csv.writer(csvfile, delimiter=',')
    NVwriter.writerow(['City','x','y','Pop'])
    NVwriter.writerow(['Ely',-114.8742,39.2533,3968])
    NVwriter.writerow(['Mesquite',-114.0672,36.8055,18541])
    NVwriter.writerow(['Fernley',-119.2518,39.6080,19863])
    NVwriter.writerow(['Fallon',-118.7770,39.4749,8409])

# Adding a new column to a .csv file and saving the output
import csv
with open("D:/Teaching/Nevada/PythonClass/Other_Cities.csv","r") as csvinput:
    with open("D:/Teaching/Nevada/PythonClass/test_output.csv", "w") as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        updatecity = []
        row = next(reader)
        row.append('State')
        updatecity.append(row)

        for row in reader:
            row.append('Nevada')
            updatecity.append(row)

        writer.writerows(updatecity)
