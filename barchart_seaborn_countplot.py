# import libraries
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load data
df = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/Summer-Olympic-medals-1976-to-2008.csv",encoding='latin-1')

# show
print(df.Country)

# top 10 countries with most medals,
# use order to sort the counts
plt.figure(figsize=(14, 8)) #set figure size to adjust labeling space
sns.countplot(x=df["Country"],order=df.Country.value_counts().iloc[:10].index, palette="tab10")
#plt.ylabel('count', fontsize=5)
#plt.xlabel('Country', fontsize=5)
#plt.tick_params(axis='both', labelsize=5)
plt.show()