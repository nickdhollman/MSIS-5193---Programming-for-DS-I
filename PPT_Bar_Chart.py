#import libraries
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load data into dataframe
df = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/mock_sales_data.csv")

# show data
print(df.head(10))

# convert Date column to datetime type - use function pd.to_datetime
df['date'] = pd.to_datetime(df['Date'])

# calculate daily sales
df['sales'] = df['Price']*df['SalesQty']

# calculate monthly sales using data aggregation
# below code groups by month for new date column created and sum the sales col created
# reset index in order to draw the barchart
dfnew = df.groupby(df.date.dt.month)['sales'].sum().reset_index()

# draw bar chart
plt.bar(dfnew['date'],dfnew['sales'])

# add information to the figure
plt.xticks(np.arange(1, 13, step=1)) #this step
plt.title('Monthly Sales Total')
plt.xlabel('Month')
plt.ylabel('$')

# save figure to a file
plt.savefig("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/monthlysale.png")

# show figure
plt.show()