# Part One
The link to the dataset used for the code and the graphs is as follows:
https://www.kaggle.com/datasets/dansbecker/melbourne-housing-snapshot?select=melb_data.csv



First, we have the effect of additional car spaces on housing prices:

![image](https://user-images.githubusercontent.com/104324776/164999512-cd5d3b95-f4ea-47c0-8a77-717993893fc2.png)

It is clear that as the number of car spaces increases, the price of the house also increases. 

The affect of rooms on housing prices by type, where h is a house, cottage, villa, semi, or terrace, u is a unit or duplex, and t is a townhouse:

![Room affect on Price by type](https://user-images.githubusercontent.com/104324776/164999615-beedfb9f-ecb1-411e-b325-fd5e6779a9ab.png)

Out of all of the housing types, we can see that for a house, cottage, villa, semi, or terrace, the prices seem to be the highest and the unit or duplex prices seem to be the lowest. However, out of all the housing types, as the rooms increase, the price also increases.

The affect of distance to a central business district:

![Distance on pRice](https://user-images.githubusercontent.com/104324776/164999629-e3cef68d-2fae-4807-8baa-ac6d40a2a741.png)

It appears that as the distance to a central business district is smaller, the price increases. This could be due to the lack of land in more urban areas.

The affect of building areas on price:

![Bulding area on Price](https://user-images.githubusercontent.com/104324776/164999648-ac557bba-1507-459a-9693-ec55a123dfd0.png)

Generally, as the building area increases, the housing price increases. 

The bedroom affect on prices by area:

![Bedroom affect on Prices by Area](https://user-images.githubusercontent.com/104324776/164999653-5dc4ac50-edff-485e-aa05-cc2e28781593.png)

We can see that the housing prices are generally higher in the Southern Metropolitan Region and lower in the Northern Victoria, Western Victoria, and Eastern Victoria areas. However, across all areas as the number of bedrooms increase the price increases. The affect of additional bedrooms appears to be larger for the Southern Metropolitan area than other areas. 


The bathroom affect on price:

![Bathroom effect on price](https://user-images.githubusercontent.com/104324776/164999670-95994c09-026a-4baf-baa5-c017194e269e.png)

Generally, as the number of bathrooms increases, the housing price increases. 

The land amount affect on price:

![Land affect on Price](https://user-images.githubusercontent.com/104324776/164999682-7ff60c44-1b7c-42c7-9217-5be581b89e17.png)

We can se that there are larger housing prices for smaller areas of land rather than larger areas of land. 

Then, there are the following pair plots for some of the dataset:

![Pairplot Project](https://user-images.githubusercontent.com/104324776/165000508-0c3651d6-f75f-4f0a-ac13-783238d99893.png)

We can see that the number of bathrooms and bedroooms is correlated to the total rooms in the house. Other than these variables being clearly positively correlated, there does not appear to be other clearly correlated variables. We can also see that for the building area column and the land column, most of the data is within a certain range with only a few outliers. 

Then, we also have the following aggregate plot 

![Aggregate Plot](https://user-images.githubusercontent.com/104324776/165621778-eec9b472-e32c-4a22-b7da-737ee7319425.png)

This comes from a groupby, grouping type by price and then finding the mean of these prices. Then, this data was graphed against the number of bedrooms, as the bedrooms are a key component in find the housing prices. We can see that the mean price does in fact increase as the number of bedrooms increases. 


My plan is to predict the housing prices based on some of the numerical or categorical variables given in the dataset as well as to see the various affects these variables have on the housing prices. These variables mainly include type, rooms, distance, bed, bath, car, landsize, and building area. 
So far from the findings, we can see that car spaces, number of total rooms, building area, number of bedrooms, and number of bathrooms have a positive affect on the housing prices. Additionally, the housing price and the region the house is located in have a big affect on the price as well.


# Part Two

### Part 1

#### Question 1
![Distributions of Price](https://user-images.githubusercontent.com/104324776/166166301-070c6067-d380-47a4-8011-3a4b4b84ad51.png)

We can see from the distribution graph that most of the prices are around 1,000,000. This is confirmed by the statstics description which states the mean is 1,075,684. Additionally, for price, the max price was around 9,000,000 while the minimum price was around 85,000. The standard deviation for price is 639,310. In regards to other important variables, for rooms the mean number of rooms is approximately 3, with the minimum number being 1 room and the maximum being 10 rooms. For bedrooms specifically, the mean is about 3 bedrooms, and the minimum is 0 and the max is 20. For bathrooms, the mean is around 2 bathrooms, with the min and max being 0 and 8 respectively. Other important statistics include those of number of car spaces and Landsize. For car spaces, the mean is around 2 car spaces, and the min and max are 0 and 10. For land size, the mean is 558.4, and the min and max are 0 and 433014. 

#### Question 2
The empty rows of building area were replaced with 0 due to the landsize having 0 values as well. The empty rows of car were also replaced with 0. Finally, the empty rows of year built were replaced with random values between the oldest and newest year built. 

#### Question 5

The following variables were dropped: 'Suburb', 'Date', 'Address', 'SellerG', 'CouncilArea', 'Longtitude', 'Lattitude','Propertycount', 'YearBuilt'. Due to most of these variables being unique identifiers, or too specific, they were dropped. Year built was dropped due to the age of a property generally not having a clear consistent positive or negative affect on the housing prices. While postcode is somewhat of a unique identifier, it was kept because the area a house is located in can potentially have a great affect on the price. 
Method and regionname were encoded using label encoding due to the wide range of values within these variables. On the other hand, because type had only 3 possibilities in this dataset, one-hot encoding was used. 

### Part 3

#### Questions 2 and 3

![Linear Regression Accuracy](https://user-images.githubusercontent.com/104324776/166167452-d7b7d948-be2c-4c75-8063-808751882d91.png)

We can see that when the percentage of testing data is 10%, the accuracy is the highest at around 61%. Additionally, as the percentage of testing increases, the accuracy also decreases. 

![Accuracy SGD](https://user-images.githubusercontent.com/104324776/166167384-e35755e9-3133-4123-892d-284e4839d4d9.png)

In the case of using the SGD algorithm, the accuracy is not positive. This most likely indicates this is not the optimal model for this type of dataset and problem. 

#### Question 4

![Residuals Plot](https://user-images.githubusercontent.com/104324776/166167513-31c07f53-595a-4218-9db1-440b123c3eca.png)

We can see that most of the residuals are below the x-axis. This could indicate that most of the predicted values were bigger than the actual values. Additionally, we can see that the R^2 value is .449. This means that around 45% of the variance is explained by the independent variables. The closer to 1 the R^2 is, the better the model generally. Since the R^2 in this case is .449, the model is not good. 

#### Question 5
![Predicted Values vs  Test Values](https://user-images.githubusercontent.com/104324776/166609580-621aa002-8c86-4fa7-9e19-07a60921effb.png)

The following article was used for the visualization : https://towardsdatascience.com/implementing-sgd-from-scratch-d425db18a72c.

From the graph, we can see that the predicted value, shown in blue, only span a small portion of the actual price values. Hence, we can see that the SGD does not work well which is backed up by the low accuracy. 


#### Question 6
MSE was also calculated per the article since the MSE is a good indicator of the quality of a model. From the high level of MSE calculated, it is an indicator that the SGD model is not best for this type of data. Additionally, we can see that by the accuracy values and the graph of predicted versus actual values that the linear regression is better.  Hence, the linear regression model is better in this case. This makes sense because linear regressions are better at handling cases where the dependent variable can take on a wide range of values. 
