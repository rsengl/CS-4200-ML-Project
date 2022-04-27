import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv('C:/Users/Rachel/Downloads/melb_data.csv')
df = df.dropna()

print(df.describe())
sns.lineplot(data = df, x = 'Bedroom2', y = 'Price')
sns.lineplot(data = df, x = 'Landsize', y = 'Price')

sns.lmplot(data = df, x = 'Bedroom2', y = 'Price', hue = 'Regionname')
sns.lineplot(data = df, x = 'Bathroom', y = 'Price')

sns.lineplot(data  = df, x = 'Car', y = 'Price')
sns.lineplot(data = df, x = 'Rooms', y = 'Price', hue = 'Type')

sns.lineplot(data = df, x = 'Distance', y = 'Price')
sns.lineplot(data = df, x = 'BuildingArea', y = 'Price')

plt.show()

df = df.drop(columns = ['Suburb', 'Address', 'SellerG', 'CouncilArea', 'Longtitude', 'Lattitude','Regionname', 'Propertycount', 'YearBuilt'])

plot = sns.pairplot(df)

plt.show()


df['Mean Price'] = df.groupby('Type')['Price'].transform('mean')

print(df['Mean Price'])


sns.lineplot(data = df, x = 'Bedroom2', y = 'Mean Price')

plt.show()