# import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# load data
df = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/Summer-Olympic-medals-1976-to-2008.csv",encoding='latin-1')

# top 10 countries with most medals
# below syntax is counting the medals by 'Country' (sum medals by row) but [:10] is telling python to only take the top 10
top_10 = df['Country'].value_counts()[:10]
print(top_10)
top_10.plot(kind='bar')
plt.title('All Time Medals of top 10 countries')
plt.xlabel('Country')
plt.ylabel('')
plt.subplots_adjust(bottom=0.4) # this increases the spacing on the bottom
plt.show()

# filter on US to show the medal distribution
medalus = df[df['Country']=='United States']['Medal'].value_counts()
medalus.plot(kind='bar')
plt.xlabel('Medal')
plt.subplots_adjust(bottom=0.3)
plt.show()
