#### Part One
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


#### Part Two

# Part 1

![Distributions of Price](https://user-images.githubusercontent.com/104324776/166166301-070c6067-d380-47a4-8011-3a4b4b84ad51.png)

We can see from the distribution graph that most of the prices are around 1,000,000. This is confirmed by the statstics description which states the mean is 1,075,684. Additionally, for price, the max price was around 9,000,000 while the minimum price was around 85,000. The standard deviation for price is 639,310. In regards to other important variables, for rooms the mean number of rooms is approximately 3, with the minimum number being 1 room and the maximum being 10 rooms. For bedrooms specifically, the mean is about 3 bedrooms, and the minimum is 0 and the max is 20. For bathrooms, the mean is around 2 bathrooms, with the min and max being 0 and 8 respectively. Other important statistics include those of number of car spaces and Landsize. For car spaces, the mean is around 2 car spaces, and the min and max are 0 and 10. For land size, the mean is 558.4, and the min and max are 0 and 433014. 

