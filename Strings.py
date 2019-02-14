# -*- coding: utf-8 -*-
"""
String Data Examples and Operations - sbkelley
"""

# String Data are immutable - that means we can't change them (can't change contents)
# We have to create a new string to make changes

# Working with string data - starting with southern Arizona's iconic mountain
mountain = 'Baboquivari'

# Some classic shots of it - and a hint at opening a web browswer at a certain location
import webbrowser
EastSide = webbrowser.open('https://hikearizona.com/photo.php?ZIP=91669')
WestSide = webbrowser.open('https://www.mountainproject.com/photo/109613206')
# See, pretty cool mountain, isn't it?  Onwards...

# Let's have a website that already stores its elevation and 
# name and read those values as strings. 
# This is an example of simple "web scraping"
import urllib.request
from bs4 import BeautifulSoup

peak_page = 'https://www.peakbagger.com/peak.aspx?pid=4157'
page = urllib.request.urlopen(peak_page)

soup = BeautifulSoup(page, 'html.parser')
find_elev = soup.find('h2')
find_name = soup.find('h1')

ElevValue = find_elev.text.strip()
NameString = find_name.text.strip()

print (ElevValue)
print (NameString)

############################################################

#Or, as my wife calls it
notitsname = NameString[0:4]
print (notitsname)

#Enter this command in interactive mode to see the string library
dir(NameString)

# Use the find command
pos = NameString.find('qu')
print (pos)

aa = NameString.find('bq')
print (aa)

# Using the strip function to remove whitespace
bestmountain = '   Baboquivari Peak  '
print (bestmountain.lstrip())
print (bestmountain.rstrip())
print (bestmountain.strip())

# Download an unnecessarily long string - or a whole lot of them? Use .find()
# In this case, if a large list of peaks were read, and each had their elevation
# values after a hyphen and before the first space, this would be powerful
peakrecord = 'BaboquivariPeak-7748 Sat Oct 14th 2014'
hyphen = peakrecord.find('-')
print (hyphen)
space = peakrecord.find(' ',hyphen)
print (space)
elev = peakrecord[hyphen+1 : space]
print (elev)

# Escape Characters - use the \"(string)\"
# sequence to include the quotes as part of the string
print("Baboquivari is considered the \"hardest\" mountain to climb in the state")
# Add a new line character
print ("Baboquivari is not easy \n but perhaps not the \"hardest\" mountain to climb in the state")
# Adding a tab
print ("Baboquivari is not easy \n \t but perhaps not the \"hardest\" mountain to climb in the state")

# Using Format Characters - this may be a harder objective than Baboquivari
print ('Mountain Name: %s,\nElevation: %d feet,\nDifficulty(Class): %.1f' % ('Brahma Temple',7551, 4.0))
# using Format Characters - passing in variables
mtn_name = 'Brahma Temple'
Elevation = 7551
YDS = 4.0
print ('Mountain Name: %s,\nElevation: %d feet,\nDifficulty(Class): %.1f' % (mtn_name, Elevation, YDS))

# String comparisons - Conditional Evaluations
print (mtn_name.islower())
print (mtn_name.isupper())

# Formatting - justification
print (mtn_name.rjust(25,'-'))
print (mtn_name.ljust(25,'-'))
print (mtn_name.center(25,'-'))

# Some of the commands you can use on string data create different data types
y = 'I am having good times today'
newy = y.split()
print (newy)
######
# Experiment a bit - refer back to the definite loop example in
# Integer_FloatData.py
# How would you create an output that would print out each word and its length?
# Hint - check out the len() built-in function

