# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from matplotlib import cm


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
from sklearn.cluster import DBSCAN
from geopy.distance import great_circle
from shapely.geometry import MultiPoint

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
#Replace missing values or drop duplicates
#checking for null values

print("Number of NaN values in every column.")
print(pd.isnull(Data).sum(axis = 0))
print("Number of NaN values in every ROW.")
print(pd.isnull(Data).sum(axis = 1))
print("Since in data set no missing values is there, lets find out the duplicates and remove it from data set ")
print("Sum of duplicates in dataframe")
print(df.duplicated().sum())
print("Drop duplicates in dataframe using keep =first")
print(Data.drop_duplicates(keep = 'first').shape)
print("Drop duplicates in dataframe using keep =last")
print(Data.drop_duplicates(keep = 'last').shape)
print("Drop duplicates in dataframe using keep =False")
print(Data.drop_duplicates(keep = False).shape)
print("Drop missing values in dataframe column")
print(Data.dropna(subset = ['Date/Time', 'Lat', 'Lon', 'Base'], how = 'any').shape)
# checking datatype
print(Data.dtypes)
# Since Data/Time column is having data type as object so we are now changing its format to datatime
print('After converting datatype of data time')
Data['Date/Time'] = pd.to_datetime(Data['Date/Time'], format='%m/%d/%Y %H:%M:%S')
print(Data.dtypes)
print('\n')
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


#implement machine learning model(Unsupervised learning)

def get_hot_spots(max_distance, min_cars, ride_data):
    ## get coordinates from ride data
    coords = ride_data[['Lat', 'Lon']].to_numpy()

    ## calculate epsilon parameter using
    kms_per_radian = 6371.0088
    epsilon = max_distance / kms_per_radian

    ## perform clustering
    db = DBSCAN(eps=epsilon, min_samples=min_cars,
                algorithm='ball_tree', metric='haversine').fit(np.radians(coords))

    ## group the clusters
    cluster_labels = db.labels_
    num_clusters = len(set(cluster_labels))
    clusters = pd.Series([coords[cluster_labels == n] for n in range(num_clusters)])

    ## report
    print('Number of clusters: {}'.format(num_clusters))

    ## initialize lists for hot spots
    lat = []
    lon = []
    num_members = []

    ## loop through clusters and get centroids, number of members
    for ii in range(len(clusters)):
        ## filter empty clusters
        if clusters[ii].any():
            ## get centroid and magnitude of cluster
            lat.append(MultiPoint(clusters[ii]).centroid.x)
            lon.append(MultiPoint(clusters[ii]).centroid.y)
            num_members.append(len(clusters[ii]))

    hot_spots = [lon, lat, num_members]

    return hot_spots


#get ride_data
ride_data=Data.loc[(Data['Nday']==21) & (Data['Hour'] >15)]
max_distance =0.05
min_pickups = 25
hot_spots =  get_hot_spots(max_distance, min_pickups, ride_data)
print(hot_spots)
## make the figure
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111)
## set the color scale
color_scale = np.log(hot_spots[2])
# color_scale = hot_spots[2]
## make the scatter plot
plt.scatter(hot_spots[0], hot_spots[1], s=80, c=color_scale, cmap=cm.cool)
print(plt.show())


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

"""visualization by creating heatmap using seaborn and matplotlib by method of custom function"""
def cust_heat(col1,col2,col3):
    merge_col = Data.groupby([col1, col2]).apply(lambda x: len(x))
    pivot = merge_col.unstack()
    plt.figure(figsize=(10, 6))
    plt.title(col3)
    return sns.heatmap(pivot, annot=False)


## validating above Analysis through Heatmap
cust_heat('day','Month','Heatmap by Month and day ')
plt.show()

##Analysis of location data points

plt.figure(figsize=(20,10))
sns.scatterplot(data=Data,y='Lat',x='Lon',alpha=0.4)
plt.xlim(-75,-72.5)
plt.ylim(40.0,41.2)
print(plt.show())