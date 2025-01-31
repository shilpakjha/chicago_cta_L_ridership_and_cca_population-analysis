## Project Title

Analysis of CTA L-ridership and population trends in Chicago Community Areas for loop and surrounding areas

## Description

In Chicago, the nine CTA L-lines (Red, Blue, Brown, Green, Orange, Pink, Purple, Purple Express, and Yellow) allow travelers to go to all major Chicagoland areas near the vicinity of the city 

In this project, we will use the CTA L Line ridership data from years, 2014 to 2019, and the population data for each Chicago Community Areas (2000, 2010, 2017)to understand ridership, and population trends and depict patterns. We will write a python code to run commands and compute statistics using pandas to answer the following questions:
* Total CTA L-ridership trend from 2014 to 2019 for all CTA L-Lines combined together 
* Ridership analysis by each of the nine individual CTA L-Lines for 2014 to 2019
* Combined ridership trend at the L-Loop Stations from 2014 to 2019
* L-Loop Stations ridership analysis(Clark/Lake, State/Lake, Lake/State, Washington/Dearborn, Monroe/State, Adams/Wabash, Washington/Wabash, Harrison, LaSalle, LaSalle/Van Buren, Quincy/Wells, Washington/Wells) Merchandise Mart, Monroe/Dearborn, Jackson/Dearborn
* Population near the community areas around the loop and surrounding loop areas

## Key Analysis Insights
* It is interesting to note that even if the overall L- ridership declined from 2014 to 2019 by 8.1%, the Chicago Loop ridership (within the Chicago Loop) increased by 8.4%.
* This trend correlates with the CCA 32 population trend data which saw a 22.5% increase in the loop population from 2010 to 2017.
* A closer look at the loop station ridership showed that the increase in ridership was mainly in a few stations (State/Lake, Washington/Wells, Washington/Dearborn, Monroe/Dearborn, Merchandise Mart, Clark/Lake, LaSalle/Van Buren) - increase range of 22.3 - 1.1 %.
* Based on the data available for the loop stations along Washington St, the increase in ridership was localized to these stations (predominantly Washington/Wells and Washington/Dearborn). This may be because of the close proximity of these stations to the Ogilvie Transpiration Center which is the connection hub for the Chicago Suburban population which works in the Chicago Loop. (Suburban Rail lines - Metra)

## APIs used
* CTA_-Ridership-L-Station-Entries-Monthly-Day: https://data.cityofchicago.org/Transportation/CTA-Ridership-L-Station-Entries-Monthly-Day-Type-A/t2rn-p8d7
* L-Map_Stops: https://data.cityofchicago.org/Transportation/CTA-System-Information-List-of-L-Stops/8pix-ypme/data

## Data sources:
* CTA_-Ridership-L-Station-Entries: https://data.cityofchicago.org/Transportation/CTA-Ridership-L-Station-Entries-Monthly-Day-Type-A/t2rn-p8d7
* L-stops: https://data.cityofchicago.org/Transportation/CTA-System-Information-List-of-L-Stops/8pix-ypme/data 
* Chicago Community Areas Data: https://datahub.cmap.illinois.gov/dataset/1d2dd970-f0a6-4736-96a1-3caeb431f5e4/resource/96bc2e7d-9276-4d66-8cbf-63a0ed09a2a2/download/CDSarchive201906.zip

## Files used:
* Chicago CCA Population File: ReferenceCCAProfiles20132017mergedCCAcopy.csv 

## Credits 
The following sites and resources were used to gain knowledge about CTA Ridership and problem solve coding and formatting issues: 
* https://stackoverflow.com 
* https://www.w3schools.com 
* https://black.now.sh/ 
* https://towardsdatascience.com/exploring-and-visualizing-chicago-transit-data-using-pandas-and-bokeh-part-i-intro-to-pandas-5d6caa8813ef
* https://www.makeareadme.com
