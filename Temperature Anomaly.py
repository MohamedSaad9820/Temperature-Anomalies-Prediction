#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as nb
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv("D:\Projects\Tempurature Anomalies Prediction/Northern Hemisphere Monthly Temperature 1880-2022.csv",sep=",",encoding="utf-8")


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


df["Temperature"].describe()


# In[6]:


df["Temperature"].describe(include="All")


# In[7]:


df["Year"].value_counts()


# In[8]:


df["Month"].value_counts()


# In[9]:


sns.boxplot(df["Temperature"])


# ## Information

# In[10]:


# Average Anomaly
# maximum positive
# maximum negative
# no. of positive (hot)
# no. of negative (cool)
# no. of standard


# In[11]:


def info(month):
    pos=neg=stand=0
    anomaly=[]
    max_pos=[]
    max_neg=[]
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
    if mon=="error_month":
        print("The Month Spelling Is Error")
    else:
        for i in range(1716):
            if(df["Month"][i]==mon):
                anomaly.append(df["Temperature"][i])
                if (df["Month"][i]==mon and df["Temperature"][i]>0):
                    pos+=1
                    max_pos.append(df["Temperature"][i])
                elif (df["Month"][i]==mon and df["Temperature"][i]<0):
                    neg+=1
                    max_neg.append(abs(df["Temperature"][i]))
                elif (df["Month"][i]==mon and df["Temperature"][i]==0):
                    stand+=1
        print("Average Anomalies in ",month," ",nb.mean(anomaly))
        print("no. of Standard Times: ",stand)
        print("no. of Positive (Hot) Times: ",pos)
        print("Maximum Positive Anomaly in ",month," ",max(max_pos))
        print("no. of Negative (Cool) Times: ",neg)
        print("Maximum Negative Anomaly in ",month," ",max(max_neg))


# In[31]:


x=input()
info(x)


# ## Predict

# In[14]:


plt.scatter(x= df['Year'], y = df['Temperature'])


# In[15]:


x = df.drop(['Temperature'] , axis = 1).values
y = df['Temperature'].values


# In[17]:


from sklearn.model_selection import train_test_split


# In[18]:


x_train , x_test , y_train , y_test = train_test_split(x,y , test_size = 0.25 , random_state=42)


# In[41]:


from sklearn.linear_model import LinearRegression
reg = LinearRegression()


# In[42]:


reg.fit(x_train,y_train)


# In[43]:


reg.score(x_train , y_train)


# In[44]:


reg.score(x_test,y_test)


# In[45]:


reg.intercept_


# In[49]:


reg.coef_


# In[47]:


reg.predict([[2025,3]])[0]


# In[ ]:




