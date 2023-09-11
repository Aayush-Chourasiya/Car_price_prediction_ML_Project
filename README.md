# Used  Hyundai  Car  Price  Prediction 

With the help of Machine Learning model we have Predicted the used Hyundai car prices in UK including various Influential Factors such as Model, Year, Mileage, Fuel type, Engine Size which significantly impact the prices of used cars

# Objectives
- Accurate price predictions for the buyers to make informed decisions by evaluating the fairness of asking prices and for Sellers they can set appropriate prices based on market trends, which increases their chances of a successful sale.

- This project aims to contribute to the understanding of used car pricing dynamics by analyzing data and uncovering the relationships between factors and prices. And make Valuable insights gained from this research can benefit market participants and improve transparency in the used car market.

# Discription

Objective: Build a Linear Regression ML model to predict used car prices based on various features.

Data Collection: Scraped data from spinny.com, a service provider in the field, to obtain a reasonable and large dataset.

Data Cleaning & Feature Engineering: Handled null values, duplicates, and noise. Generated 14 meaningful features through EDA and feature generation techniques.

Final Data Preparation: Applied feature selection, encoding, and scaling to prepare the dataset for training the model.

Independent Features: Model, body type, fuel type, transmission, model year, km driven, mileage, seating capacity, ground clearance, boot space, fuel tank capacity, max power.

Data Analysis and Visualization: Conducted data analysis using group by, pivot tables, and aggregation, and visualized the data for insights.

Training: Split the dataset into training and testing sets, and trained the model using Linear Regression.
Predicting: The model can be used by buyers/sellers to predict the prices of pre-owned cars using hypothetical features.



Testing: Generated predicted values for prices and evaluated model accuracy using R2 score and Adjusted R2 score (85% and 84%, respectively).
![WhatsApp Image 2023-09-11 at 22 00 36](https://github.com/Aayush-Chourasiya/Car_price_prediction_ML_Project/assets/133970565/5bf93b22-58fd-48d2-98eb-37f45933be74)
![WhatsApp Image 2023-09-11 at 22 01 43](https://github.com/Aayush-Chourasiya/Car_price_prediction_ML_Project/assets/133970565/5142165b-0194-4248-83a2-fff5e40d00fa)



# Dataset
![Screenshot (1615)](https://github.com/Aayush-Chourasiya/Price-Prediction-of-Pre-Owned-Cars/assets/133970565/7d9f61f6-4763-43eb-a448-02ffccc15054)


# Insights
![Screenshot (1626)](https://github.com/Aayush-Chourasiya/Price-Prediction-of-Pre-Owned-Cars/assets/133970565/490e0498-d7c2-4a11-b6df-999f9fbe6d0c)

- The top models with the highest counts are Tucson, I10, and I30, indicating their prevalence in the dataset.
- Petrol has the highest count (2902), followed by diesel (1608), hybrid (349), and others (1).
- The manual transmission has the highest count (3611), followed by automatic (669), semi-auto (578), and others (2).
- Santa Fe has the highest Average Price among all around(21.6k), followed by Ioniq, I800, and others.









![Screenshot (1628)](https://github.com/Aayush-Chourasiya/Price-Prediction-of-Pre-Owned-Cars/assets/133970565/1fd8ed20-adab-4d82-a400-43a070296b49)

- The price demonstrates a strong positive correlation with the Model, Engine size, and year, while a weak correlation is observed with Total Driven, Fuel Type, and mpg.
-  The Random Forest model shows the lowest MSE and MAE values, indicating better accuracy and precision in predicting the target variable.
- With an R-squared score of 0.93, the Random Forest model demonstrates a strong correlation between the predicted and actual value.


# Conclusion
- Error Distribution: After training our model, we analyzed the difference between the test and predicted values using a distribution plot. The errors followed a normal distribution with a mean close to zero. This indicates that our model's predictions are generally accurate, as the errors are minimal.
- Scatter Plot Analysis: We plotted the test points against the predicted points using a scatter plot. The points aligned closely along the diagonal line, indicating a strong correlation between the predicted and actual values. This suggests that our model is effectively capturing the patterns and trends in the data.
- Performance Metrics: We evaluated the performance of our model using metrics such as Root Mean Square Error (RMSE), R2 Score, and Mean Square Error (MSE). Our model achieved an RMSE of 1.36 and an MSE of 1.97 for the test and predicted test values. These metrics provide insights into the accuracy and precision of our model's predictions.
- Accuracy Score: While accuracy score is typically used for classification tasks, we adapted it to assess the accuracy of our regression model. By setting a cutoff based on MSE, we classified predictions as either correct or incorrect. Our model achieved an accuracy score of 93.4%, indicating its effectiveness in predicting used car prices.

# Challenges
- Transforming categorical values and removing unnecessary features for regression compatibility.

- Finding the best regression algorithm and dealing with challenges in gridsearchCV for hyper parameter tuning.

- Identifying influential features using techniques like Pearson coefficient correlation and extra tree regressor.

- Learning HTML from scratch to develop a webpage showcasing the model's workings.


# Future Scope of the Model for the Masses:

Empowering Buyers: The model estimates the fair market value for used cars based on input characteristics (make, model, year, mileage, condition, and features), helping buyers make informed decisions and negotiate better deals.

Transparent Pricing: The model provides standardized and objective pricing, reducing information asymmetry between sellers and buyers, and preventing exploitation due to a lack of market knowledge.

Saving Time and Effort: Buyers can quickly estimate fair price ranges without manual research, saving time and effort during the purchasing process.

Selling Assistance: Sellers can use the model to set reasonable prices based on their car's characteristics, attracting potential buyers more effectively.

Financial Planning: Accurate price predictions aid in financial planning, allowing individuals to make informed decisions about selling their car and its impact on their overall financial situation.
