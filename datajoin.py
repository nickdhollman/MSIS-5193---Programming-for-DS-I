# import library
import pandas as pd

# import data
df1 = pd.read_csv("C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Week 5 - Connect to SQL and Data Joins\\customers.csv",encoding='latin-1')
df2 = pd.read_csv("C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Week 5 - Connect to SQL and Data Joins\\employees.csv",encoding='latin-1')
df3 = pd.read_csv("C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Week 5 - Connect to SQL and Data Joins\\orders.csv",encoding='latin-1')
df4 = pd.read_csv("C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Week 5 - Connect to SQL and Data Joins\\payments.csv",encoding='latin-1')

#print(df1, df2, df3)

# apply full outer join
print(df1.dtypes, df3.dtypes)
df_outer = pd.merge(df1, df3, on="customerNumber", how='outer')
pd.set_option('display.max_columns', None) #show all columns
print(df_outer)


# apply left join
print(df2.dtypes)
df_left = pd.merge(df1, df2, left_on='salesRepEmployeeNumber',right_on='employeeNumber', how='left')
pd.set_option('display.max_columns', None) #show all columns
print(df_left)

# apply inner join
df_inner = pd.merge(df1, df2, left_on='salesRepEmployeeNumber',right_on='employeeNumber', how='inner')
pd.set_option('display.max_columns', None) #show all columns
print(df_inner)

# apply right join
df_outer = pd.merge(df1, df2, left_on='salesRepEmployeeNumber',right_on='employeeNumber', how='right')
pd.set_option('display.max_columns', None) #show all columns
print(df_outer)

# join customer and payment csv, then get the total number of payments by each customer
print(df1.dtypes)
print(df4.dtypes)
# join on customer number
df_inner_class = pd.merge(df1, df4, left_on='customerNumber',right_on='customerNumber', how='inner')
pd.set_option('display.max_columns', None) #show all columns
print(df_inner_class)
# calculate the total amount of payments by each customer
Payment_by_cust = df_inner_class.groupby("customerNumber")[["amount"]].agg(["sum"])
print(Payment_by_cust)


