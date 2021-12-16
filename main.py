# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, this Project is created for data analytics using Uber dataset created by, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


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
files = os.listdir()
apr_df = pd.read_csv(r'Uber_datasets/uber-raw-data-apr14.csv')
may_df = pd.read_csv(r'Uber_datasets/uber-raw-data-may14.csv')
jun_df = pd.read_csv(r'Uber_datasets/uber-raw-data-jun14.csv')
jul_df = pd.read_csv(r'Uber_datasets/uber-raw-data-jul14.csv')
aug_df = pd.read_csv(r'Uber_datasets/uber-raw-data-aug14.csv')
sep_df = pd.read_csv(r'Uber_datasets/uber-raw-data-sep14.csv')

# concatenating all dataset into one
data =pd.concat([apr_df,may_df,jun_df,jul_df,aug_df,sep_df])
print(data.head())
data1 =pd.concat([apr_df,may_df,jun_df,jul_df,aug_df,sep_df])
print(data1.head())

