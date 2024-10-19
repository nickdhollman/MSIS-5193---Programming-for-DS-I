import pandas as pd

sales = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/sales_data_with_stores.csv")

############## BOOLEAN METHODS #############

#the below syntax filters the sales dataset to only rows with values of sales > 100
# operations: >, >= (greater than or equal to), <, <= (less than or equal to), ==, != (not equal)
sales_sub = sales[sales['price'] > 100]
print(sales_sub['price'])

# the below syntax builds off the filtering in the above dataset but filters off multiple criteria
# this statement would filter the sales data to only stores equal to violet and price greater than 100
sales_sub_b = sales[(sales['price'] > 100) & (sales['store'] == 'Violet')]
print(sales_sub_b[['price','store']])

############## PANDAS METHODS ###########
# below statement would build off above methods, keeping only stores with price greater than 100 and
# store equal to violet or rose, '|' represent OR
sales_sub_c = sales[(sales['price'] > 100) & ((sales['store'] == 'Violet') | (sales['store'] == 'Rose'))]
print(sales_sub_c[['price','store']])

# the below syntax produces the same result as the above statement, but uses the isin function which makes the syntax easier
sales_sub_d = sales[(sales['price'] > 100) & sales['store'].isin(['Violet', 'Rose'])]
print(sales_sub_d[['price','store']])

# the below syntax is the filtering process if you want to filter by a range of values, such as greater than or equal to 100
# and less than or equal to 151
sales_sub_e = sales[((sales['price'] >=100) & (sales['price'] <=150))]
print(sales_sub_e[['price','store']])

# the below syntax uses the between function and produces the same results as the above statement in a more efficient manner
sales_sub_f = sales[sales['price'].between(100,150)]
print(sales_sub_f[['price','store']])