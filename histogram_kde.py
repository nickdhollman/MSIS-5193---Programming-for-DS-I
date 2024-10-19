import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# load data into dataframe
loan = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/train_Loan.csv")

# draw the histogram with KDE
sns.set_style('darkgrid')
sns.displot(loan['LoanAmount'],kde=True)
plt.xlabel('LoanAmount($)')
plt.ylabel('Frequency(n)')
plt.title('Histogram of Loan Amount with Kernel Density Estimation')
plt.subplots_adjust(top=0.9)
plt.show()

# load data into dataframe
stockapp = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/apple_stock_prices_2022.csv")

# draw the histogram using two variables (open and close price) with KDE
sns.set_style('darkgrid')
sns.histplot(data=stockapp,x="Open",label="Open", kde=True)
sns.histplot(data=stockapp, x="Close", color="red", label="Close", kde=True)
plt.xlabel('')
plt.ylabel('Frequency(n)')
plt.title('Histogram of Stock Price type with Kernel Density Estimation')
plt.subplots_adjust(top=0.9)
plt.legend()
plt.show()

## Class exercise
#Normalize the column Price and SalesQty in file mock_sales_data.csv, then generate histogram to see their distribution.


