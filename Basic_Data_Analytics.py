import pandas as pd

df = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/Salaries.csv")
df.head()
#this will not produce anything, instead, you need to use print

#below prints the first 5 rows
print(df.head())

#below prints the number of rows and columsn
print(df.shape)

#below prints the type of each variable
print(df.dtypes)