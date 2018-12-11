import numpy as np
import sys
from sklearn import  datasets, svm
from keras.models import load_model
import extract as e;
import matplotlib.pyplot as plt

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


    model = load_model('model.hd5')
    X, Y = e.vectorize(file_name, window_size)
    X = X.reshape(X.shape[0], X.shape[1], 1)

    print(Y.shape)
    y_predict = model.predict(X);

    test_loss, test_acc = model.evaluate(X, Y)

    print('Test accuracy:', test_acc)

    plt.clf()
    plt.plot(Y, y_predict, 'o')

    plt.show()
