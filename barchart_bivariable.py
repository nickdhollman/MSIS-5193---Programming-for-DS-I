# import libraries
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load data
df = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/Summer-Olympic-medals-1976-to-2008.csv",encoding='latin-1')

# top 10 countries with most medals and show gender distribution
plt.figure(figsize=(13, 6))
sns.countplot(x="Country", hue="Gender", data=df, order=df.Country.value_counts().iloc[:10].index)
plt.show()

# top 10 countries with most medals and show gender distribution using catplot
sns.catplot(kind="count", y="Country", hue="Gender", data=df, order=df.Country.value_counts().iloc[:10].index)
plt.show()

#### Class exercise ####
#Use the loan data to generate a bar chart to show the relations between marriage status and property area
#Read and experiment using the code in document “stacked bar chart reading.pdf” (in Canvas Files -> reading materials folder) about creating stacked bar chart
#code for boxplot - fig = sns.catplot(x="Country", y="Year", hue="Gender",kind="box", data=df,order=df.Country.value_counts().iloc[:10].index)

#sample code for stacked bar chart
'''
#set seaborn plotting aesthetics
sns.set(style='white')

#create stacked bar chart
df.set_index('Day').plot(kind='bar', stacked=True, color=['steelblue', 'red'])
'''
