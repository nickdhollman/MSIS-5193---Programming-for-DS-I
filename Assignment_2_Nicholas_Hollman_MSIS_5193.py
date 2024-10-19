#import libraries
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn import preprocessing
import sidetable
import numpy as np
from sklearn.preprocessing import LabelEncoder
import sklearn.feature_selection as fs

#import data
chr = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/2017CHR_CSV_Analytic_Data-new.csv")
print(chr.shape)
print(chr.head())
print(chr.dtypes)

### 1 - Check if any columns have missing data
print(chr.isnull().sum())
#no missing data

## verify there is no missing data
chr_nomiss = chr.dropna(axis=0)
print(chr_nomiss.shape)
#same shape of #3186 rows and 37 columns - no missing data

### 2 - Drop (remove) the identifier columns: FIPS Code, statecode, countycode, country
chr_drop = chr.drop(['5-Digit FIPS Code', 'statecode', 'countycode', 'county'], axis=1)
#verify dropped columns
print(chr_drop.shape)
print(chr_drop.dtypes)

### 3 - use z-score normalization to normalize three columns: poor physical health days value,
# poor mental health days value, food environment index value
# initialize z-score normalization scaler
scalerzscore = preprocessing.StandardScaler()

# normalize LoanAmount
chr_drop[['Poor physical health days Value_z']] = scalerzscore.fit_transform(chr_drop[['Poor physical health days Value']])
chr_drop[['Poor mental health days Value_z']] = scalerzscore.fit_transform(chr_drop[['Poor mental health days Value']])
chr_drop[['Food environment index Value_z']] = scalerzscore.fit_transform(chr_drop[['Food environment index Value']])

# show normalized values
print(chr_drop['Poor physical health days Value'].agg(["mean","std"]))
print(chr_drop[['Poor physical health days Value_z', 'Poor physical health days Value']])
print(chr_drop[['Poor mental health days Value_z', 'Poor mental health days Value']])
print(chr_drop[['Food environment index Value_z', 'Food environment index Value']])

#### 4 Create a new column “Diabetes-level” by coding the “Diabetes Value” into four groups,
# and label them as low, median low, median high, and high (Hint: refer to data coding –
# categorizing coding)
# Descriptive stats for diabetes value
print(chr_drop.stb.freq(['Diabetes Value']))
# continuous in nature so freq does not provide much
print(chr_drop['Diabetes Value'].agg(['min','median', 'mean','max']))
print(chr_drop['Diabetes Value'].quantile([0.25, 0.75]))
# 0 - le quantile 0.25 = low, gt quantile 0.25 - median = median low,
# gt median - quantile 0.75 = median high, greater than quantile 0.75 = high
#create bins
bins = [0, 0.095, 0.1110, 0.1280, np.inf]

# create labels for each bin
group = ['Low', 'Median Low', 'Median High', 'High']

# convert diabetes value into diabetes label and assign the group labels
chr_drop['Diabetes-level'] = pd.cut(chr_drop['Diabetes Value'], bins=bins, labels=group)

# show the results
print(chr_drop[['Diabetes Value','Diabetes-level']])
groupbyDiabetes_lev = chr_drop.groupby("Diabetes-level")[["Diabetes Value"]].agg(["min", "max"])
print(groupbyDiabetes_lev)

#### OPTIONAL - 5 - Apply feature selection to find the top 5 features relevant to “Diabetes-level”.
# use new column “Diabetes-level” as target column y, the rest columns
# (excluding “Diabetes Value” and “Diabetes-level”) as input X))
# are all variables in numerical format
print(chr_drop.dtypes)
# all variables are float or integer in numeric format other than diabetes level
#make diabetes level numeric
Le = LabelEncoder()
chr_drop['Diabetes-level'] = Le.fit_transform(chr_drop['Diabetes-level'])
print(chr_drop.dtypes)

# define the target column y, and input columns (features) in X
y = chr_drop['Diabetes-level']
#drop diabetes level, diabetes value, and untransformed variables
X = chr_drop.drop(['Diabetes-level','Diabetes Value','Food environment index Value', 'Poor physical health days Value', 'Poor mental health days Value'],axis=1)

# apply feature selection - discrete features=False because the X variables are continuous (interval/ratio)
res = dict(zip(X.columns, fs.mutual_info_classif(X, y, discrete_features=False)))

# show ranked features
print(res)
#Population estimate Value had the highest information gain so this would be the best feature for selection
#print(res.sort_values("Salary", axis=0, ascending=True,
                 #inplace=True, na_position='first')