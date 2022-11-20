'''training.py'''
'''Github repository for this BSP: https://github.com/CookNChips/BSP1---DoodleRec-Deep-Learning-Image-Recognition'''
'''Only usable via IDLE for now'''

#Import needed libraries to read data (csv and .npy files)
import numpy as np
import pandas as pd
import os

#Import functions from doc.py
from doc import *

#Prompt user for LearningRate and number of Iterations
LearningRate, Iterations = Prompt()

#Compute the Weights and Biases
Weight1, Bias1, Weight2, Bias2 = LowOnCurve(DoodleData, Labels, LearningRate, Iterations)

#Transform them into strings
Weight1 = str(Weight1.tolist())
Weight2 = str(Weight2.tolist())
Bias1 = str(Bias1.tolist())
Bias2 = str(Bias2.tolist())

#Write the values in nn.txt
f = open("nn.txt", "w")
f.write("Neural Network Weights (1, 2) and Biases (1, 2):" + 2*"\n" + Weight1 + "\n" + Weight2 + "\n" + Bias1 + "\n" + Bias2)

print("Training is done! nn.txt is now correctly updated with your Weight1, Weight2, Bias1 and Bias2 matrices. Please rerun DoodleRec (main.py) to update the Neural Network.")