# import libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

########### THIS IS THE CORRECT CODE TO PRODUCE THE SAMPLED LINECHART ##########

# df : input data frame
# step : sampling interval
def systematic_sampling(df, step):
    #Get the indexes of the sampling data
    indexes = np.arange(0, len(df), step=step)

    #Get the subset based on the indexes
    systematic_sample = df.iloc[indexes]

    #return the new data frame with sampled data
    return systematic_sample

# load data into dataframe
price = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/prod_prices.csv")

# data sampling
pricenew = systematic_sampling(price, 5)

# impute missing data
pricenew[['price']] = pricenew[['price']].fillna(method='ffill')

# plot price
# plt.plot(price['price'])

# plot price with date
plt.plot(pricenew['Date'],pricenew['price'])

# Set the font size of xticks
plt.xticks(fontsize=10)

plt.show()
