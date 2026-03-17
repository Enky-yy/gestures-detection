import numpy as np
from sklearn.model_selection import train_test_split
from datasets import load_datasets
from model import create_model

x,y = load_datasets("../../datasets/gesture_datasets.csv")

x = x.reshape(x.shape[0],1,x.shape[1])

X_train , X_test , y_train , y_test = train_test_split(x,y,test_size=0.2)

model = create_model((1,42), len(set(y)))

model.fit(X_train,y_train,validation_data=(X_test,y_test),epochs=20,batch_size=32)

model.save('../../models/gesture_model.h5')
