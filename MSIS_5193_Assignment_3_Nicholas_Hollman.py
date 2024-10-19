#import libraries
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sidetable

######## TASK #1 ##########

#load wine dataset
wine = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/Wine.csv")
print(wine.shape)
#999 rows, 12 columns
print(wine.head())
print(wine.dtypes)

# 1 -Draw a bar chart using ‘quality’ and ‘alcohol’ column to see if the quality level has any relationship with the alcohol amount

# Descriptive stats
print(wine.stb.freq(['quality']))
# 6 categoeries ranging from three - eight
print(wine.stb.freq(['alcohol']))
# continuous in nature so freq does not provide much
print(wine['alcohol'].agg(['min','median', 'mean','max']))
print(wine['alcohol'].quantile([0.25, 0.75]))

#Generate bar plot
#plt.figure(figsize=(13, 6))
#one variable plots
sns.countplot(x=wine["quality"],order=wine.quality.value_counts().iloc[:6].index, palette="tab10")
plt.show()
sns.displot(wine['alcohol'],kde=True)
plt.show()
#Bivariate plot
#sns.catplot(x="quality", y="alcohol", kind="box", data=wine, order=wine.quality.value_counts().iloc[:6].index)
#plt.show()
sns.catplot(x="quality", y="alcohol", kind="box", data=wine, order=['three','four','five','six','seven','eight'])
plt.title('Alcohol Amount by Quality Level')
plt.xlabel('Quality Level')
plt.ylabel('Alcohol Amount')
plt.subplots_adjust(top=0.9)
plt.show()
#order_means=wine.groupby(['quality'])['alcohol'].mean().sort_values(ascending=True)
#sns.catplot(x="quality", y="alcohol", kind="box", data=wine, order=order_means.index)
#plt.show()

# 2 Draw a histogram plot using ‘total sulfur dioxide’, and explain what you learn from the figure
#descriptive stats
print(wine['total sulfur dioxide'].agg(['min','median', 'mean','max']))
print(wine['total sulfur dioxide'].quantile([0.25, 0.75]))
sns.displot(wine['total sulfur dioxide'],kde=True)
plt.title('Distribution of total sulfur dioxide')
plt.xlabel('Total sulfur dioxide')
plt.ylabel('Frequency (n)')
plt.subplots_adjust(top=0.9)
plt.show()

# 3 - Draw a scatter plot using `residual sugar’ and ‘quality’, and explain what you learn from the figure
#descriptive stats
print(wine['residual sugar'].agg(['min','median', 'mean','max']))
print(wine['residual sugar'].quantile([0.25, 0.75]))

plt.scatter(wine['quality'], wine['residual sugar'])
plt.title('Scatter plot Quality Level vs. Residual Sugar')
plt.xlabel('Quality Level')
plt.ylabel('Residual Sugar')
plt.show()

# 4 - Draw a hexbin plot using `residual sugar’ and ‘alcohol’, and explain what you learn from the figure
wine.plot.hexbin(x='alcohol', y='residual sugar', gridsize=30) #gridsize specifies how big the hexagon will be
plt.title('Hexbin plot of Alcohol Amount vs. Residual Sugar')
plt.xlabel('Alcohol Amount')
plt.ylabel('Residual Sugar')
plt.show()


######## TASK #2  - Use country_population_historic.csv ##########

# load data and get shape, dtype, head
country = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/country_population_historic.csv")
print(country.shape)
#266 rows, 64 columns
print(country.head())
print(country.dtypes)

# 1 - (1)	Select the 10 countries with the largest population in the year 1960,
# use the heatmap to show the changes of the populations of these 10 countries from 1960 to 1970

#filter dataset to year 1960-1970
country_1960_970 = country.iloc[:,0:12]
print(country_1960_970.dtypes)
country_sorted = country_1960_970.sort_values(by ='1960', ascending=False)
print(country_sorted[['Country Name','1960']].head(10))
top_country_sorted= country_sorted.head(10)
print(top_country_sorted)


# draw heatmap
# create "Year" variable from 1960 - 1970 columns, create "Population" from column values
country_long = pd.melt(top_country_sorted, id_vars=['Country Name'], value_vars=['1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970'],
                       var_name='Year', value_name='Population')
print(country_long)


# index is the y-axis, columns is the x-axis, value is the cell
#### TO - DO - STILL NEED TO FLIP Y-AXIS LABELS TO BE HORIZONTAL
country_heat = country_long.pivot(index="Year", columns="Country Name", values="Population")
plt.figure(figsize=(20, 8))
sns.heatmap(country_heat,annot=True,cmap='RdYlGn',linewidths=0.30)
plt.title("Population Heatmap by Country")
plt.xticks(rotation=30, ha='right')
plt.yticks(rotation=90)
plt.subplots_adjust(bottom=0.2)
plt.show()

#problem is this plot does not show country names but also shows regions, descriptor etc.
#under the column "Country Name"
#import list of country names found on web
country_name = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/Country_name.csv")
print(country_name.head())
print(country_name.shape)

#innerjoin countr_name and country by "Country Name" to only keep countries in dataset
country_only =country.merge(country_name,how="inner",on="Country Name")
print(country_only.head())

#re-run code above that produced first plot to keep only top 10 countries pop in 1960 but
#excluding region, etc. by using country_only dataset
#filter dataset to year 1960-1970
country_only_1960_970 = country_only.iloc[:,0:12]
print(country_only_1960_970.dtypes)
country_only_sorted = country_only_1960_970.sort_values(by ='1960', ascending=False)
print(country_only_sorted[['Country Name','1960']].head(10))
top_country_only_sorted= country_only_sorted.head(10)
print(top_country_only_sorted)


# draw heatmap
# create "Year" variable from 1960 - 1970 columns, create "Population" from column values
country_only_long = pd.melt(top_country_only_sorted, id_vars=['Country Name'], value_vars=['1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970'],
                       var_name='Year', value_name='Population')
print(country_only_long)


# index is the y-axis, columns is the x-axis, value is the cell
#### TO - DO - STILL NEED TO FLIP Y-AXIS LABELS TO BE HORIZONTAL
country_only_heat = country_only_long.pivot(index="Year", columns="Country Name", values="Population")
plt.figure(figsize=(20, 8))
sns.heatmap(country_only_heat,annot=True,cmap='RdYlGn',linewidths=0.30)
plt.title("Population Heatmap by Country")
plt.xticks(rotation=30, ha='right')
plt.yticks(rotation=90)
plt.subplots_adjust(bottom=0.2)
plt.show()
