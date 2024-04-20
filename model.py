import numpy as np
import pandas as pd
import sklearn
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('Zomato_df.csv')


df.drop('Unnamed: 0', axis= 1, inplace= True)
print(df.head())

x= df.drop('rate', axis=1)
y= df['rate']

x_train,x_test,y_train,y_test = train_test_split(x,y, test_size= 0.3, random_state= 42)

from sklearn.ensemble import ExtraTreesRegressor
ET_model = ExtraTreesRegressor(n_estimators= 120)
ET_model.fit(x_train, y_train)
y_pred = ET_model.predict(x_test)

r2_score(y_test, y_pred)

import pickle

pickle.dump(ET_model, open('model.pkl', 'wb'))      # wb - written binary
model = pickle.load(open('model.pkl', 'rb'))