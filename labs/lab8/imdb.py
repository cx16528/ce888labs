
from __future__ import print_function
import numpy as np
np.random.seed(1337)  # for reproducibility

from keras.preprocessing import sequence
from keras.models import Model
from keras.layers import Dense, Activation, Embedding, Flatten, Input, PReLU, Dropout, Merge
from keras.datasets import imdb
from keras.layers.convolutional import Convolution1D
from keras.layers.pooling import GlobalMaxPooling1D
from keras.layers import LSTM
from keras.layers.advanced_activations import PReLU
from keras.models import Sequential
from keras.layers.embeddings import Embedding

max_features = 20000
maxlen = 80  # cut texts after this number of words (among top max_features most common words)
batch_size = 32

print('Loading data...')
(X_train, y_train), (X_test, y_test) = imdb.load_data(nb_words=max_features)
print(len(X_train), 'train sequences')
print(len(X_test), 'test sequences')

print (X_train[0])

print('Pad sequences (samples x time)')
X_train = sequence.pad_sequences(X_train, maxlen=maxlen)
X_test = sequence.pad_sequences(X_test, maxlen=maxlen)
print('X_train shape:', X_train.shape)
print('X_test shape:', X_test.shape)

print('Build model...')


#inputs = Input(shape=(maxlen,))
#x = inputs
#x = Embedding(max_features, 128, dropout=0.2)(x)
#x = Flatten()(x)
#x = Dense(1)(x)
#x = Convolution1D(32, 8, border_mode = 'valid', )(x)
#x = GlobalMaxPooling1D()(x)
#x = PReLU()(x)
#x = Dense(64)(x)
#x = PReLU()(x)
#x = Dropout(0.5)(x)
#x = Dense(64)(x)
#x = PReLU()(x)
#x = Dropout(0.5)(x)
#predictions = Activation("sigmoid")(x)

model = Sequential()
model.add(Embedding(max_features,
128,
input_length=maxlen,
dropout=0.2))
#model.add(Flatten())
#model.add(Dense(1))
#model.add(PReLU())
#model.add(Convolution1D(nb_filter=32,
#filter_length=8,
#border_mode='valid',
#activation='relu',
#subsample_length=1))
#model.add(GlobalMaxPooling1D())
# We add a vanilla hidden layer:
#model.add(Dense(1))
#model.add(Dropout(0.2))
#model.add(Activation('relu'))
model.add(LSTM(128, dropout_W=0.2, dropout_U=0.2))
model.add(Dense(1))
#model.add(PReLU())
#model.add(Dense(64))
#model.add(PReLU())
#model.add(Activation('sigmoid'))






#model = Model(input=inputs, output=predictions)
#model.compile(loss='binary_crossentropy',
              #optimizer='adam',
              #metrics=['accuracy'])

#print('Train...')



#model.fit(X_train, y_train, batch_size=batch_size, nb_epoch=15,
          #validation_data=(X_test, y_test))

model0 = Sequential()

model0.add(Embedding(max_features,
128,
input_length=maxlen,
dropout=0.2))
model0.add(Convolution1D(nb_filter=32,
filter_length=8,
border_mode='valid',
activation='relu',
subsample_length=1))
model0.add(GlobalMaxPooling1D())
# We add a vanilla hidden layer:
model0.add(Dense(1))
#model0.add(Dropout(0.2))
#model0.add(Activation('relu'))

#model0.compile(loss='binary_crossentropy',
#              optimizer='adam',
#              metrics=['accuracy'])
#print('Train...')

#model0.fit(X_train, y_train, batch_size=batch_size, nb_epoch=15,
#          validation_data=(X_test, y_test))
#score, acc = model0.evaluate(X_test, y_test,
#                            batch_size=batch_size)
		  
merge = Merge([model, model0], mode='concat')

final_model = Sequential()
final_model.add(merge)
final_model.add(Dense(1, activation = 'sigmoid'))	  
final_model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
print('Train...')

final_model.fit([X_train,X_train], y_train, batch_size=batch_size, nb_epoch=15,
          validation_data=([X_test,X_test], y_test))
		  

			  
score, acc = final_model.evaluate(X_test, y_test,
                            batch_size=batch_size)
print('Test score:', score)
print('Test accuracy:', acc)