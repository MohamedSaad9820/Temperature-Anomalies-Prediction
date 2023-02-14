#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,jsonify,request
from temperature_anomaly import *
app      = Flask(__name__)
df = get_data()
accuracy = train(df)

@app.route('/')        ## Homepage
def home():
    data = {
        'name':'Temperature_Anomalies',
        'page_name':'الصفحة الرئيسيه'
    }
    return jsonify(data)

@app.route('/train') ## train
def fl_train():
    accuracy = train(df)
    data = {
        '1)name':'Temperature_Anomalies'+"                                                                                                                                                                          ",
        '2)result':'Ok'+"                                                                                                                                                  ",
        '3)page_name':'Train'+"                                                                                                                                            ",
        '4)accuracy':str(accuracy)+"                                                                                                                                                                                                                               ",
        '5)Regression_Function ':"Y="+str(round(reg.intercept_,3))+" + "+str(round(reg.coef_[0],3))+"X1"+" + "+str(round(reg.coef_[1],3))+"X2"
    }
    return jsonify(data)

@app.route('/predict') ## predict
def fl_predict():
    y  = request.args["y"]
    m  = request.args['m']
    year  = int(y)
    mon= month(str(m))
    accuracy=train(df)
    print(m)
    print(y)
    avg=avg_anom(df,mon)
    max_post=max_pos(df,mon)
    max_negt=max_neg(df,mon)
    num_post=num_pos(df,mon)
    num_negt=num_neg(df,mon)
    num_standt=num_stand(df,mon)
    pred_anom=predict(year,mon)
    if pred_anom>0:
        typ="Positive Anomaly (Hot)"
    elif pred_anom<0:
        typ="Negative Anomaly (Cool)"
    else:
        typ="Standard Value"
    
    data = {"0)TOPIC(0)":"(The Historical Data Of Temperature Anomalies Of ("+m+") From 1880 To 2022)                                                                                                       ",
           "01)The Average Anomaly in ("+m+") is ":str(avg)+"                                                                                                                             ",
           "02)The Number Of Standard Times in ("+m+") is ":str(num_standt)+"                                                                                                                                   ",
           "03)The Maximum Positive (Hot) Anomaly in ("+m+") is ":str(max_post)+"                                                                                                                         ",
           "04)The Number Of Times Of Positive (Hot) Anomaly in ("+m+") is ":str(num_post)+"                                                                                                              ",
           "05)The Maximum Negative (Cool) Anomaly in ("+m+") is ":str(max_negt)+"                                                                                                                        ",
           "06)The Number Of Times Of Negative (Cool) Anomaly in ("+m+") is ":str(num_negt)+"                                                                                                             ",
           '1)-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------':"  ",
           "1)TOPIC(1)":"The Prediction Of Temperature Anomaly Of ("+m+" "+str(y)+")                                                                                                                ",
           "11)The Prediction Temperature Anomaly is ":str(pred_anom)+"                                                                                                                               ",
           "12)The Anomaly Type is ":typ+"                                                                                                                                                  "
           }
    return jsonify(data)
app.run()


# In[ ]:




