# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(
        f'Hi, this Project is created for data analytics using Uber dataset created by, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Prakher')

# libraries for data manipulation and exploration
import pandas as pd
import numpy as np
# libraries for data visualization
import matplotlib.pyplot as plt
import seaborn as sns
import os

# we have dataset of six months of year 2014
# april, may, june, july, august and september
# Listing down the required files
files = [filename for filename in sorted(os.listdir(r'Uber_datasets')) if filename.startswith("uber-")]
# concatenating all dataset into one
path = 'C:/Users/win-10/PycharmProjects/UCDPA_PRAKHER/Uber_datasets/'
Data = pd.DataFrame()

for file in files:
    df = pd.read_csv(path + "/" + file, encoding='utf-8')
    Data = pd.concat([df, Data])
# Step 2 :Analysing data
print(Data.shape)
# checking Top 5 rows
print(Data.head())
# checking last 5 rows
print(Data.tail())
# checking datatype
print(Data.dtypes)
# Since Data/Time column is having data type as object so we are now changing its format to datatime
print('After converting datatype of data time')
Data['Date/Time'] = pd.to_datetime(Data['Date/Time'], format='%m/%d/%Y %H:%M:%S')
print(Data.dtypes)
# Now, we were going to add a new collumn to define weekday, day, minute, month, and hour
# displaying all columns
# pd.options.display.max_columns = None
Data['Month'] = Data['Date/Time'].dt.month_name().str[:3]
Data['day'] = Data['Date/Time'].dt.day_name().str[:3]
Data['Hour'] = Data['Date/Time'].dt.hour
Data['Nday'] = Data['Date/Time'].dt.day
Data['Date/Time'] = Data['Date/Time'].dt.date
print(Data.head)
# Replace missing values or drop duplicates
# checking if there are null values or not
print('Null values in each column :')
print(Data.isnull().sum())
print('\n')
print(Data.info())

#Analysis of above data using visualization library

print('Plotting the trips by the hours in a day')
plt.figure(figsize=(12,5))
# creating bar plot to show the count of rides by hours of day
sns.countplot(x='Hour',data=Data,palette='mako',saturation=1)
# removing the frame around graph
sns.despine(bottom=True, left=True)
# removing x and y label
plt.xlabel('Hours')
plt.ylabel('Number of rides')
plt.title('Number of rides by hours', fontsize=15);
print(plt.show())

print('Plotting data by trips during every day of the month')
plt.figure(figsize=(10,8))
plt.hist(Data['Nday'], bins=31,color='b', edgecolor='red', rwidth=0.8) # bins is the number of equal width in the graphs
plt.xlabel('Day')
plt.ylabel('Sum of Numbers of Trips')
plt.title('Journey by days in month')
print(plt.show())