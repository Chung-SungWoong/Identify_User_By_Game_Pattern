from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense
from sklearn.model_selection import train_test_split

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy
import tensorflow as tf

seed = 0
numpy.random.seed(seed)
tf.random.set_seed(seed)

df = pd.read_excel('/Users/chung_sungwoong/Desktop/Check.xlsx', names = ['accuracy','time','user'])

dataset = df.values
x = dataset[:,0:2].astype(float)
Y_obj = dataset[:,2]

e = LabelEncoder()
e.fit(Y_obj)
Y = e.transform(Y_obj)
Y_encoded = np_utils.to_categorical(Y)      #원 핫 인코딩

x_train, x_test, y_train,y_test = train_test_split(x,Y_encoded,test_size = 0.3, random_state = seed)

#소프트맥스 모델

model = Sequential()
model.add(Dense(16,input_dim=2,activation='relu'))
model.add(Dense(3,activation='sigmoid'))


model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(x_train,y_train,epochs=50, batch_size=1)

print("\n Accuracy: %.4f" %(model.evaluate(x_test,y_test)[1]))
