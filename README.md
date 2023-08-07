
# Used  Hyundai  Car  Price  Prediction 

With the help of Machine Learning model we have Predicted the used Hyundai car prices in UK including various Influential Factors such as Model, Year, Mileage, Fuel type, Engine Size which significantly impact the prices of used cars

# Objectives
- Accurate price predictions for the buyers to make informed decisions by evaluating the fairness of asking prices and for Sellers they can set appropriate prices based on market trends, which increasing their chances of a successful sale.

- This project aims to contribute to the understanding of used car pricing dynamics by analyzing data and uncovering the relationships between factors and prices. And make Valuable insights gained from this research can benefit market participants and improve transparency in the used car market.

# Dataset
![Screenshot (1615)](https://github.com/Aayush-Chourasiya/Price-Prediction-of-Pre-Owned-Cars/assets/133970565/7d9f61f6-4763-43eb-a448-02ffccc15054)


# insights
Image daal

# Discription

Objective: To build a Machine Learning model (Linear Regression) that can predict prices (label) of used cars based on various features
Data Collection: For this, a reasonable and large enough dataset was required. Now, instead of looking for some old data or sample data available on the internet, I decided to scrape the website of a service provider already working in this field. So, I came across spinny.com which has a simple yet cool UI. Finally, the data was scrapped from this website.
Data Cleaning & Feature Engineering: Initially the dataset had all the data in just 7 columns, the data had null values, duplicates, and noise too. After applying techniques like Data Cleaning (imputation, outlier detection, and removing duplicate records), EDA, and Feature Generation, a total of 14 meaningful features were generated, which can be used for drawing insights through aggregations and visualization. Then, I applied some final techniques, to prepare the final data for training the model, like Feature Selection, Feature Encoding, and Feature Scaling. The final dataset has the following independent features:

Model
body type
fuel type
transmission
model (year)
km driven (in thousands)
mileage (in kmpl)
eating capacity (units)
ground clearance (in mm)
boot space (inliterss)
fuel tank capacity (inliterss)
max power (in bhp)

Data Analysis and Visualisation: Meanwhile data analysis through groupby, pivot table, and aggregate functions was also done and the data was visualized (screenshots may be referred to).
Training: The final dataset was then split into training and testing datasets and trained through Linear Regression.
Testing: The predicted values for the label (price) were then generated. The accuracy came out to be 85% using the R2 score metric and 84% using the Adjusted R2 score method.
Predicting (Applying the Model): As a test case, predicting the price of a used car using hypothetical features seems to be quite reasonable and meaningful. The model now can be used by a user who may be a buyer/seller to predict the prices of pre-owned cars.

#Future Scope of the Model for the Masses:
Empowering Buyers: The model can assist potential buyers in estimating the fair market value of a used car they are interested in. By inputting the car's relevant characteristics, such as make, model, year, mileage, condition, and additional features, the model can provide a predicted price range. This helps buyers make informed decisions and negotiate better deals.
Transparent Pricing: The model can increase transparency in the used car market by providing a standardized and objective pricing mechanism. It reduces information asymmetry between sellers and buyers, ensuring that individuals are less likely to be taken advantage of due to a lack of market knowledge. The model's predictions can serve as a reference point for evaluating a seller's asking price.
Saving Time and Effort: Instead of manually researching and comparing prices for similar used cars, individuals can rely on the machine learning model to quickly estimate a fair price range. This saves time and effort for potential buyers, allowing them to focus on other aspects of the purchasing process.
Selling Assistance: The model can also benefit sellers by guiding them in setting reasonable prices for their used cars. By considering the characteristics of their vehicle and examining the predicted price range, sellers can ensure they are not undervaluing or overpricing their cars. This helps sellers attract potential buyers more effectively.
Financial Planning: The availability of accurate price predictions can aid individuals in their financial planning. For example, if someone intends to sell their car in the future, they can estimate its potential value using the machine learning model. This information allows them to make informed decisions about when to sell and how it may impact their overall financial situation.
