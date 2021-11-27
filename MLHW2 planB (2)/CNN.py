
# coding: utf-8

# In[3]:


import os
from keras.models import Sequential, load_model
#from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D
from keras.utils import np_utils, plot_model ,to_categorical
from keras.datasets import mnist
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from keras.layers import *
from keras.callbacks import *
import keras
from sklearn.preprocessing import *


# In[4]:


# Import PyDrive and associated libraries.
# This only needs to be done once per notebook.
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

# Authenticate and create the PyDrive client.
# This only needs to be done once per notebook.
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)


# In[5]:


(A_train, B_train), (C_test, Y_test) = mnist.load_data()
#x_train = X_train.reshape(60000, 1, 28, 28)/255
#x_test = X_test.reshape(10000, 1, 28, 28)/255
#y_train = np_utils.to_categorical(Y_train)
#y_test = np_utils.to_categorical(Y_test)


data_1 = pd.read_csv(r'/content/drive/My Drive/Colab Notebooks/MLHW2 planB/mnist_train.csv')
X_train = data_1.drop(['label','id'],axis=1).values
Y_train = data_1['label'].values

data_3 = pd.read_csv(r'/content/drive/My Drive/Colab Notebooks/MLHW2 planB/mnist_test.csv')
X_test = data_3.drop(['id'],axis=1).values
test=data_3['id']

x_train = X_train.reshape(60000, 1, 28, 28)
x_test = X_test.reshape(10000, 1, 28, 28)
y_train = np_utils.to_categorical(Y_train)
y_test = np_utils.to_categorical(Y_test)


# In[6]:


print(X_train.shape)
print(Y_train.shape)
print(X_test.shape)
print(Y_test.shape)
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)


# In[ ]:


# Model Structure
model = Sequential()
model.add(Conv2D(filters=32, kernel_size=3, input_shape=(1, 28, 28), activation='relu', padding='same'))
model.add(MaxPool2D(pool_size=2, data_format='channels_first'))
model.add(Flatten())
model.add(Dense(256,  kernel_initializer='normal', activation='relu'))
model.add(Dense(256, input_dim=256,  kernel_initializer='normal',activation='relu'))
model.add(Dense(128, input_dim=256,  kernel_initializer='normal',activation='relu'))
model.add(Dense(32, input_dim=128,  kernel_initializer='normal',activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))
print(model.summary())


# In[ ]:


# Train
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=50, batch_size=32,verbose=1)
# Test
loss, accuracy = model.evaluate(x_test, y_test)
print('Test:')
print('Loss: %s\nAccuracy: %s' % (loss, accuracy))


# In[ ]:


Z_test = X_test.reshape(10000, 28, 28)/255
# Save model
model.save('./CNN_Mnist.h5')

# Load Model
model = load_model('./CNN_Mnist.h5')

# Display
def plot_img(n):
    plt.imshow(X_test[n], cmap='gray')
    plt.show()

def all_img_predict(model):
    print(model.summary())
    loss, accuracy = model.evaluate(x_test, y_test)
    print('Loss:', loss)
    print('Accuracy:', accuracy)
    predict = model.predict_classes(x_test)
    print(pd.crosstab(Y_test.reshape(-1), predict, rownames=['Label'], colnames=['predict']))

def one_img_predict(model, n):
    predict = model.predict_classes(x_test)
    print(' 圖片:')
    plt.axis("off")
    plot_img(n)
    print(' 預測數字:', predict[n])
    print(' 答案數字:', Y_test[n])


# In[ ]:


print("預測機率:",model.predict(x_test))
print("預測答案:",np.argmax(model.predict(x_test),axis=-1))


# In[ ]:


pre=model.predict_classes(x_test)
confusion_matrix(Y_test,pre)


# In[ ]:


pd.DataFrame(confusion_matrix(Y_test,pre))


# In[ ]:


#x_train = X_train.reshape(60000, 1, 28, 28)/255
#x_test = X_test.reshape(10000, 1, 28, 28)/255
#y_train = np_utils.to_categorical(Y_train)
#y_test = np_utils.to_categorical(Y_test)

false_index= np.nonzero(pre != Y_test)[0]
print("預測錯誤:",len(false_index))


# In[ ]:


#x_train = X_train.reshape(60000, 1, 28, 28)/255
#x_test = X_test.reshape(10000, 1, 28, 28)/255
#y_train = np_utils.to_categorical(Y_train)
#y_test = np_utils.to_categorical(Y_test)

false_img= Z_test[false_index]
ori_label= Y_test[false_index]
pre_label= pre[false_index]

width=10
height=int(len(false_index)/10) +1
plt.figure(figsize=(14,40))
for (index,img) in enumerate(false_img):
    plt.subplot(height,width,index + 1)
    msg="ori:"+str(ori_label[index])+"  "+"pre:"+str(pre_label[index])
    plt.title(msg)
    plt.axis("off")
    plt.imshow(img, cmap="gray")


# In[ ]:


prediction = pd.DataFrame(pre, columns=['label'])
result = pd.concat([test,prediction], axis=1)
result.columns
result.to_csv('/content/drive/My Drive/Colab Notebooks/MLHW2 planB/output.csv', index=False)


# In[2]:


get_ipython().system('jupyter nbconvert --to script hw3.ipynb')

