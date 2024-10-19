import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn import preprocessing

# load data
loan = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/train_Loan.csv")

# prepare subplots to enable the creation of dual axis
fig, ax = plt.subplots(figsize=(12,5))

# Create a new Axes with an invisible x-axis and an
# independent y-axis positioned opposite
# to the original one (i.e. at right).
# twinx function creates another invisible x-axis and an independent y-axis
ax2 = ax.twinx()

# add title to the figure, and set the label
# for x-axis as empty
ax.set_title('Applicant Income and Loan Amount')
ax.set_xlabel('')

# plot values, one on ax, the other on ax2 - ax2 is the second axis created with the twinx function
ax.plot(loan['Loan_ID'], loan['ApplicantIncome'], color='green', marker='x')
ax2.plot(loan['Loan_ID'], loan['LoanAmount'], color='red', marker='o')

# plot the labels for ax and ax2
ax.set_ylabel('Applicant Income')
ax2.set_ylabel('Loan Amount')

# add legend to figure - loc sets the location of the legend
ax.legend(['Applicant Income'])
ax2.legend(['Loan Amount'], loc='upper center')

# remove the xticks to tidy the figure
ax.set_xticks([])
ax2.set_xticks([])

# add a grid to the figure
ax.yaxis.grid(color='lightgray', linestyle='dashed')

# show figure
plt.show()

############ Class Exercise
# Load the apple_google_stock_prices_092022.csv file.
# Draw a figure to show whether the close price of APPLE and GOOGLE has any correlation.
# (hint: use filter to separate APPLE and GOOGLE into two dataframes first)



