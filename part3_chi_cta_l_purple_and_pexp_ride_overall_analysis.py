# Part 3- CTA combined Purple and Pexp L- Line Ridership Analysis
# CTA L-Ridership Data Science Project 1
# Data used:

# Data 1 -CTA - Ridership - 'L' Station Entries - Monthly Day-Type Averages & Totals url given below
# This is data from 2001 to 2020 (only Q1)
# https://data.cityofchicago.org/Transportation/CTA-Ridership-L-Station-Entries-Monthly-Day-Type-A/t2rn-p8d7
# Data 2 -L-Stops Data url given below:
# https://data.cityofchicago.org/Transportation/CTA-System-Information-List-of-L-Stops/8pix-ypme

# Required package installs

import pandas as pd
import matplotlib.pyplot as plt
import bokeh as bk
import math
from ast import literal_eval

# Get the Data 1 and 2 Files Use API to connect with the portal and get with Data 1 and 2

# DataFrame 1
# Get the entire ridership data from 2001 to 2020(Q1)
# Write a function to:
# Pick the line type
# Grouping by stationame and year and sum the values
# Sort values
# Create a Pivot table with monthtotal and stationames as rows and the year as the columns

l_rides = pd.read_csv(
    "https://data.cityofchicago.org/resource/t2rn-p8d7.csv?%24limit=350000"
)
l_rides.head()

# Add date_time, year and month columns to the data set

l_rides["date_time"] = pd.to_datetime(l_rides["month_beginning"])
l_rides["month"] = l_rides["date_time"].dt.month
l_rides["year"] = l_rides["date_time"].dt.year
l_rides.head()

# DataFrame 1.1 (subset of ridership data from 2014 to 2020)

l_2014_2020_rides = l_rides[(l_rides["year"] > 2013) & (l_rides["year"] <= 2020)]
l_2014_2020_rides

# Analysis on DataFrame 1
# Ridership analysis by stations year over year (2014-2020)

# DataFrame 2

l_map_stops = pd.read_csv(
    "https://data.cityofchicago.org/resource/8pix-ypme.csv", sep=","
)

# Add the co-ordinates to each L-stop
# Create a merc function to convert the
def merc(Coords):
    Coordinates = literal_eval(Coords)
    lat = Coordinates[0]
    lon = Coordinates[1]
    r_major = 6378137.000
    x = r_major * math.radians(lon)
    scale = x / lon
    y = (
        180.0
        / math.pi
        * math.log(math.tan(math.pi / 4.0 + lat * (math.pi / 180.0) / 2.0))
        * scale
    )
    return (x, y)

    # Use the function to create the x and y coordinates for each l-stop


l_map_stops["coords_x"] = l_map_stops["location"].apply(lambda x: merc(x)[0])
l_map_stops["coords_y"] = l_map_stops["location"].apply(lambda x: merc(x)[1])
l_map_stops[["location", "coords_x", "coords_y"]].head()

# Drop duplicates since each stop is for going to and going from directions. ALl other data stays same.
l_map_stops.drop_duplicates(subset="map_id", keep="last", inplace=True)

# Change the column name "map_id" to match the name in the l_2014_2020_rides column name which is "station_id"
# This will allow us to merge DataFrames 1 and 2
# The new merged dataframe wnow contains the line infor added for each station.
l_map_stops.rename(columns={"map_id": "station_id"}, inplace=True)
l_map_stops.head()

# Merge the DataFrames 1 and 2 together on the map_id (data)
# This gives us the ridership across all the L-stops between 2014 and 2020.
# Left Joined the ridership data with the L-stop data so that all the ridership rows are included.

merged_df1and2 = pd.merge(
    left=l_2014_2020_rides,
    right=l_map_stops,
    how="left",
    left_on="station_id",
    right_on="station_id",
)

# Sort the monthtotal values in ascending order

merged_df1and2.sort_values(ascending=False, by="monthtotal", inplace=True)
# merged_df1and2.info()

merged_df1and2.pnk = merged_df1and2.pnk.fillna(True)
merged_df1and2.brn = merged_df1and2.brn.fillna(True)
merged_df1and2.g = merged_df1and2.g.fillna(True)
merged_df1and2.o = merged_df1and2.o.fillna(True)
merged_df1and2.p = merged_df1and2.p.fillna(True)
merged_df1and2.red = merged_df1and2.red.fillna(False)
merged_df1and2.blue = merged_df1and2.blue.fillna(False)
merged_df1and2.pexp = merged_df1and2.pexp.fillna(False)
merged_df1and2.y = merged_df1and2.y.fillna(False)

# merged_df1and2.info()

line_name = ""
start_year = 0
end_year = 0


def l_line_analysis(line_name, start_year, end_year):
    line_name = str(line_name)
    start_year = int(start_year)
    end_year = int(end_year)
    print("\nLine Name:", line_name)

    if line_name == "red":
        ridesby_line_year_range = merged_df1and2[
            (merged_df1and2["red"] == 1)
            & (merged_df1and2["year"] >= start_year)
            & (merged_df1and2["year"] <= end_year)
        ]

    elif line_name == "blue":
        ridesby_line_year_range = merged_df1and2[
            (merged_df1and2["blue"] == 1)
            & (merged_df1and2["year"] >= start_year)
            & (merged_df1and2["year"] <= end_year)
        ]

    elif line_name == "o":
        ridesby_line_year_range = merged_df1and2[
            (merged_df1and2["o"] == 1)
            & (merged_df1and2["year"] >= start_year)
            & (merged_df1and2["year"] <= end_year)
        ]

    elif line_name == "pnk":
        ridesby_line_year_range = merged_df1and2[
            (merged_df1and2["pnk"] == 1)
            & (merged_df1and2["year"] >= start_year)
            & (merged_df1and2["year"] <= end_year)
        ]

    elif line_name == "p":
        ridesby_line_year_range = merged_df1and2[
            (merged_df1and2["p"] == 1)
            & (merged_df1and2["year"] >= start_year)
            & (merged_df1and2["year"] <= end_year)
        ]

    elif line_name == "pexp":
        ridesby_line_year_range = merged_df1and2[
            (merged_df1and2["pexp"] == 1)
            & (merged_df1and2["year"] >= start_year)
            & (merged_df1and2["year"] <= end_year)
        ]

    # elif line_name == 'PandPexp':
    #    ridesby_line_year_range = merged_df1and2[(merged_df1and2['P'] == 1) &
    #                        (merged_df1and2['Pexp'] == 1) &
    #                        (merged_df1and2['year'] >= start_year) &
    #                        (merged_df1and2['year'] <= end_year)]

    # This uses the OR boolean operator to capture both, the P or Pexp rides
    # In 2019 there were 0 P rides since both the stations Madison/Wabash and Randoplh/Wabash were dropped
    elif line_name == "pandpexp":
        ridesby_line_year_range = merged_df1and2[
            (merged_df1and2["p"] == 1)
            | (merged_df1and2["pexp"] == 1)
            & (merged_df1and2["year"] >= start_year)
            & (merged_df1and2["year"] <= end_year)
        ]

    elif line_name == "g":
        ridesby_line_year_range = merged_df1and2[
            (merged_df1and2["g"] == 1)
            & (merged_df1and2["year"] >= start_year)
            & (merged_df1and2["year"] <= end_year)
        ]

    elif line_name == "brn":
        ridesby_line_year_range = merged_df1and2[
            (merged_df1and2["brn"] == 1)
            & (merged_df1and2["year"] >= start_year)
            & (merged_df1and2["year"] <= end_year)
        ]
    elif line_name == "y":
        ridesby_line_year_range = merged_df1and2[
            (merged_df1and2["y"] == 1)
            & (merged_df1and2["year"] >= start_year)
            & (merged_df1and2["year"] <= end_year)
        ]

    df1 = ridesby_line_year_range.groupby(["stationame", "year"]).sum()
    df1.sort_values(ascending=True, by="monthtotal", inplace=True)
    df2 = (
        pd.pivot_table(data=df1, index="year", values="monthtotal", aggfunc="sum")
        .reset_index()
        .rename(columns={"monthtotal": "total_monthly_rides"})
    )
    df3 = df2[df2["year"].isin(["2014", "2019"])].copy()
    df3["difference"] = (
        df3["total_monthly_rides"].shift(-1) - df3["total_monthly_rides"]
    )
    df3["percent_change"] = df3["difference"] * 100 / df3["total_monthly_rides"]

    print(df3)


def main():
    #l_line_analysis("red", 2014, 2019)
    #l_line_analysis("blue", 2014, 2019)
    #l_line_analysis("o", 2014, 2019)
    #l_line_analysis("pnk", 2014, 2019)
    #l_line_analysis("p", 2014, 2019)
    #l_line_analysis("pexp", 2014, 2019)
    l_line_analysis("pandpexp", 2014, 2019)
    #l_line_analysis("g", 2014, 2019)
    #l_line_analysis("brn", 2014, 2019)
    #l_line_analysis("y", 2014, 2019)


if __name__ == "__main__":
    main()
