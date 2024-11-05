# -*- coding: utf-8 -*-
"""Spam Mail Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WS11HO7Odxs4J8bTvI2bFiyr4GsOG0KX

Importing the dependencies
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data collection and pre-processing"""

# loading the data from csv file to a pandas Dataframe
raw_mail_data = pd.read_csv('/content/mail_data.csv')

print(raw_mail_data)

# replace the null values with a null string
mail_data = raw_mail_data.where((pd.notnull(raw_mail_data)),'')

# printing the first 5 rows
mail_data.head()

# checking the size of the dataset
mail_data.shape

"""Label Encoding"""

# label spam mail as 0; ham mail as 1
mail_data.loc[mail_data['Category'] == 'spam', 'Category',] = 0
mail_data.loc[mail_data['Category'] == 'ham', 'Category',] = 1

# seperating the data as texts and label
X = mail_data['Message']
Y = mail_data['Category']

print(X)
print(Y)

"""Spliting the data into training & test data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.18, random_state = 2)

print(X.shape)
print(X_train.shape)
print(X_test.shape)

"""Feature Extraction"""

# transforn the text data to feature vactors that can be used as input to the logistic regression
feature_extraction = TfidfVectorizer(min_df = 1, stop_words = 'english', lowercase = True)

X_train_features = feature_extraction.fit_transform(X_train)
X_test_features = feature_extraction.transform(X_test)

# covert Y_train & Y_test values as integer
Y_train = Y_train.astype('int')
Y_test = Y_test.astype('int')

print(X_train_features)

"""Training the Model

Logistic Regression
"""

model = LogisticRegression()

# training the Logistic Regression model with the training data
model.fit(X_train_features, Y_train)

"""Evaluating the trained model"""

# prediction on training data
prediction_on_training_data = model.predict(X_train_features)
accuracy_on_training_data = accuracy_score(Y_train, prediction_on_training_data)

print('Accuracy on training data : ', accuracy_on_training_data)

# prediction on tesy data
prediction_on_test_data = model.predict(X_test_features)
accuracy_on_test_data = accuracy_score(Y_test, prediction_on_test_data)

print('Accuracy on test data : ', accuracy_on_test_data)

"""Building a predictive system"""

input_mail = ["FreeMsg Hey there darling it's been 3 week's now and no word back! I'd like some fun you up for it still? Tb ok! XxX std chgs to send, Â£1.50 to rcv"]

# convert text to feature vector
input_data_features = feature_extraction.transform(input_mail)

# making prediction
prediction = model.predict(input_data_features)
print(prediction)

if prediction[0] == 1:
  print('The mail is a Ham-mail')
else:
  print('The mail is Spam-mail')