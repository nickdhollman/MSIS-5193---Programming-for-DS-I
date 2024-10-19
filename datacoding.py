import pandas as pd
from sklearn.preprocessing import LabelEncoder
import sidetable
import numpy as np

# Read a dataset
food = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/groceries.csv")

# show the top few rows
print(food.head())

# check the number of unique values in column product_group
print(food['product_group'].nunique())

# show the number of missing values in each column
print(food.isnull().sum())

# initial label encoder to do numeric encoding
Le = LabelEncoder()

# code the product_group to numbers
food['product_group']= Le.fit_transform(food['product_group'])

# show the top few rows to see the coding result
print(food.head())


# impute the missing values in 'price' column and prepare for categorizing coding
food.head()
print(food['price'].nunique())
print(food.isnull().sum())
#food[['price']] = food[['price']].fillna(method='ffill')
food[['price']] = food[['price']].ffill()
print(food.isnull().sum())

# show max and min value of 'price' column
print(food['price'].max())
print(food['price'].min())
print(food['price'].agg(['min','median','mean','max']))
print(food['price'].quantile([0.25, 0.75]))

# create bins
bins = [0, 2, 4, 6, 8, 10, np.inf]

# create labels for each bin
group = ['<2', '2-4', '4-6', '6-8', '8-10', '>10']

# convert price into price groups and assign the group labels
food['price_group'] = pd.cut(food['price'], bins=bins, labels=group)

# show the results
print(food[['price','price_group']])

## Class ex - encode the columns 'Education' and 'ApplicantIncome' using either numeric coding or categorizing coding strategy
#### handle missing data first
loan = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/train_Loan.csv")
print(loan.isnull().sum())
#no missing data for ApplicantIncome
#No missing data for Education
print(loan.dtypes)
#Education is object type, ApplicantIncome is integer
print(loan.stb.freq(['Education']))
print(loan['Education'].head())
#use numeric coding for Education
print(loan['ApplicantIncome'].agg(['min','median', 'mean','max']))
print(loan['ApplicantIncome'].quantile([0.25, 0.75]))
#use categorizing coding strategy for ApplicantIncome

# initial label encoder to do numeric encoding
Le = LabelEncoder()

# code the product_group to numbers
loan['Education']= Le.fit_transform(loan['Education'])

# show the top few rows to see the coding result
print(loan['Education'].head())
print(loan.head())

# create bins for ApplicantIncome - 0, 25th pct., median, 75th pct, infinity
bins = [0, 2877.5, 3812.5, 5795.0, np.inf]

# create labels for each bin
group = ['<2877.5', '2877.5-3812.4', '3812.5-5794.9', '>= 5795.0']

# convert price into price groups and assign the group labels
loan['App_Inc_group'] = pd.cut(loan['ApplicantIncome'], bins=bins, labels=group)

# show the results
print(loan[['ApplicantIncome','App_Inc_group']])
