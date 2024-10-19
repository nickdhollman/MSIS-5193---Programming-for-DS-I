import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn import preprocessing

# load data
loan = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/train_Loan.csv")

# fill missing values
loan[['ApplicantIncome']] = loan[['ApplicantIncome']].ffill()
loan[['LoanAmount']] = loan[['LoanAmount']].ffill()

# normalize data
scaler = preprocessing.MinMaxScaler()
loan[['LoanAmount']] = scaler.fit_transform(loan[['LoanAmount']])
loan[['ApplicantIncome']] = scaler.fit_transform(loan[['ApplicantIncome']])

# plot charts
plt.plot(loan['LoanAmount'])
plt.plot(loan['ApplicantIncome'])

# add title, legend and labels for x-axis, and y-axis
plt.legend(['LoanAmount','ApplicantIncome'])
plt.title('Loan Amount vs. Applicant Income')
plt.xlabel('')
plt.ylabel('$')

# show figure
plt.show()

