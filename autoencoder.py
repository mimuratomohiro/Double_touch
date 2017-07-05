import keras
import numpy as np
import scipy as sp
from keras.layers import Input, Dense
from keras.layers import merge
from keras.models import Model
from keras.datasets import mnist
import matplotlib.pyplot as plt
from keras.utils import plot_model


result     = np.load("result.npy")
angle      = np.load("result_angle.npy")
point      = np.load("result_point.npy")
joint      = np.load("result_move.npy")

angle      = np.c_[angle,angle[:,0]+angle[:,1],angle[:,2]+angle[:,3]]
angle_sin  = np.sin(angle)
angle_cos  = np.cos(angle)
angle      = np.c_[angle_sin,angle_cos]

encoding_dim = 2
input_img1 = Input(shape=(result.shape[1],))
input_img2 = Input(shape=(angle.shape[1],))
input_img3 = Input(shape=(joint.shape[1],))


encoded1 = Dense(result.shape[1], activation="linear")(input_img1)
encoded3 = Dense(joint.shape[1], activation="linear")(input_img3)
encoded = merge([encoded1, input_img2,encoded3], mode='concat', concat_axis=1)
encoded = Dense(2, activation="linear")(encoded)

decoded  = Dense(result.shape[1]+angle.shape[1]+joint.shape[1], activation="linear")(encoded)
decoded1 = Dense(result.shape[1], activation="linear")(decoded)
decoded1 = Dense(result.shape[1], activation='sigmoid')(decoded1)
decoded2 = Dense(angle.shape[1], activation="linear")(decoded)
decoded3 = Dense(joint.shape[1], activation="linear")(decoded)
decoded3 = Dense(joint.shape[1], activation='sigmoid')(decoded3)


autoencoder1 = Model(input=[input_img1,input_img2,input_img3], output=[decoded1,decoded2,decoded3])
autoencoder1.compile(optimizer='adam', loss='binary_crossentropy')

autoencoder1.fit([result[:2000],angle[:2000],joint[:2000]], [result[:2000],angle[:2000],joint[:2000]],
                nb_epoch=100,
                batch_size=80,
                shuffle=True,
                validation_data=([result[2000:2080],angle[2000:2080],joint[2000:2080]], [result[2000:2080],angle[2000:2080],joint[2000:2080]]))

encoder      = Model(input=[input_img1,input_img2,input_img3], output=encoded)
encoded_imgs = encoder.predict([result,angle,joint])
decoded_imgs = autoencoder1.predict([result,angle,joint])

plot_model(autoencoder1, show_shapes=True, show_layer_names=True, to_file='model.png')
autoencoder1.summary()
plt.plot(encoded_imgs[:,0],encoded_imgs[:,1],'o')
plt.show()

plt.plot(point[:,0],point[:,1],'o')
plt.show()


