### slides 5-6

# import libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# load data into dataframe
price = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/prod_prices.csv")

# impute missing data - forward fill using the previous obs for missing data b/c it is time series
price[['price']] = price[['price']].ffill()

# plot price with date
plt.plot(price['Date'],price['price'])

# Set the font size of xticks
plt.xticks(fontsize=5)
plt.show()

# impute missing data - same step as above so not needed
price[['price']] = price[['price']].ffill()

# df : input data frame
# step : sampling interval
def systematic_sampling(df, step):
    #Get the indexes of the sampling data
    indexes = np.arange(0, len(df), step=step)

    #Get the subset based on the indexes
    systematic_sample = df.iloc[indexes]

    #return the new data frame with sampled data
    return systematic_sample

# plot price
pricenew = systematic_sampling(price, 5)

# plot price with date
plt.plot(pricenew['Date'],pricenew['price'])

plt.show()