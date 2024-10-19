import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn import preprocessing

# Read a dataset
loan = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/train_Loan.csv")
print(loan.head())
print(loan.dtypes)
print(loan.isnull().sum())

# impute missing value
loan['LoanAmount'] = loan['LoanAmount'].fillna(loan['LoanAmount'].mean())
print(loan['LoanAmount'])

# initialize min-max normalization scaler
scaler = preprocessing.MinMaxScaler()

# normalize LoanAmount
loan[['LoanAmount']] = scaler.fit_transform(loan[['LoanAmount']])

# show normalized values
print(loan[['LoanAmount']])

# initialize z-score normalization scaler
scalerzscore = preprocessing.StandardScaler()

# normalize LoanAmount
loan[['LoanAmount']] = scalerzscore.fit_transform(loan[['LoanAmount']])

# show normalized values
print(loan[['LoanAmount']])

# create a dataframe to show removing duplicates
df = pd.DataFrame({
    'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
    'style': ['cup', 'cup', 'cup', 'pack', 'pack'],
    'rating': [4, 4, 3.5, 15, 5]
})
print(df)

# remove duplicates based on all columns
dfnew = df.drop_duplicates()

# show results
print(dfnew)

# remove duplicates based on column 'brand'
dfnew_ = df.drop_duplicates(subset=['brand'])

# show results
print(dfnew_)

# remove duplicates based on columns 'brand' and 'style'
dfnew_both = df.drop_duplicates(subset=['brand', 'style'], keep='last')

# show results
print(dfnew_both)

#keep first
dfnew_both_ = df.drop_duplicates(subset=['brand', 'style'], keep='first')

# show results
print(dfnew_both_)

### Class - ex - impute all numerical columns of the loan data and normalize them using Z-score
loan = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/train_Loan.csv")
print(loan.head())
print(loan.dtypes)
#numerical columns: ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History
print(loan.isnull().sum())
print(loan[['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History']])
scalerzscore = preprocessing.StandardScaler()

# normalize LoanAmount
'''
loan[['ApplicantIncome']] = scalerzscore.fit_transform(loan[['ApplicantIncome']])
loan[['CoapplicantIncome']] = scalerzscore.fit_transform(loan[['CoapplicantIncome']])
loan[['LoanAmount']] = scalerzscore.fit_transform(loan[['LoanAmount']])
loan[['Loan_Amount_Term']] = scalerzscore.fit_transform(loan[['Loan_Amount_Term']])
loan[['Credit_History']] = scalerzscore.fit_transform(loan[['Credit_History']])

# show normalized values
print(loan[['ApplicantIncome','CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History']])
'''

#try more efficient code
loan[['ApplicantIncome','CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History']] = scalerzscore.fit_transform(loan[['ApplicantIncome','CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History']])

print(loan[['ApplicantIncome','CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History']])