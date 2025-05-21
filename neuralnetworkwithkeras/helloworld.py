
import keras
from keras.models import Sequential
from keras.layers import Dense


model=Sequential()

# n_cols=dataset.shape[1]


import pandas as pd
from sklearn.datasets import make_regression


df=pd.read_csv('Synthetic_Regression_Dataset.csv')
print(df.info())
print('------------')
print(df.head(5))
