import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
import math
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from yellowbrick.regressor import ResidualsPlot
from sklearn import decomposition
#Part II of lab
df = pd.read_csv('C:/Users/Rachel/Downloads/melb_data.csv')

#Q1

sns.displot(data = df, x = 'Price')

print(df.describe())

plt.show()

#Q2

df['BuildingArea'] = df['BuildingArea'].fillna(value = 0)
df['Car'] = df['Car'].fillna(value = 0)

def fill_empty(row):
    if math.isnan(row):
        return np.random.randint(1900,2018)
    return row

df['YearBuilt'] = df['YearBuilt'].apply(fill_empty)


#Q3

df = df.drop(columns = ['Suburb', 'Date', 'Address', 'SellerG', 'CouncilArea', 'Longtitude', 'Lattitude', 'Propertycount', 'YearBuilt'])


#Q4

#label encoding 
le = preprocessing.LabelEncoder()
df['Regionname'] = le.fit_transform(df['Regionname'])
df['Method'] = le.fit_transform(df['Method'])

#one- hot encoding

oh = preprocessing.OneHotEncoder()

new_columns = pd.DataFrame(oh.fit_transform(df[['Type']]).toarray())
df = df.join(new_columns)

df = df.drop('Type', axis = 1)

df = df.rename(columns = {0 : 'Type h', 1 : 'Type u', 2 : 'Type t'} )

print(df)

#Q5

df['Mean Price by Type'] = df.groupby('Bedroom2')['Price'].transform('mean')

df['Mean Price by Region'] = df.groupby('Regionname')['Price'].transform('mean')

df['Standard Deviation of Price by Rooms'] = df.groupby('Rooms')['Price'].transform('std')

#fix this somehow?
df['Standard Deviation of Price by Rooms'] = df['Standard Deviation of Price by Rooms'].fillna(value = 0)

print(df)

#Q6

#Q7

y_data = df['Price']
x_data = df.drop(columns = ['Price'])

#Q8

scaler = StandardScaler()
x_data = scaler.fit_transform(x_data)

#Q9

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size  = .10, random_state = 1)

#PART II

#Q1
lin_reg = linear_model.LinearRegression()

sgd_reg = linear_model.SGDRegressor()

model_linear = lin_reg.fit(x_train, y_train)

model_sgd = sgd_reg.fit(x_train, y_train)


#PART 3

#1 and #2


lin_accuracy = []
sgd_accuracy = []

lin_accuracy.append(model_linear.score(x_test, y_test))
sgd_accuracy.append(model_sgd.score(x_test, y_test))


#Q3
#20%
x_train2, x_test2, y_train2, y_test2 = train_test_split(x_data, y_data, test_size  = .30, random_state = 1)
model_linear2 = lin_reg.fit(x_train2, y_train2)
model_sgd2 = sgd_reg.fit(x_train2, y_train2)
lin_accuracy.append(model_linear2.score(x_test2, y_test2))
sgd_accuracy.append(model_sgd2.score(x_test2, y_test2))

#30% testing
x_train3, x_test3, y_train3, y_test3 = train_test_split(x_data, y_data, test_size  = .30, random_state = 1)
model_linear3 = lin_reg.fit(x_train3, y_train3)
model_sgd3 = sgd_reg.fit(x_train3, y_train3)
lin_accuracy.append(model_linear3.score(x_test3, y_test3))
sgd_accuracy.append(model_sgd3.score(x_test3, y_test3))

#40% testing
x_train4, x_test4, y_train4, y_test4 = train_test_split(x_data, y_data, test_size  = .30, random_state = 1)
model_linear4 = lin_reg.fit(x_train4, y_train4)
model_sgd4 = sgd_reg.fit(x_train4, y_train4)
lin_accuracy.append(model_linear4.score(x_test4, y_test4))
sgd_accuracy.append(model_sgd4.score(x_test4, y_test4))

#50% testing
x_train5, x_test5, y_train5, y_test5 = train_test_split(x_data, y_data, test_size  = .50, random_state = 1)
model_linear5 = lin_reg.fit(x_train5, y_train5)
model_sgd5 = sgd_reg.fit(x_train5, y_train5)
lin_accuracy.append(model_linear5.score(x_test5, y_test5))
sgd_accuracy.append(model_sgd5.score(x_test5, y_test5))

#60% testing
x_train6, x_test6, y_train6, y_test6 = train_test_split(x_data, y_data, test_size  = .30, random_state = 1)
model_linear6 = lin_reg.fit(x_train6, y_train6)
model_sgd6 = sgd_reg.fit(x_train6, y_train6)
lin_accuracy.append(model_linear6.score(x_test6, y_test6))
sgd_accuracy.append(model_sgd6.score(x_test6, y_test6))


#70% test
x_train7, x_test7, y_train7, y_test7 = train_test_split(x_data, y_data, test_size  = .70, random_state = 1)
model_linear7 = lin_reg.fit(x_train7, y_train7)
model_sgd7 = sgd_reg.fit(x_train7, y_train7)
lin_accuracy.append(model_linear7.score(x_test7, y_test7))
sgd_accuracy.append(model_sgd7.score(x_test7, y_test7))

#80% testing
x_train8, x_test8, y_train8, y_test8 = train_test_split(x_data, y_data, test_size  = .30, random_state = 1)
model_linear8 = lin_reg.fit(x_train8, y_train8)
model_sgd8 = sgd_reg.fit(x_train8, y_train8)
lin_accuracy.append(model_linear8.score(x_test8, y_test8))
sgd_accuracy.append(model_sgd8.score(x_test8, y_test8))


#90% test
x_train9, x_test9, y_train9, y_test9 = train_test_split(x_data, y_data, test_size  = .90, random_state = 1)
model_linear9 = lin_reg.fit(x_train9, y_train9)
model_sgd9 = sgd_reg.fit(x_train9, y_train9)
lin_accuracy.append(model_linear9.score(x_test9, y_test9))
sgd_accuracy.append(model_sgd9.score(x_test9, y_test9))


percent_array = [.10,.20, .30, .40, .50,.60, .70,.80, .90]



plt.plot(lin_accuracy, percent_array)
plt.title('Accuracy for Different Percentages of Testing Data- Linear Regression')

plt.show()
plt.plot(sgd_accuracy, percent_array)
plt.title('Accuracy for Different Percentages of Testing Data- SGD Regression')

plt.show()

#Q4

visual = ResidualsPlot(model_linear)

visual.fit(x_data,y_data)
visual.score(x_train, y_train)
visual.poof()

#Q5

