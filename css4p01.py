# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 15:49:37 2024

@author: jaydo
"""

import pandas as pd

'''Read in the csv file using the Rank column as the index and fix the spaces 
 in the column names'''
column_names = ["Rank", "Title", "Genre", "Description", "Director", "Actors",
                "Year", "Runtime_Minutes", "Rating", "Votes", "Revenue_Millions", "Metascore"]
df = pd.read_csv("movie_dataset.csv", index_col=0,
                 header=0, names=column_names)


# Fill the NaN values in the revenue column with the mean value
rev = df["Revenue_Millions"].mean()
df.fillna(rev, inplace=True)

# Fill the NaN values in the metascore column with the median value
meta = df["Metascore"].median()
df.fillna(meta, inplace=True)

# Dropping any duplicate rows
df.drop_duplicates(inplace=True)

# Filter data by year
df2015 = df[df["Year"] == 2015]
df2016 = df[df["Year"] == 2016]
df2017 = df[df["Year"] == 2017]

# Concatinat the three years
df_2015_to_2017 = pd.concat([df2015, df2016, df2017], ignore_index=True)

avg_revenue_2015_to_2017 = df_2015_to_2017["Revenue_Millions"].mean()

# Filter data for christopher nolan
df_Christopher_Nolan = df[df["Director"] == "Christopher Nolan"]

# Filter data for rating greater than or equal to 8.0
df_rating8 = df[df["Rating"] >= 8.0]

df_Christopher_Nolan_avg_rating = df_Christopher_Nolan["Rating"].mean()

# Filter years
df2006 = df[df["Year"] == 2006]
df2007 = df[df["Year"] == 2007]
df2008 = df[df["Year"] == 2008]

df2006_avg_rating = df2006["Rating"].mean()
df2007_avg_rating = df2007["Rating"].mean()
df2008_avg_rating = df2008["Rating"].mean()
df2016_avg_rating = df2016["Rating"].mean()

percentage_increase_2006_to_2016 = ((297-44) / 44) * 100

#Split actors column
df[['Actor1', 'Actor2', 'Actor3', 'Actor4']] = df['Actors'].str.split(',', n=3, expand=True)

#Check if actor is listed in any of the actor columns
'''Bradley Cooper, Mark Wahlberg, Chris Pratt, Matthew McConaughey'''
actor = "Mark Wahlberg"

df_actor1 = df[df["Actor1"] == actor]
df_actor2 = df[df["Actor2"] == actor]
df_actor3 = df[df["Actor3"] == actor]
df_actor4 = df[df["Actor4"] == actor]

#Split genre column
df[['genre1', 'genre2', 'genre3', ]] = df['Genre'].str.split(',', n=3, expand=True)

#Save as seperate data frames
df_genre1 = df["genre1"]
df_genre2 = df["genre2"]
df_genre3 = df["genre3"]

#Drop NaNs
df_genre1.dropna(inplace=True)
df_genre2.dropna(inplace=True)
df_genre3.dropna(inplace=True)

#Concatinate the 3 data frames and drop duplicates
df_genre_total = pd.concat([df_genre1, df_genre2, df_genre3], ignore_index=True)
df_genre_total.drop_duplicates(inplace = True)

#Data correlation
df_describe = df.describe()
df.info()

#Visualization
import matplotlib.pyplot as plt
'''Revenue_Millions, Metascore, Rating, Votes, Runtime_Minutes, Year'''
plt.scatter(df["Runtime_Minutes"], df["Votes"])
plt.show()

plt.scatter(df["Runtime_Minutes"], df["Metascore"])
plt.show()

plt.scatter(df["Runtime_Minutes"], df["Revenue_Millions"])
plt.show()

plt.scatter(df["Runtime_Minutes"], df["Rating"])
plt.show()

plt.scatter(df["Year"], df["Revenue_Millions"])
plt.show()

plt.scatter(df["Year"], df["Metascore"])
plt.show()

plt.scatter(df["Year"], df["Rating"])
plt.show()

plt.scatter(df["Metascore"], df["Rating"])
plt.show()

plt.scatter(df["Votes"], df["Rating"])
plt.show()

plt.scatter(df["Votes"], df["Metascore"])
plt.show()

plt.scatter(df["Votes"], df["Revenue_Millions"])
plt.show()
