#Libraries
from mysql.connector import connection
import csv
import pandas as pd

# connect to DB server
cnx = connection.MySQLConnection(user='readonlyuser', password='Fall2024Msis5193!',
                                 host='34.66.134.201',
                                 database='Northwind')

# initialize the cursor
cursor = cnx.cursor() # uncomment the below section when running the product excel file creation code, then recomment to run the category excel file creation code
'''
# Show tables
cursor.execute("show tables")
for x in cursor:
    print(x)

# select and print product and category
cursor.execute("select * from Product")
for x in cursor:
    print(x)
cursor.execute("select * from Category")
for x in cursor:
    print(x)

# select Product to export to csv
cursor.execute("select * from Product")

# initialize a cursor to execute SQL statement
print(cursor.description)
num_fields = len(cursor.description)
field_names = [i[0] for i in cursor.description]
print(field_names)
'''
# save the table to a file Products.csv
'''
with open('Product.csv', 'w', newline='')  as fp:
    writer = csv.writer(fp)
    writer.writerow(field_names)
    for x in cursor:
        print(list(x))
        writer.writerow(list(x))
        '''

# select Category to export to csv #### uncomment the below section when running the category excel file creation code
'''
cursor.execute("select * from Category")

# initialize a cursor to execute SQL statement
print(cursor.description)
num_fields = len(cursor.description)
field_names = [i[0] for i in cursor.description]
print(field_names)

# save the table to a file Category.csv
with open('Category.csv', 'w', newline='')  as fp:
    writer = csv.writer(fp)
    writer.writerow(field_names)
    for x in cursor:
        print(list(x))
        writer.writerow(list(x))
'''

#close database
cnx.close()

#import CSV files
Product = pd.read_csv("C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Week 5 - Connect to SQL and Data Joins\\Product.csv",encoding='latin-1')
Category = pd.read_csv("C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Week 5 - Connect to SQL and Data Joins\\Category.csv",encoding='latin-1')
print(Product.head)
print(Product.dtypes)
print(Product.shape)
print(Category.head)
print(Category.dtypes)
print(Category.shape)

#join product and category
Product_cat = pd.merge(Product, Category, left_on='categoryId',right_on='categoryId', how='left')
pd.set_option('display.max_columns', None) #show all columns
print(Product_cat)
#verify it worked correctly with dtypes and shape
print(Product_cat.dtypes)
print(Product_cat.shape)

#get the number of products in each category
#below syntax creates a list of the unique values of products by each category
unique = Product_cat.groupby("categoryId",as_index=False).agg(unique_values = ("productId", "unique"))
print(unique)

#below syntax applies the principles above but counts the number of unique values of product ID instead of a list of values
nunique = Product_cat.groupby("categoryId",as_index=False).agg(number_of_unique_products = ("productId", "nunique"))
print(nunique)

#repeat above with cateroryName and productName
unique_products = Product_cat.groupby("categoryName",as_index=False).agg(unique_products = ("productName", "unique"))
print(unique_products)

#below syntax applies the principles above but counts the number of unique values of product Name instead of a list of values
nunique_products = Product_cat.groupby("categoryName",as_index=False).agg(number_of_unique_products = ("productName", "nunique"))
print(nunique_products)

#export result of nunique products to csv file
nunique_products_csv = nunique_products.to_csv('Number of Products in Each Category.csv', index = False)