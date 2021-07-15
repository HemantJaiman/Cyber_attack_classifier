# -*- coding: utf-8 -*-
"""
Created on Mon May 11 04:33:04 2020

@author: Hackie_Packie
"""

import pandas as pd
import numpy as np
from sklearn import preprocessing 
label_encoder = preprocessing.LabelEncoder() 
from sklearn.metrics import confusion_matrix,accuracy_score

data= pd.read_csv('dataset.csv')
#data = data.iloc[:2320 ,:]

data=data.drop([' Flow Duration', 'Total Length of Fwd Packets',' Total Length of Bwd Packets', ' Fwd IAT Mean','Fwd Packets/s',' Bwd Packets/s',' Min Packet Length',' Max Packet Length',' SYN Flag Count',' PSH Flag Count',' ACK Flag Count',' URG Flag Count'], axis = 1)


data['Flow Bytes/s'] = data['Flow Bytes/s'].astype(float) 
data[' Flow Packets/s'] = data[' Flow Packets/s'].astype(float)
data[' Label'] = data[' Label'].astype(str)
data[' Label']= label_encoder.fit_transform(data[' Label'])


x= data.loc[:, data.columns != ' Label']
y= data[" Label"]
y = y.to_frame()


r=[]
for i in range(1001,1160):
    r.append(i)

train_x = x.iloc[:2160,:]
train_x = train_x.drop(r)
#train_x.values
train_x = train_x.as_matrix()


train_y = y.iloc[:2160,]
train_y = train_y.drop(r)
#train_y.values
train_y = train_y.as_matrix()


df1 = x.iloc[r]
df2 = x.iloc[2160:,:]
test_x = pd.concat([df1,df2])
test_x = test_x.as_matrix()


df3 = y.iloc[r]
df4 = y.iloc[2160:,:]
test_y = pd.concat([df3,df4])
test_y = test_y.as_matrix()


train_x=train_x.astype('int')
train_y=train_y.astype('int')
test_y = test_y.astype('int')
test_x= test_x.astype('int')




#train_x = pd.DataFrame(train_x)
#train_y = pd.DataFrame(train_y)
#test_x = pd.DataFrame(train_x)
#test_y = pd.DataFrame(test_y)


from sklearn.svm import SVC
svclassifier = SVC(kernel='linear')
svclassifier.fit(train_x, train_y)
pred = svclassifier.predict(test_x)

#checking accuracy
cm = confusion_matrix(pred,test_y)
print(cm)
acc=accuracy_score(pred,test_y)
print(acc*100)