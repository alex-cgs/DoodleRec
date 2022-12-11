'''test.py'''
'''Github repository for this BSP: https://github.com/CookNChips/BSP1---DoodleRec-Deep-Learning-Image-Recognition'''
'''For easier use, please execute the DoodleRec.bat file provided with this, or read the README file'''

import os #To open the files needed for the Flask application, as well as the user's matrix yourmatrix.txt file
import pandas as pd #To read data.csv
import numpy as np #For testing datasets and open the data base that are .npy files
import matplotlib.pyplot as plt #For displaying the image
import random as rd #For selecting a random number

#List of possible guesses by the software. Will be used to display the result.
names = ["Airplane", "Cookie", "Cat", "Cup", "Hat", "Snowman", "Star", "Stop_sign", "Television", "Tree"]

#From training.py, we import the necessary functions in order to have redundancy between main.py and training.py
from doc import Sigmoid, Softmax, OneHot, ForwardPropagation, Prediction, Params

def Init():

    nb = input("Welcome to test.py! Test the Neural Network over random images from data.csv. Please specify a number of images to test on: ")

    try:
        nb = int(nb)
    except:
        os.sys.exit("Error: Must specify an integer.")
    
    return nb

nb = Init()

#Import the Weights and Biases from nn.txt
Weight1, Weight2, Bias1, Bias2 = Params()

data = pd.read_csv('nn_training/data/data.csv')
data = np.array(data)
print(data)

for i in range(nb):
    r = rd.randint(0, len(data) - 1)
    image = data[r]
    label = image[0]
    image = image[1:]
    imageR = image.reshape((28, 28)).tolist()
    image = np.tile(image, (10000, 1)).T

    Z1, A1, Z2, A2 = ForwardPropagation(image, Weight1, Bias1, Weight2, Bias2)

    #Find the prediction according to the Neural Network
    Guess = Prediction(A2)
    Guess = names[Guess[0].item()]
    print(f"Image {i + 1}: \n Label: {names[label]} \n Prediction: {Guess} \n Remaining image: {nb - i - 1}, please close the image to continue. \n \n \n")

    plt.gray()
    plt.imshow(imageR, interpolation='nearest')
    plt.show()
