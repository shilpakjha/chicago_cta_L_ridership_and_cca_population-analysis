# Part 4- CTA L- Line Ridership in Loop Stations
# CTA L-Ridership Data Science Project 1
#Data used:

# Data 1 -CTA - Ridership - 'L' Station Entries - Monthly Day-Type Averages & Totals url given below
#This is data from 2001 to 2020 (only Q1)
# https://data.cityofchicago.org/Transportation/CTA-Ridership-L-Station-Entries-Monthly-Day-Type-A/t2rn-p8d7
# Data 2 -L-Stops Data url given below:
#https://data.cityofchicago.org/Transportation/CTA-System-Information-List-of-L-Stops/8pix-ypme

#Required package installs

import pandas as pd
import matplotlib.pyplot as plt
import bokeh as bk
import math
from ast import literal_eval

#Get the Data 1 and 2 Files Use API to connect with the portal and get with Data 1 and 2

# DataFrame 1
#Get the entire ridership data from 2001 to 2020(Q1)
# Write a function to:
# Pick the line type
# Grouping by stationame and year and sum the values
# Sort values
# Create a Pivot table with monthtotal and stationames as rows and the year as the columns

l_rides = pd.read_csv("https://data.cityofchicago.org/resource/t2rn-p8d7.csv?%24limit=350000")
l_rides.head()

# Add date_time, year and month columns to the data set

l_rides['date_time'] = pd.to_datetime(l_rides['month_beginning'])
l_rides["month"] = l_rides["date_time"].dt.month
l_rides["year"] = l_rides["date_time"].dt.year
l_rides.head()

#DataFrame 1.1 (subset of ridership data from 2014 to 2020)

l_2014_2020_rides = l_rides[(l_rides['year'] > 2013) & (l_rides['year'] <= 2020)]
l_2014_2020_rides

# Analysis on DataFrame 1
# Ridership analysis by stations year over year (2014-2020)

# DataFrame 2

l_map_stops = pd.read_csv('https://data.cityofchicago.org/resource/zbnc-zirh.csv',sep=',')

# Add the co-ordinates to each L-stop
# Create a merc function to convert the
def merc(Coords):
    Coordinates = literal_eval(Coords)
    lat = Coordinates[0]
    lon = Coordinates[1]
    r_major = 6378137.000
    x = r_major * math.radians(lon)
    scale = x/lon
    y = 180.0/math.pi * math.log(math.tan(math.pi/4.0 + lat * (math.pi/180.0)/2.0)) * scale
    return (x, y)

    #Use the function to create the x and y coordinates for each l-stop

l_map_stops['coords_x'] = l_map_stops['Location'].apply(lambda x: merc(x)[0])
l_map_stops['coords_y'] = l_map_stops['Location'].apply(lambda x: merc(x)[1])
l_map_stops[['Location', 'coords_x', 'coords_y']].head()

# Drop duplicates since each stop is for going to and going from directions. ALl other data stays same.
l_map_stops.drop_duplicates(subset='MAP_ID', keep="last", inplace=True)

# Change the column name "map_id" to match the name in the l_2014_2020_rides column name which is "station_id"
#This will allow us to merge DataFrames 1 and 2
#The new merged dataframe wnow contains the line infor added for each station.
l_map_stops.rename(columns = {'MAP_ID':'station_id'}, inplace = True)
l_map_stops.head()

# Merge the DataFrames 1 and 2 together on the map_id (data)
# This gives us the ridership across all the L-stops between 2014 and 2020.
# Left Joined the ridership data with the L-stop data so that all the ridership rows are included.

merged_df1and2 = pd.merge(left=l_2014_2020_rides, right=l_map_stops, how='left', left_on='station_id', right_on='station_id')

#Sort the monthtotal values in ascending order

merged_df1and2.sort_values(ascending=False,by="monthtotal",inplace=True)
#merged_df1and2.info()

merged_df1and2.Pnk = merged_df1and2.Pnk.fillna(True)
merged_df1and2.BRN = merged_df1and2.BRN.fillna(True)
merged_df1and2.G = merged_df1and2.G.fillna(True)
merged_df1and2.O = merged_df1and2.O.fillna(True)
merged_df1and2.P = merged_df1and2.P.fillna(True)
merged_df1and2.RED = merged_df1and2.RED.fillna(False)
merged_df1and2.BLUE = merged_df1and2.BLUE.fillna(False)
merged_df1and2.Pexp = merged_df1and2.Pexp.fillna(False)
merged_df1and2.Y = merged_df1and2.Y.fillna(False)
# Replaced NaN values for 20 stations with value 100
merged_df1and2.rename(columns = {'Community Areas':'chi_community_areas'}, inplace = True)
merged_df1and2.chi_community_areas = merged_df1and2.chi_community_areas.fillna(100)
merged_df1and2.rename(columns = {"Census Tracts": 'chi_census_tracts'}, inplace = True)
# Replaced NaN values for the census tracts for 20 stations with value 200.
merged_df1and2.chi_census_tracts = merged_df1and2.chi_census_tracts.fillna(200)
#merged_df1and2.info()

# Analysis of the ridership in the loop from 2014 to 2020.
wash_loop_stations = merged_df1and2.groupby(['stationame', 'year']).sum()
wash_loop_stations.sort_values(ascending=False,by="monthtotal",inplace=True)
loop_stations = pd.pivot_table(data = wash_loop_stations, index = ['stationame','year'], values=["monthtotal"])
loop_stations_2014_2019 = loop_stations.query('year == [2014, 2019] and stationame == ["Clark/Lake", "State/Lake", "Lake/State", "Monroe/State", "Jackson/State", "Adams/Wabash", "Harrison", "LaSalle", "LaSalle/Van Buren", "Quincy/Wells","Merchandise Mart", "Monroe/Dearborn", "Jackson/Dearborn", "Washington/Dearborn", "Washington/Wells", "Washington/Wabash"]').copy()
loop_stations_2014_2019.sort_values(ascending=False,by="monthtotal",inplace=True)
loop_stations_2014_2019
loop_stations_2yrs_2014_2019  = pd.pivot_table(data = loop_stations_2014_2019 , index= 'stationame', columns='year', values="monthtotal")
loop_stations_2yrs_2014_2019['2019_2014_difference'] = loop_stations_2yrs_2014_2019[2019] - loop_stations_2yrs_2014_2019[2014]
loop_stations_2yrs_2014_2019["2014_to_2019_percent_change"] = loop_stations_2yrs_2014_2019['2019_2014_difference'] *100/loop_stations_2yrs_2014_2019[2014]
loop_stations_2yrs_2014_2019.sort_values(ascending=False, by='2014_to_2019_percent_change', inplace =True)
loop_stations_2yrs_2014_2019
