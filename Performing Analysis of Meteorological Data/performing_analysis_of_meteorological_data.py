import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

filepath = 'weatherHistory.csv'
data = pd.read_csv(filepath)
data.head()

data.shape

data.info

data['Loud Cover'].unique()

data.drop(['Loud Cover'], axis = 1, inplace = True)
data.head()

# now check for missing columns
data.isna().sum()

# Setting plot style
sns.set_style(style = 'whitegrid')

data.describe()

"""**YEAR-WISE ANALYSIS**"""

#Resampling the data year-wise by mean

indices = [2,4,6,7,8]
year_data = data.iloc[:,indices].resample('Y').mean()
year_data.head()

year_data.describe()

for ind in range(len(year_data.columns)):
    sns.distplot(year_data.iloc[:,ind])
    plt.show()

year_data.corr()

#normalizing year data

normal_data = (year_data - year_data.min())/ (year_data.max() - year_data.min())
normal_data.head()

#Line graph representation
plt.figure(figsize=(12,6))
plt.xlabel('YEAR')
plt.ylabel('LINE PLOT', fontsize=30)
sns.lineplot(data = normal_data, marker = 's')
plt.show()

#Box Plot
plt.figure(figsize = (10,4))
plt.title('BOX PLOT', fontsize=30)
sns.boxplot(data = normal_data)
plt.show()

# Heatmap
plt.figure(figsize=(6,8))
plt.title('HEATMAP', fontsize=25)
sns.heatmap(normal_data, annot=True, cmap='Blues',
            yticklabels=normal_data.index.year)
plt.show()

"""**Temperature vs Humidity**"""

data.head(1)

#Resampling data month-wise by mean
monthly_data = data.iloc[:,3:5].resample('M').mean()
monthly_data.head()

monthly_data.describe()

#Graphical representation
plt.figure(figsize=(14,5))
plt.title('Apparent Temperature vs Humidity')
sns.lineplot(x=monthly_data.iloc[:,0],
             y=monthly_data.iloc[:,1],
             color='green')
plt.show()

# Regression plot for Apparent Temperature & Humidity
plt.figure(figsize=(10,5))
plt.title('Apparent Temperature vs Humidity')
sns.regplot(x=monthly_data.iloc[:,0],
            y=monthly_data.iloc[:,1])
plt.show()

plt.figure(figsize=(10,5))
plt.xlabel('YEAR')
plt.title('Variation of Apparent Temperature and Humidity')
sns.lineplot(data=monthly_data)
plt.show()

print(monthly_data.corr())
sns.pairplot(monthly_data, kind = 'scatter')
plt.show()

"""ANALYSIS ON NORMALIZED DATA"""

# Normalizing data
temp = monthly_data
normed_data = (temp - temp.min()) / (temp.max() - temp.min())
normed_data.head()

# Line graph representation of normalized data
plt.figure(figsize=(12,6))
plt.title('Apparent Temperature & Humidity - Normalized')
plt.xlabel('YEAR', fontsize=12)
sns.lineplot(data=normed_data)
plt.show()

# Correlation of variables
sns.pairplot(normed_data, kind='reg')
plt.show()
