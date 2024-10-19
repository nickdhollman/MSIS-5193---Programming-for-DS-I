import matplotlib.pyplot as plt
import pandas as pd

# load data into dataframe
loan = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/train_Loan.csv")

# create bins by list the boundaries of the bins,
# draw histogram based on LoanAmount
ax = plt.hist(loan['LoanAmount'], bins=[100, 200, 300, 400, 500])
plt.xlabel('LoanAmount($)')
plt.ylabel('Frequency(n)')
plt.title('Histogram of Loan Amount')
plt.show()

# specify the number of bins
plt.hist(loan['LoanAmount'], bins=10)
plt.xlabel('LoanAmount($)')
plt.ylabel('Frequency(n)')
plt.title('Histogram of Loan Amount')
plt.show()
