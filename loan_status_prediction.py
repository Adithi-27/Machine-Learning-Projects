# -*- coding: utf-8 -*-
"""Loan Status Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fKOAeRm01TEpMUdYr0u_JbCFknrriTEg

Importing the Dependencies
"""

import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

"""Data Collection and data pre-processing"""

# loading the dataset to pandas dataframe
loan_dataset = pd.read_csv('/content/train_u6lujuX_CVtuZ9i (1).csv')

type(loan_dataset)

# printing the first 5 rows of the dataframe
loan_dataset.head()

# number of rows and columns
loan_dataset.shape

# statistical measures
loan_dataset.describe()

# number of missing values in each column
loan_dataset.isnull().sum()

# dropping the missing values
loan_dataset = loan_dataset.dropna()

# number of missing values in each column
loan_dataset.isnull().sum()

# label encoding
loan_dataset.replace({"Loan_Status":{'N':0,'Y':1}},inplace=True)

# printing the first 5 rows of the dataframe
loan_dataset.head()

# Dependent column values
loan_dataset['Dependents'].value_counts()

# replacing the value of 3+ to 4
loan_dataset = loan_dataset.replace(to_replace='3+', value=4)

# dependent values
loan_dataset['Dependents'].value_counts()

"""Data Visualization"""

# education and loan status
sns.countplot(x='Education', hue='Loan_Status', data=loan_dataset)

# marital status & loan status
sns.countplot(x='Married', hue='Loan_Status', data=loan_dataset)

# convert categorical columns to numerical values
loan_dataset.replace({'Married':{'No':0,'Yes':1},'Gender':{'Male':1,'Female':0},'Self_Employed':{'No':0,'Yes':1},
                      'Property_Area':{'Rural':0,'Semiurban':1,'Urban':2},'Education':{'Graduate':1,'Not Graduate':0}},inplace=True)

loan_dataset.head()

# seperating the data and label
X = loan_dataset.drop(columns=['Loan_ID','Loan_Status'],axis=1)
Y = loan_dataset['Loan_Status']

print(X)
print(Y)

"""Train Test Split"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""Training the model:
Support Vector Machine Model
"""

classifier = svm.SVC(kernel='linear')

# training the support vector machine model
classifier.fit(X_train, Y_train)

"""Model Evaluation"""

# accuracy score on training data
X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy on training data : ', training_data_accuracy)

# accuracy score on test data
X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy on test data : ', test_data_accuracy)

"""Predictive System"""

Input_data_from_user = (1,1,4,1,0,3036,2504.0,158.0,360.0,0.01, 3)
input_data_as_numpy_array = np.asarray(Input_data_from_user)

# reshaping the data as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = classifier.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The Loan is approved')
else:
  print('The Loan is not approved')