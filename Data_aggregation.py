import pandas as pd

sales = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/sales_data_with_stores.csv")

#below syntax calculates the mean of stock_qty and price by store and stores it as a print variable groupbystore
groupbystore = sales.groupby('store')[["stock_qty","price"]].mean()

print(groupbystore)

#below calculates the mean and max of stock_qty and price variables in the sales dataset, and stores it to a print variable groupbystoremulti
groupbystoremulti = sales.groupby("store")[["stock_qty","price"]].agg(["mean", "max"])

print(groupbystoremulti)

#below syntax creates a new dataframe newdf (because of as_index=False), and stores the aggregate functions created below
#as avg_stock_qty and avg_price from using avg_stock_qty = and avg_price =
newdf = sales.groupby("store", as_index=False).agg(avg_stock_qty = ("stock_qty", "mean"), avg_price = ("price", "mean"))
print(newdf)

#below syntax creates a new dataframe that does a similar function as above but groups by store and product group and sorts in descending order
newdf_sort = (sales.groupby(["store", "product_group"],
                            as_index=False).agg(avg_sales = ("last_week_sales", "mean")).sort_values(by="avg_sales",ascending=False).head())

print(newdf_sort)

#below syntax applies the principles above but also creates a list of the unique values of product code
unique = sales.groupby("store",as_index=False).agg(unique_values = ("product_code", "unique"))
print(unique)

#below syntax applies the prinicples above but counts the number of unique values of product code instead of a list of values
nunique = sales.groupby("store",as_index=False).agg(number_of_unique_values = ("product_code", "nunique"))
print(nunique)

########## IN CLASS EXERCISE #######
#Find out the total number of flights based on the combination of origin and dest
flights = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/flights.csv")
print(flights.dtypes)

nunique_origin = flights.groupby("origin",as_index=False).agg(number_of_unique_values = ("flight", "nunique"))
print(nunique_origin)

nunique_dest = flights.groupby("dest",as_index=False).agg(number_of_unique_values = ("flight", "nunique"))
print(nunique_dest)

nunique_origin_dest = flights.groupby(["dest","origin"], as_index=False).agg(number_of_unique_values = ("flight","nunique"))
print(nunique_origin_dest)


