# load libraries
from sklearn.preprocessing import LabelEncoder
import sklearn.feature_selection as fs
import pandas as pd
import sidetable

# import data
PlayTennis = pd.read_csv('C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/playTennis.csv')

# since the features are not numbers, we need to encode data
Le = LabelEncoder()
print(PlayTennis)

# code columns
PlayTennis['outlook'] = Le.fit_transform(PlayTennis['outlook'])
PlayTennis['temp'] = Le.fit_transform(PlayTennis['temp'])
PlayTennis['humidity'] = Le.fit_transform(PlayTennis['humidity'])
PlayTennis['windy'] = Le.fit_transform(PlayTennis['windy'])
PlayTennis['play'] = Le.fit_transform(PlayTennis['play'])
print(PlayTennis)

# define the target column y, and input columns (features) in X
y = PlayTennis['play']
X = PlayTennis.drop(['play'],axis=1)

# apply feature selection - discrete features=True because none of the X variables are continuous (interval/ratio)
res = dict(zip(X.columns, fs.mutual_info_classif(X, y, discrete_features=True)))

# show ranked features
print(res)
#outlook had the highest information gain so this would be the best feature for selection
