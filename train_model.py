import extract;
import numpy as np
import sys
import os
from keras.models import Sequential
from keras.callbacks import EarlyStopping
from keras.callbacks import ModelCheckpoint
from sklearn.model_selection import train_test_split
from keras.layers import Dropout, Flatten, Dense, Activation, Conv2D, MaxPooling2D, Convolution1D, Dropout,Conv1D,MaxPooling1D
from keras.initializers import random_uniform

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
file_name = ''
window_size = 0
if len(sys.argv) < 3:
    print('invalid number of arguments')
    print('supply training file name and window size')
else:
    try:
        file_name = sys.argv[1];
        print(file_name)
    except:
        sys.exit('invalid training file specified')
    try:
        window_size = (int(sys.argv[2]) - 1)/2;
        print(window_size)
    except:
        sys.exit('invalid window size specified')
    print('done')
    #fix random seed for reproducibility
    seed = 7
    np.random.seed(seed)


    X, Y = extract.vectorize(file_name, window_size);
    print('shape X')
    print(X.shape)
    print('shape Y')
    print(Y.shape)

    batch_size = 128
    samples_per_epoch = 1000
    validation_steps = 300
    nb_filters1 = 32
    nb_filters2 = 64
    pool_size = 2
    activation='relu'
    learning_rate = 0.0025
    hidden_initializer = random_uniform(seed=7)
    dropout_rate = 0.75

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.10, random_state=42)

    x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], 1)
    x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], 1)

    model = Sequential()

    model.add(Convolution1D(filters=32, kernel_size=3, input_shape=(x_train.shape[1:3]), activation=activation))
    model.add(Convolution1D(filters=64, kernel_size=3, activation=activation))

    #model.add(Dropout(dropout_rate))
    #model.add(Dense(128,  kernel_initializer=hidden_initializer, activation=activation))
    model.add(Dropout(dropout_rate))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Flatten())
    model.add(Dense(128, kernel_initializer=hidden_initializer, activation=activation))
    model.add(Dense(Y.shape[1], kernel_initializer=hidden_initializer, activation='softmax'))

    model.compile(loss = 'categorical_crossentropy', optimizer='Adam', metrics =['accuracy'])

    model.summary();

    monitor = EarlyStopping(monitor='val_loss', min_delta=0.0001, patience=10, mode='auto')
    checkpointer = ModelCheckpoint(filepath="best_weights.hdf5", save_best_only=True)

    model.fit(x_train, y_train, validation_data=(x_test, y_test), callbacks=[checkpointer, monitor], epochs=3,
              batch_size=batch_size)
    model.save('model.hd5');
