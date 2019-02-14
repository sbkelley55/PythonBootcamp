# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 09:34:10 2019

@author: sbkelley
Census Data Assignment
"""
# Add the census library - this is one you'll have to install as follows
# Open the conda terminal and enter 
# conda install -c conda-forge census
from census import Census

# Next, request an API Key from the US Census
# https://api.census.gov/data/key_signup.html
Washoe = '031'

#Question - what does the 'E' stand for in the table name
c = Census("Your Key Here - whatever the key was you received after your request")

# These table and keys come from the US Census Table Shell
# Full documentation here: https://api.census.gov/data/2017/acs/acs5/variables.html
# The first dataset are commmute totals by tract for bicycling, and the 
# second is for walking
WashoeTractBike = c.acs.state_county_tract('B08006_014E', 32, Washoe, Census.ALL)
WashoeTractWalk = c.acs.state_county_tract('B08006_015E', 32, Washoe, Census.ALL)

# Can you extract the values at the census tract level in Washoe County
# for walking and bicycling commuting to work from the ACS2017 Data?

# Then, based on what you learned in the previous two activities, can you 
# make some graphs or charts?




    
    
