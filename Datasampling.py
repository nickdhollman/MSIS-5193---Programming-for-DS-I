import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

# df : input data frame
# step : sampling interval
def systematic_sampling(df, step):
    #Get the indexes of the sampling data - len(df) is the length of the dataframe
    indexes = np.arange(0, len(df), step=step)

    #Get the subset based on the indexes
    systematic_sample = df.iloc[indexes]

    #return the new data frame with sampled data
    return systematic_sample

# load data into dataframe
price = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/prod_prices.csv")
print(price)
print(price.shape)
print(price.head(10))
print(price.dtypes)

# impute missing data
#price[['price']] = price[['price']].fillna(method='ffill')
price[['price']] = price[['price']].ffill()

# data sampling - sample every 5 rows
pricenew = systematic_sampling(price, 5)

# show results
print(pricenew)

# load data
loan = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/train_Loan.csv")

# show the size of loan (number of rows, number of columns)
print(loan.shape)
print(loan.head(10))
print(loan.dtypes)

# check the unique values of
print(loan['Property_Area'].nunique())

#### DISPROPORTIONATE SAMPLING ####
# sample 100 from each value of 'Property_Area' - we are telling python to sample 100 from each unique property area group
loansample = loan.groupby('Property_Area',group_keys=False).apply(lambda x: x.sample(100))

# show results
print(loansample)

#### PROPORTIONATE SAMPLING ###
# sample 0.6 of the data based on the combination of 'Property_Area' and 'Education'
loansample_b = loan.groupby(['Property_Area','Education'],group_keys=False).apply(lambda x: x.sample(frac=0.6))

# show results
print(loansample_b)

## Class Exercise - Make a proportionate sampling based on gender, married, dependents, self-employed
## Handle missing data first
loan = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/train_Loan.csv")
print(loan)
print(loan.shape)
print(loan.head(10))
print(loan.dtypes)
print(loan.isnull().sum())
#Gender - object, Married - object, Dependents - object, Education - object, Self-employed-object
#fill missing values
#imputerconst= SimpleImputer(strategy='constant',fill_value='unknown')
imputer = SimpleImputer(strategy='most_frequent')

# impute Gender using most frequent value in the column
loan[['Gender','Married', 'Dependents', 'Education', 'Self_Employed']] = imputer.fit_transform(loan[['Gender','Married', 'Dependents', 'Education', 'Self_Employed']])
print(loan.isnull().sum())

#proportional sampling based on gender married dependents education and self employment
loansample_ex = loan.groupby(['Gender','Married', 'Dependents', 'Education', 'Self_Employed'],group_keys=False).apply(lambda x: x.sample(frac=0.5))

print(loansample_ex)