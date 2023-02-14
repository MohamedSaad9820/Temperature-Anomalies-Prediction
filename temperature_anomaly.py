#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as nb
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
reg = LinearRegression()


def get_data():
    df=pd.read_csv("D:\Projects\Tempurature Anomalies Prediction/Northern Hemisphere Monthly Temperature 1880-2022.csv",sep=",",encoding="utf-8")
    return df

def month(month):
    if month == "January":
        mon=1
    elif month == "February":
        mon=2
    elif month == "March":
        mon=3
    elif month == "April":
        mon=4
    elif month == "May":
        mon=5
    elif month == "June":
        mon=6
    elif month == "July":
        mon=7
    elif month == "August":
        mon=8
    elif month == "September":
        mon=9
    elif month == "October":
        mon=10
    elif month == "November":
        mon=11
    elif month == "December":
        mon=12
    else:
        mon="error_month"
    return mon

def avg_anom(df,mon):
    anomaly=[]
    for i in range(len(df)):
        if(df["Month"][i]==mon):
            anomaly.append(df["Temperature"][i])
        i+=1
    return nb.mean(anomaly)

def max_pos(df,mon):
    max_pos=[]
    for i in range(len(df)):
        if (df["Month"][i]==mon and df["Temperature"][i]>0):
            max_pos.append(df["Temperature"][i])
        i+=1
    return max(max_pos)

def num_pos(df,mon):
    pos=0
    for i in range(len(df)):
        if (df["Month"][i]==mon and df["Temperature"][i]>0):
            pos+=1
        i+=1
    return pos

def max_neg(df,mon):
    max_neg=[]
    for i in range(len(df)):
        if (df["Month"][i]==mon and df["Temperature"][i]<0):
            max_neg.append(abs(df["Temperature"][i]))
        i+=1
    return max(max_neg)

def num_neg(df,mon):
    neg=0
    for i in range(len(df)):
        if (df["Month"][i]==mon and df["Temperature"][i]<0):
            neg+=1
        i+=1
    return neg

def num_stand(df,mon):
    stand=0
    for i in range(len(df)):
        if (df["Month"][i]==mon and df["Temperature"][i]==0):
            stand+=1
        i+=1
    return stand

def train(df):
    x = df.drop(['Temperature'] , axis = 1).values
    y = df['Temperature'].values
    x_train,x_test,y_train,y_test = train_test_split(x,y, test_size= 0.25, random_state =42)
    reg.fit(x_train , y_train)
    return round(reg.score(x_train , y_train)*100,2)

def predict(year,mon):
    y=reg.predict([[year,mon]])[0]
    return y


# In[ ]:




