# Section 5 - Machine Learning

This section of the repository contains the resources and code to extract and explore data from from https://archive.ics.uci.edu/ml/datasets/Car+Evaluation as instructed. A machine learning model was then trained to predict the buying price of the car given parameters in the requirements.

# Solution
The data was imported and explored. It can be observed the dataset is categorical in nature, meaning it has all categorical fields. There is also no null values and duplicates in the dataset. Some visualizations was produced to help us better understand the dataset. It can be observed that

* All the attributes have uniformly distributed unique values, except for Class
* Through the correlation plot, we can also observe that the buying price has no correlation with any of the attributes in the dataset, except for Class. On the other hand, it is observed that the class field has significant correlation with all the attributes

![correlation plot](correlation_plot.png?raw=true "correlation plot")

* It can also be observed from the website source that buying price is stated as an attribute. It is suspected that this dataset is designed to predict class values

Keeping that in mind, we move on by converting categorical variables into numerical values and mapping it against our data. The data is split for training and testing. GridSearchCV was then used to perform hyperparameter tuning to find the best model with the best parameters. We had explored 5 models which are svc, random_forest, knn, decision tree and xgboost because these are the common models to predict categorical data.

It is concluded that xgboost is performing the best among the models. The training data is fit into the model and used to predict on testing data, which resulted in a 35% accuracy, which is low. This is to be expected because the attributes in the dataset do not correlate to the buying field. A classification report and confusion matrix was then produced to evaluate our model.

After loading the model into a pickle file, we used it to predict the buying price of the car given the attributes:

	Maintenance = High
	Number of doors = 4
	Lug Boot Size = Big
	Safety = High
	Class Value = Good

which returns a low buying price as a result. 

As it was suspected that the dataset was used to predict class instead of buying price, the above process was repeated to predict class values which resulted in a way better model yielding a 97% accuracy. Both model and code to predict buying price and class were stored in this repository.


# Files and Folder Structure
- resources: contains code and model to predict class and buying price of car
- .png: visualize correlation plot to explain the lack of correlation between buying and other attributes

