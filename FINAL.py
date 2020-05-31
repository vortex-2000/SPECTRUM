import matplotlib.pyplot as plt

import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import itertools
import statsmodels.api as sm


import numpy as nm

model=LinearRegression()

df = pd.read_csv("student-math.csv", sep=';')



col=df["G1"]+df["G2"]+df["G3"]

df["final grade"]=col

le= LabelEncoder()

dfle=df

dfle["Pstatus"]=le.fit_transform(dfle["Pstatus"])
dfle["Mjob"]=le.fit_transform(dfle["Mjob"])
dfle["Fjob"]=le.fit_transform(dfle["Fjob"])
dfle["reason"]=le.fit_transform(dfle["reason"])
dfle["schoolsup"]=le.fit_transform(dfle["schoolsup"])
dfle["famsup"]=le.fit_transform(dfle["famsup"])
dfle["paid"]=le.fit_transform(dfle["paid"])
dfle["activities"]=le.fit_transform(dfle["activities"])
dfle["nursery"]=le.fit_transform(dfle["nursery"])
dfle["higher"]=le.fit_transform(dfle["higher"])
dfle["internet"]=le.fit_transform(dfle["internet"])
dfle["romantic"]=le.fit_transform(dfle["romantic"])
dfle["sex"]=le.fit_transform(dfle["sex"])
dfle["school"]=le.fit_transform(dfle["school"])
dfle["address"]=le.fit_transform(dfle["address"])
dfle["famsize"]=le.fit_transform(dfle["famsize"])
dfle["guardian"]=le.fit_transform(dfle["guardian"])

X=dfle[['Pstatus','Mjob','Fjob','reason','schoolsup','famsup','paid',
        'activities','nursery','higher','internet','romantic','sex',
        'school','address','famsize','guardian','age','G1','G2',
        'absences','health','Walc','Dalc','goout','freetime','famrel',
        'failures','studytime','traveltime','Fedu','Medu']].values

Y=dfle["final grade"]






X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=5)


model.fit(X_train,Y_train)
model.predict(X_test)
print(model.score(X_test,Y_test))

#print(model.predict(X_test).shape)
#print(Y_test.shape)

#plt.scatter(model.predict(X_test),Y_test)
X = nm.append(arr = nm.ones((395,1)).astype(int), values=X, axis=1) 
X_opt=X[:,[0,3,4,5,6,8,9,
           11,12,13,14,18,19,20,
           
           21,22,23,24,27,28,
           31,32]]
 
model_OLS=sm.OLS(endog=Y,exog=X_opt).fit()
print(model_OLS.summary())


X_train,X_test,Y_train,Y_test=train_test_split(X_opt,Y,test_size=0.2,random_state=5)


model.fit(X_train,Y_train)
model.predict(X_test)
print(model.score(X_test,Y_test))



