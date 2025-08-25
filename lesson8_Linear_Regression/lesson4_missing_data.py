import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

with open('../course_data/DATA/Ames_Housing_Feature_Description.txt', 'r') as f: print(f.read())

df = pd.read_csv('../course_data/DATA/Ames_outliers_removed.csv')
df.info()

df.head()
df = df.drop('PID', axis=1)
len(df.columns)
df.isnull().sum()/len(df)

def percent_missing(my_df):
    result = 100*my_df.isnull().sum() / len(my_df)
    result = result[result>0].sort_values()
    return result

percent_nan = percent_missing(df)
print(f"PERCENT_NAN: \n{percent_nan}")