import pandas as pd

#below would import a fake dataset labeled sales
sales = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/sales_data_with_stores.csv")

#below would sort the fake dataset sales above by price to get a sorted dataset of sales by the price column
sales_sorted = sales.sort_values(by='price')

#below would show the first 10 rows of the sorted sales dataset and only show store, price, stock_qty columns
#this would be handy if we wanted to select the stores with the highest prices
#this is an example of using the slicing function in conjunction with the sorting function to get a desired outcome
print(sales_sorted.loc[:,['store', 'price', 'stock_qty']].head(10))

#below gives the values in descending order instead of default ascending order
sales_sorted_desc = sales.sort_values(by='price', ascending=False)

#below would give the top 10 lowest stores by price
print(sales_sorted_desc.loc[:,['store', 'price', 'stock_qty']].head(10))

############## IN CLASS EXERCISE #################

#sort the flights by air_time and distance to find the longest flight
flights = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/flights.csv")

flights_sorted = flights.sort_values(by=['air_time', 'distance'], ascending=False)
print(flights_sorted.loc[:,['flight', 'air_time', 'distance']].head(10))
#the longest flight was flight 15
print(flights_sorted.dtypes)

#select the longest flight
print(flights_sorted.loc[:,['flight','air_time','distance']].head(1))