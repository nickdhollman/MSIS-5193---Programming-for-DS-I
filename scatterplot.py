# import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# load a build-in data set 'tips'
tips =sns.load_dataset('tips')
print(tips)

# check the relation between day and tips
plt.scatter(tips['day'], tips['total_bill'])
plt.title('Scatter plot day vs. total_bill')
plt.xlabel('day')
plt.ylabel('total_bill')
plt.show()

