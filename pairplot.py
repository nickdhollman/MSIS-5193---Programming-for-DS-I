# importing packages
import seaborn
import matplotlib.pyplot as plt
import pandas as pd

# loading dataset using seaborn
df = seaborn.load_dataset('tips')

# pairplot
seaborn.pairplot(df)
plt.show()

# pairplot with hue sex
seaborn.pairplot(df, hue='sex')
plt.show()

# loading dataset using seaborn
df = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/sales_data_with_stores.csv")

# drop the columns that are not needed - this is to reduce the size of the visualization as pairplot will do visualizations
# for all bivariate relationships
dfnew = df.drop(['last_week_sales','last_month_sales'], axis=1)

# pairplot with hue store
seaborn.pairplot(dfnew, hue='store')
plt.show()

### In class exercise - Use the groceries.csv, drop the product_code and sales_date,
# then generate the pairplot to understand the correlations between the price and sales_quantity with regards to product_group.

