import pandas as pd
import sidetable

#below imports the sales dataset, but only selects certain columns
sales = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/sales_data_with_stores.csv",usecols= ["store","product_group","product_code",
                                                                                           "cost","price","last_week_sales"])

#below syntax should create a summary table for the product group variable
test = sales.stb.freq(["product_group"])

print(test)

################ IN CLASS EXERCISE ###########
#Download Salaries.csv from Canvas dataset folder, load it as a dataframe
salary = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/Salaries.csv")

#Use one statement to answer the following questions
##### How many ranks exist?
##### What is the size of rank in terms of the number of professors?
##### What is the cumulative salary of the entire portfolio?
rank = salary.stb.freq(["rank"])
print(rank)

##below would count the relative % of salary by rank
salary_rank = salary.stb.freq(["rank"], value='salary')
print(salary_rank)

print((salary.stb.freq(["rank"]),salary.stb.freq(["rank"], value='salary')))