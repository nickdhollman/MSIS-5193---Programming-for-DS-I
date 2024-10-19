import pandas as pd

df = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/Salaries.csv")

#this will print the series type of data for salary
#also notice that there are no column titles for the series type
print(df['salary'])
print(type(df['salary']))

#this produce a dataframe object of salary columns from salaries excel file
print(df[['salary']])
print(type(df[['salary']]))

#this will produce a dataframe object of rank and salary columns
#notice that the first column shown is rank and then salary because that is the order I called them in
print(df[['rank', 'salary']])

#below uses the loc function which allows us to call certain rows and columns using their column names
#the below code calls for the 10 - 15 row of the columns rank and salary
print(df.loc[10:15, ['rank', 'salary']])

#below uses the iloc function which allows use to call certain rows and columns using their column indexes
#the below code is a special example, ":" calls all rows, and [-1] calls the last column
print(df.iloc[:,-1])