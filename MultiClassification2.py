from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy
import tensorflow as tf

seed = 0
numpy.random.seed(seed)
tf.random.set_seed(seed)

#df = pd.read_csv('/Users/chung_sungwoong/Desktop/Practice/DeepLearning_Practice/dataset/iris.csv', names = ['special_length','sepal_width','petal_length','petal_width','species'])
df = pd.read_excel('/Users/chung_sungwoong/Desktop/Check2.xlsx', names = ['accuracy','time','user'])

dataset = df.values
x = dataset[:,0:2].astype(float)
Y_obj = dataset[:,2]

e = LabelEncoder()
e.fit(Y_obj)
Y = e.transform(Y_obj)
Y_encoded = np_utils.to_categorical(Y)      #원 핫 인코딩

#소프트맥스 모델

model = Sequential()
model.add(Dense(16,input_dim=2,activation='relu'))
model.add(Dense(3,activation='softmax'))

model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(x,Y_encoded,epochs=50, batch_size=1)

print("\n Accuracy: %.4f" %(model.evaluate(x,Y_encoded)[1]))
