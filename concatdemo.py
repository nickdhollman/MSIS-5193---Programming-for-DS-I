import pandas as pd

# create demo dataframe df1
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                    index=[0, 1, 2, 3])

# create demo dataframe df2
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                    index=[4, 5, 6, 7])

# create demo dataframe df3
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                    index=[8, 9, 10, 11])



# define the order of concatenate
frames = [df1, df2, df3] # this means you are going to stack df1 on top of df2 which will be on top of df3

# concatenate data and save to a new variable result
result = pd.concat(frames)

# show result
print(result)


# define a series - a list
series1 = ['X0', 'X1', 'X2', 'X3']

# convert the series into a dataframe, and add a name 'X' to the column
s1 = pd.Series(series1, name='X')
print(s1)

# concatenate df1 and s1 by column wise
result = pd.concat([df1, s1], axis=1) #### axis=1 is specifying you are doing the concatenation columnwise, axis=0 is specifying you are concatenating rowwise
print(result)


# load data
Salary_1= pd.read_csv('C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Week 5 - Connect to SQL and Data Joins\\basic_salary - 1.csv')
Salary_2= pd.read_csv('C:\\Users\\nickd\\OneDrive - Oklahoma A and M System\\Programming for Data Science\\Week 5 - Connect to SQL and Data Joins\\basic_salary - 2.csv')
print(Salary_1.head)
print(Salary_1.shape)
print(Salary_2.head)
print(Salary_2.shape)

# concatenate data frames
appendsalary=pd.concat([Salary_1,Salary_2])
print(appendsalary.shape)

print(appendsalary)

#CLASS EXERCISE
d1 = pd.DataFrame({"Name":["Pankaj", "Lisa"], "ID":[1,2], "Department":["hr","sales"]})
print(d1)
d2 = pd.DataFrame({"Role":["Admin","Editor"], "ID":[1,2]})
print(d2)

d2_ = d2.drop('ID', axis=1)
result = pd.concat([d1, d2_], axis=1) #### axis=1 is specifying you are doing the concatenation columnwise, axis=0 is specifying you are concatenating rowwise
print(result)