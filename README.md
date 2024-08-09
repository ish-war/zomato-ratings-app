# zomato-ratings-app

## Objective

The main agenda of this project is to:

* Perform extensive Exploratory Data Analysis (EDA) on the Zomato Dataset.
* Build an appropriate Machine Learning Model that will help various Zomato restaurants predict their respective ratings based on certain features.
* Deploy the machine learning model via Flask to enable live predictions of restaurant ratings.

## Project Workflow

* Data Preprocessing = Renamed columns for clarity, Handled missing values and duplicates, Conducted Exploratory Data Analysis (EDA) to uncover insights and trends.
* Feature Engineering = Converted categorical variables into numeric format using label encoding, Applied label encoding to categorical columns to facilitate model building.
* Model Building = Built models using Linear Regression, Random Forest, and Extra Tree Regressor algorithms, Calculated R² scores for model evaluation: Random Forest: R² score of 88% and Extra Tree Regressor: R² score of 92%
* Model Deployment = Saved the trained model using Pickle, Developed a web application using Flask and PyCharm, Created necessary files: app.py, index.html, and model.py.

## Web Application Development

* Model Deployment = Created a Pickle file of the best-performing model, Deployed the model using Flask.
* Application Structure = Developed the web application using PyCharm, Created necessary files: model.py, index.html, and app.py.
* User Interface = Designed a user-friendly interface with index.html to interact with the model.

## Conclusion

This project successfully developed a robust machine learning model to predict Zomato restaurant ratings based on various features. The Extra Tree Regressor model demonstrated superior performance with an R² score of 92%, indicating high accuracy in predictions. The Random Forest model also performed well with an R² score of 88%.

Restaurant owners can use the predictive model to understand factors influencing their ratings and take informed actions to enhance their service quality.Overall, this project provides a valuable tool for Zomato restaurants to predict and improve their ratings, ultimately contributing to better customer experiences and business growth.

## Web Development Image
![image](https://github.com/user-attachments/assets/8f901841-cc50-4b7c-85c3-a051af69475a)


