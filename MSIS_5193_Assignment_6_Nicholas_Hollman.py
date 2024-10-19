#Importing the Libraries
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

#### HOMEWORK ####

# Task 1. Write code to generate rules based your selected confidence and support thresholds (20 pts)
# (Hint: you might need to make the thresholds in the code much lower to get rules)

## import data
groceries_arm = pd.read_csv("C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Week 8 - Association Rule Mining\\groceriesARM.csv",header=None)

#get the shape of dataframe
print("Size of table: ",groceries_arm.shape)
print("No of Transactions: ",groceries_arm.shape[0])
print("No of items: ",groceries_arm.shape[1])

# fill the missing value with 0
groceries_arm.fillna(0,inplace=True)

# initialize an empty set to get all unique products
all_products = set()

#Finding all the unique products
for index, row in groceries_arm.iterrows():
    # update() method updates the current set, by adding items from row
    all_products.update(row)
print("Count of products: ",len(all_products))
print("Products: ",all_products)

# Remove '0' from the product list
all_products.remove(0)
print("Count of products: ",len(all_products))
print("Products: ",all_products)

# One Hot Encoding -- see PPT for details, making dataset in format desirable for function with Products as each column head and 0 or 1 for presence or absence in each row
encoded_vals = list()

# iterate through dataframe to convert each cell into 1 - has product or 0 - no product
for index, row in groceries_arm.iterrows():
    # set all cells in a row as 0
    rowset = {item:0 for item in all_products}

    # iterate through the row, if the item is no 0, set the value to be 1
    # this is using the original row value from the "in row" statement
    rowset.update({item:1 for item in row if item != 0 })

    # add the rowset to the list
    encoded_vals.append(rowset)

# convert the list into a new dataframe
encoded_vals_df = pd.DataFrame(encoded_vals)
print(encoded_vals_df)

# generate freq item sets using support threshold min_support=0.03
freq_items = apriori(encoded_vals_df, min_support=0.03,use_colnames=True)

# get the rules with confidence threshold set to 0.2
rules = association_rules(freq_items, metric="confidence", min_threshold=0.2)

# get the columns 'antecedents', 'consequents', 'support', 'confidence' from the rules
#antecendents is left side (X), consequents is right side (Y)
rules = rules[['antecedents', 'consequents', 'support', 'confidence']]

# sort the rules using "confidence" and "support", and show the top 20 rules
pd.set_option('display.max_columns', None)
print(rules.sort_values(["confidence","support"],ascending=[False, False]).reset_index(drop= True).head(20))