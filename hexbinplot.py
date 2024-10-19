# import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# load data
df = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/apple_stock_prices_2022.csv")

# draw scatter plot
plt.scatter(df['Close'],df['Open'])
plt.title('Scatter plot')
plt.xlabel('Close')
plt.ylabel('Open')
plt.show()

# draw hexbin plot
df.plot.hexbin(x='Close', y='Open', gridsize=20) #gridsize specifies how big the hexagon will be
plt.title('Hexbin plot')
plt.xlabel('Close')
plt.ylabel('Open')
plt.show()
