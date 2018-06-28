import numpy as np
import pandas as pd

# import the data from csv file
raw_data = pd.read_csv("Building_Permits.csv")

print("number of nan's in each column of data")
raw_data.isnull().sum()

# perform some cleaning operations
def clean_data(data):
    data = data.dropna()
    return data


refined_data = clean_data(raw_data)