import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn import preprocessing
import sidetable

# Read a dataset with missing values
loan = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/train_Loan.csv")
print(loan.head())

# Select the rows that have at least one missing value
loadtop = loan[loan.isnull().any(axis=1)].head()
print(loadtop)
print(loadtop.isnull().sum())
print(loadtop[['Loan_ID','Gender', 'Self_Employed', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History']])

# drop the rows with missing values
loannew = loan.dropna(axis=0)

# show the number of missing values for each column
print(loannew.isnull().sum())

# delete the column 'Dependents'
loannew = loan.drop(['Dependents'],axis=1)

# show columns with missing values
print(loannew.isnull().sum())

# impute the married column using the most common value
loan['Married'] = loan['Married'].fillna(loan['Married'].mode()[0])

# impute the Self_Employed column using the most common value
loan['Self_Employed'] = loan['Self_Employed'].fillna(loan['Self_Employed'].mode()[0])

# impute the LoanAmount using the mean value
loan['LoanAmount'] = loan['LoanAmount'].fillna(loan['LoanAmount'].mean())

#check that imputation worked
print(loan.isnull().sum())

# load data
price = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/prod_prices.csv")
print(price.head())

# show columns with missing values
print(price.isnull().sum())

# show columns with missing values
#price[['price']] = price[['price']].fillna(method='ffill')
price[['price']] = price[['price']].ffill()

# show columns with missing values
print(price.isnull().sum())

# initalize the imputer using SimpleImputer in sklearn, use most frequent value to impute
imputer = SimpleImputer(strategy='most_frequent')

# impute Gender using most frequent value in the column
loan[['Gender']] = imputer.fit_transform(loan[['Gender']])
print(loan.isnull().sum())

# initalize the imputer using SimpleImputer in sklearn, use new value 'unknown' to impute
imputerconst= SimpleImputer(strategy='constant',fill_value='unknown')

# impute Gender using new value 'unknown' to impute
# above section must be commented out for this to work
loan[['Gender']] = imputerconst.fit_transform(loan[['Gender']])
print(loan.stb.freq(["Gender"]))

### Class ex
food = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/food-consumption.csv")

print(food.isnull().sum())

imputer = SimpleImputer(strategy='most_frequent')

print(food.dtypes)
print(food[["Sweetener", "Biscuits", "Yoghurt"]].agg(["mean", "median", "min", "max"]))

# impute Sweetener, Biscuits, Yoghurt using most frequent value in the column
food['Sweetener'] = food[['Sweetener']].fillna(food[['Sweetener']].median())
food['Biscuits'] = food[['Biscuits']].fillna(food[['Biscuits']].median())
food['Yoghurt'] = food[['Yoghurt']].fillna(food[['Yoghurt']].median())
print(food.isnull().sum())
print(food[["Sweetener", "Biscuits", "Yoghurt"]].agg(["mean", "median", "min", "max"]))







