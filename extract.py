import re
import Vectorize
import numpy as np;
from sklearn.preprocessing import LabelEncoder;
from keras.utils import np_utils

def writeToFile(filename, input):
	with open(filename, "w") as tofile:
		tofile.write(input);

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def isLabel(line):
 	return bool(re.match('^[HEC]+$', line));

#method seperates label from training data
def training(file): 
	sequence = "";
	label = " "
	with open(file, "r") as myfile:
		for line in myfile:
			
			if not hasNumbers(line):
				if not isLabel(line):
					sequence += line.strip()
					sequence = sequence.strip()
				if isLabel(line):
					label += line.strip()
					label = label.strip()
		return sequence, label;

def vectorize(filename, window):
	sequence, label = training(filename)
	inputs = Vectorize.vectorizeSequence(sequence, window)
	inputs.tofile("input.txt")
	labels = np.array(list(label))
	labels.tofile("labels.txt")
	labels = encodeLable(labels)
	return inputs, labels;

def encodeLable(label):
	# encode class values as integers
	encoder = LabelEncoder()
	encoder.fit(label)
	encoded_Y = encoder.transform(label)
	# convert integers to dummy variables (i.e. one hot encoded)
	return np_utils.to_categorical(encoded_Y)







