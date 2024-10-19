# import libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# load the show the built-in data set in seaborn library
flights = sns.load_dataset("flights")
print(flights)

# draw the heatmap, index is the y-axis, columns is the x-axis, value is the cell (what the heat distribution is representing)
plt.figure(figsize=(18, 6))
flights = flights.pivot(index="month", columns="year", values="passengers")
ax = sns.heatmap(flights, annot=True) #annot=True labels the values w/n the cells
plt.title("Heatmap Flight Data")
plt.show()

# load a build-in data set 'tips'
sales = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/sales_data_with_stores.csv")

# data aggregation - get average last week sales by store and product group
salesnew = sales.groupby(["store","product_group"], as_index=False).agg(
   avg_sales = ("last_week_sales", "mean")
).sort_values(by="avg_sales", ascending=False)
print(salesnew.groupby(["store","product_group"])['avg_sales'].mean())

# draw the heatmap, index is the y-axis, columns is the x-axis, value is the cell
salesnew = salesnew.pivot(index="store", columns="product_group", values="avg_sales")
sns.heatmap(salesnew,annot=True,cmap='RdYlGn',linewidths=0.30)
plt.title("sales heatmap")
plt.show()

## In class ex
# Use the groceries.csv, add a new column “totalsale” by multiply “price” and “sales_quantity” columns,
# and group the data by “product_description” and “product_group” to generate the heatmap to check the product with highest sales.

