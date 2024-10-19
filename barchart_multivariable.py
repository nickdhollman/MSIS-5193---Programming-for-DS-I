# import libraries
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load data
df = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/Summer-Olympic-medals-1976-to-2008.csv",encoding='latin-1')

# top 10 countries with most medals and show gender distribution in years using catplot
fig = sns.catplot(x="Country", y="Year", hue="Gender",kind="box", data=df,order=df.Country.value_counts().iloc[:10].index)
fig.fig.set_figwidth(14)
fig.fig.set_figheight(6)
plt.show()
