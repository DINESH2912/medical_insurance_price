# -*- coding: utf-8 -*-
"""medical_insurance_price_prediction

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z72c-8K-sv6ul805qS0-m6o2cFmRVEpq
"""

import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
insurance=pd.read_csv("https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv")
insurance

# to prepare our data we can borrow some classes from the sklearn
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import MinMaxScaler,OneHotEncoder
from sklearn.model_selection import train_test_split
# create a column transformer
ct=make_column_transformer((MinMaxScaler(),["age","bmi","children"]),
                            (OneHotEncoder(handle_unknown="ignore"),["sex","smoker","region"])
                            )

# create x and y
x=insurance.drop("charges",axis=1)
y=insurance["charges"]
# train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
# fit the column transformer to training data
ct.fit(x_train)
# transform the training and testing data with normalization
x_train_normal=ct.transform(x_train)
x_test_normal=ct.transform(x_test)

x_test_normal[0]

# building a neural network
tf.random.set_seed(42)
#create a model
insurance_model=tf.keras.Sequential([tf.keras.layers.Dense(100),
                                     tf.keras.layers.Dense(100),
                                     tf.keras.layers.Dense(100),
                                     tf.keras.layers.Dense(100),
                                     tf.keras.layers.Dense(1)])
# compile the model
insurance_model.compile(loss=tf.keras.losses.mae,
                     optimizer=tf.keras.optimizers. Adam(),
                     metrics=["mae"])
# fit the model
insurance_model.fit(x_train_normal,y_train,epochs=400)

insurance_model.evaluate(x_test_normal,y_test)