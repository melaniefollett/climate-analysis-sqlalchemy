# Climate Analysis Using SQLAlchemy

# Part 1: Climate Analysis and Exploration
For this project I used Python and SQLAlchemy to do basic climate analysis and data exploration of a Hawaii weather database. 

# Database Setup
I used SQLAlchemy create_engine to connect to the sqlite database. I then used SQLAlchemy automap_base() to reflect the tables into classes and saveed a reference to those classes called Station and Measurement.  Next I performed a variety of analyses on the data.

# Precipitation Analysis
First I designed a query to retrieve the last 12 months of precipitation data, selecting only the date and prcp values.  Then I loaded the query results into a Pandas DataFrame and set the index to the date column.  I sorted the DataFrame values by date and plotted the results using the DataFrame plot method.  Finally, I used Pandas to print the summary statistics for the precipitation data.

# Station Analysis
I designed a query to calculate the total number of stations, and then designed a query to find the most active stations.  I listed the stations and observation counts in descending order and determined which station had the highest number of observations.

Next I designed a query to retrieve the last 12 months of temperature observation data.  I filtered by the station with the highest number of observations.  Finally, I plotted the results as a histogram.

# Temperature Analysis I

Hawaii is reputed to enjoy mild weather all year. I wanted to investigate if there is a meaningful difference between the temperature in summer (June) and winter (December).
First I identified the average temperature in both June and December at all stations across all available years in the dataset.


I used a paired t-test to determine whether the difference in the means, if any, is statistically significant. I used a paired t-test since the temperature data came from the same stations at different times.  That means the data is related and must be paired.  The p-value was <0.05 which means there is a significant difference between the temperatures in June and Dec.

# Temperature Analysis II

I decided to investigate what the temperatures woud be if I planned a trip to Hawaii from 2017-09-13' to '2017-09-23'.  I used a function to calculate the min, avg, and max temperatures for my trip using the matching dates from the previous year (2016).  Then I plotted the min, avg, and max temperature as a bar chart, using the average temperature as the bar height and the peak-to-peak (tmax-tmin) value as the y error bar.

# Daily Rainfall Average

I was also curious about the daily rainfall for Hawaii during the trip dates I had chosen.  I calculated the rainfall per weather station using the previous year's matching dates.  I then calculated the daily normals (averages for the min, avg, and max temperatures).  I used a function to calculate the normals for each day of the trip and appended the results to a list, and I loaded the list of daily normals into a Pandas DataFrame and set the index equal to the date.  Finally I used Pandas to plot an area plot (stacked=False) for the daily normals.


# Part 2: Climate App
Once I completed my initial analysis, I designed a Flask API based on the queries that I had developed.

# Routes

/api/v1.0/precipitation
- Converts the query results to a Dictionary using date as the key and prcp as the value.
- Returns the JSON representation of the dictionary.

/api/v1.0/stations
- Returns a JSON list of stations from the dataset.

/api/v1.0/tobs
- Queries for the dates and temperature observations from a year from the last data point.
- Returns a JSON list of Temperature Observations (tobs) for the previous year.

/api/v1.0/<start> and /api/v1.0/<start>/<end>
- Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
- When given the start only, calculates TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
- When given the start and the end date, calculates the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
