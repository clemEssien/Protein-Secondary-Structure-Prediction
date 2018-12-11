from numpy import argmax, array


def paddzeros(num):
    n='';
    while num>0:
        n+='X';
        num -= 1;
    return n


def apply_window(string, char, window):
	l = len(string);
	res = ''

	left = string.index(char) - window;

	if (left < 0):
		s = paddzeros(abs(left)) + string[0: string.index(char) + window + 1]
		s = paddzeros((2 * window + 1) - len(s)) + s
		res += (s)
	if (left == 0):
		s = string[window - string.index(char): string.index(char) + window + 1];
		s = s + paddzeros((2 * window + 1) - len(s))
		res += (s)
	if (left > 0):
		s = string[string.index(char) - window: string.index(char) + window + 1]
		s = s + paddzeros((2 * window + 1) - len(s))
		res += (s)
	return res;

def vectorizeSequence(sequence, window):
	integer_encoded = [vectorize_sequence_with_window(apply_window(sequence, char, window)) for char in sequence]
	protein_vector = array(integer_encoded)
	return protein_vector;

def multiplyList(myList):
	result = 1
	for x in myList:
		if x != 0:
			result = result * x
	return result

def addList(myList):
	result = 0
	for x in myList:
		result = result + x
	return result

def vectorize_sequence_with_window(string):
	letterDict = {}
	vectors = [];
	letterDict["A"] = [0.008, 0.134, -0.475, -0.039, 0.181, 0.00]
	letterDict["R"] = [0.171, -0.361, 0.107, -0.258, -0.364, 0.00]
	letterDict["N"] = [0.255, 0.038, 0.117, 0.118, -0.055, 0.00]
	letterDict["D"] = [0.303, -0.057, -0.014, 0.225, 0.156, 0.00]
	letterDict["C"] = [-0.132, 0.174, 0.070, 0.565, -0.374, 0.00]
	letterDict["Q"] = [0.149, -0.184, -0.030, 0.035, -0.112, 0.00]
	letterDict["E"] = [0.221, -0.280, -0.315, 0.157, 0.303, 0.00]
	letterDict["G"] = [0.218, 0.562, -0.024, 0.018, 0.106, 0.00]
	letterDict["H"] = [0.023, -0.177, 0.041, 0.280, -0.021, 0.00]
	letterDict["I"] = [-0.353, 0.071, -0.088, -0.195, -0.107, 0.00]
	letterDict["L"] = [-0.267, 0.018, -0.265, -0.274, 0.206, 0.00]
	letterDict["K"] = [0.243, -0.339, -0.044, -0.325, -0.027, 0.00]
	letterDict["M"] = [-0.239, -0.141, -0.155, 0.321, 0.077, 0.00]
	letterDict["F"] = [-0.329, -0.023, 0.072, -0.002, 0.208, 0.00]
	letterDict["P"] = [0.173, 0.286, 0.407, -0.215, 0.384, 0.00]
	letterDict["S"] = [0.199, 0.238, -0.015, -0.068, -0.196, 0.00]
	letterDict["T"] = [0.068, 0.147, -0.015, -0.132, -0.274, 0.00]
	letterDict["W"] = [-0.296, -0.186, 0.389, 0.083, 0.297, 0.00]
	letterDict["Y"] = [-0.141, -0.057, 0.425, -0.096, -0.091, 0.00]
	letterDict["V"] = [-0.274, 0.136, -0.187, -0.196, -0.299, 0.00]
	letterDict["X"] = [0.000, 0.000, 0.000, 0.000, 0.00, 1]

	for char in string:
		for x in char:
			vectors += (letterDict[x])
	return vectors;

def vectorizeSequence1(letter):
	letterDict = {}
	letterDict["A"] = [0.008, 0.134, -0.475, -0.039, 0.181]
	letterDict["R"] = [0.171, -0.361, 0.107, -0.258, -0.364]
	letterDict["N"] = [0.255, 0.038, 0.117, 0.118, -0.055]
	letterDict["D"] = [0.303, -0.057, -0.014, 0.225, 0.156]
	letterDict["C"] = [-0.132, 0.174, 0.070, 0.565, -0.374]
	letterDict["Q"] = [0.149, -0.184, -0.030, 0.035, -0.112]
	letterDict["E"] = [0.221, -0.280, -0.315, 0.157, 0.303]
	letterDict["G"] = [0.218, 0.562, -0.024, 0.018, 0.106]
	letterDict["H"] = [0.023, -0.177, 0.041, 0.280, -0.021]
	letterDict["I"] = [-0.353, 0.071, -0.088, -0.195, -0.107]
	letterDict["L"] = [-0.267, 0.018, -0.265, -0.274, 0.206]
	letterDict["K"] = [0.243, -0.339, -0.044, -0.325, -0.027]
	letterDict["M"] = [-0.239, -0.141, -0.155, 0.321, 0.077]
	letterDict["F"] = [-0.329, -0.023, 0.072, -0.002, 0.208]
	letterDict["P"] = [0.173, 0.286, 0.407, -0.215, 0.384]
	letterDict["S"] = [0.199, 0.238, -0.015, -0.068, -0.196]
	letterDict["T"] = [0.068, 0.147, -0.015, -0.132, -0.274]
	letterDict["W"] = [-0.296, -0.186, 0.389, 0.083, 0.297]
	letterDict["Y"] = [-0.141, -0.057, 0.425, -0.096, -0.091]
	letterDict["V"] = [-0.274, 0.136, -0.187, -0.196, -0.299]
	letterDict["X"] = [0, 0, 0, 0, 1]

	return letterDict[letter];


def vectorizeSequenceAdd():
    letterDict = {}
    letterDict["A"] = -0.191
    letterDict["R"] = 0.303
    letterDict["N"] = 0.086
    letterDict["D"] = 0.613
    letterDict["C"] = 0.88
    letterDict["Q"] = -0.074
    letterDict["E"] = -0.672
    letterDict["G"] = 0.146
    letterDict["H"] = -0.492
    letterDict["I"] = -0.137
    letterDict["L"] = -0.582
    letterDict["K"] = 0.473
    letterDict["M"] = -0.142
    letterDict["F"] = 1.035
    letterDict["P"] = 0.158
    letterDict["S"] = -0.705
    letterDict["T"] = -0.206
    letterDict["W"] = 0.287
    letterDict["Y"] = -0.82
    letterDict["V"] = 0.04
    letterDict["X"] = 0
    return letterDict;

def vectorizeSequenceMult():
    letterDict = {}
    letterDict["A"] = 0.35944428
    letterDict["R"] = 33.97357656
    letterDict["N"] = 92.72634462
    letterDict["D"] = 0.84869694
    letterDict["C"] = -0.5610252672
    letterDict["Q"] = -0.0226646784
    letterDict["E"] = 4.601867556
    letterDict["G"] = 0.098143668
    letterDict["H"] = 3.18057597
    letterDict["I"] = -12.9105418365
    letterDict["L"] = -7.188651396
    letterDict["K"] = -0.73579077
    letterDict["M"] = -0.32241216
    letterDict["F"] = -166.255579776
    letterDict["P"] = -0.946861104
    letterDict["S"] = -62.0309138904
    letterDict["T"] = -0.542302992
    letterDict["W"] = 52.7945142384
    letterDict["Y"] = 40.8374238272
    letterDict["V"] = 2.98397736
    letterDict["X"] = 0
    return letterDict;



