'''doc.py'''
'''Github repository for this BSP: https://github.com/CookNChips/BSP1---DoodleRec-Deep-Learning-Image-Recognition'''
'''Only usable via IDLE for now'''
'''Please execute training.py for training'''


'''Part 0°. Initialisation of data set and parameters'''

#Import needed libraries to read data (csv and .npy files)
import numpy as np
import pandas as pd
import os
import json


#Prompt the user for a LearningRate and an Iteration number
def Prompt():

    LearningRate = input("Welcome to training.py! Make sure the .csv file is ready to use (by launching setdata.py). Please specify a learning rate (would recommend no more than 1, must be an integer or a float): ")

    try:
        LearningRate = float(LearningRate)
    except:
        os.sys.exit("Error: Must specify a float.")

    Iterations = input("How many iterations? (Please specify an integer) ")

    try:
        Iterations = int(Iterations)
    except:
        os.sys.exit("Error: Must specify an integer.")
    
    return LearningRate, Iterations



#Initialize data into into a set of training data
data = pd.read_csv('nn_training/data/data.csv')
data = np.array(data)
x, y = data.shape

TrainingData = data.T
Labels = TrainingData[0]
DoodleData = TrainingData[1:y]
DoodleData = DoodleData


#Initialize random parameters for weights and biases
def Parameters():
    Weight1 = np.random.rand(10, 784) - 0.5
    Bias1 = np.random.rand(10, 1) - 0.5
    Weight2 = np.random.rand(10, 10) - 0.5
    Bias2 = np.random.rand(10, 1) - 0.5
    return Weight1, Bias1, Weight2, Bias2


'''Part 1°. Mathematical functions: Activation, Derivative, and Loss functions'''

#Sigmoid function for an entire matrix
def Sigmoid(Matrix):
    return 1 / (1 + np.exp(-Matrix))

#Sigmoid derivative function for an entire matrix
def SigmoidDerivative(Matrix):
    Sigma = Sigmoid(Matrix)
    return Sigma * (1 - Sigma)

#Softmax function for an entire matrix
def Softmax(Matrix):
    A = np.exp(Matrix) / sum(np.exp(Matrix))
    return A

#OneHot encoding function for an entire matrix
def OneHot(Matrix):
    OneHotMatrix = np.zeros((Matrix.size, Matrix.max() + 1))
    OneHotMatrix[np.arange(Matrix.size), Matrix] = 1
    OneHotMatrix = OneHotMatrix.T
    return OneHotMatrix


'''Part 2°. Neural Network functions: ForwardPropagation, BackwardPropagation, NewParameters and LowOnCurve'''

#Step 1) ForwardPropagation: we apply weights and biases to the matrix with Sigmoid and Softmax as activation functions
def ForwardPropagation(Matrix, Weight1, Bias1, Weight2, Bias2):
    Z1 = Weight1.dot(Matrix) + Bias1
    A1 = Sigmoid(Z1)
    Z2 = Weight2.dot(A1) + Bias2
    A2 = Softmax(Z2)
    return Z1, A1, Z2, A2

#Step 2) BackwardPropagation: we apply the obtained results with the SigmoidDerivative and OneHot as loss functions
def BackwardPropagation(Mat1, Mat2, Z1, A1, Z2, A2, Weight1, Weight2):
    OneHotMatrix = OneHot(Mat2)
    dZ2 = A2 - OneHotMatrix
    derWeight2 = 1 / x * dZ2.dot(A1.T)
    derBias2 = 1 / x * np.sum(dZ2)
    dZ1 = Weight2.T.dot(dZ2) * SigmoidDerivative(Z1)
    derWeight1 = 1 / x * dZ1.dot(Mat1.T)
    derBias1 = 1 / x * np.sum(dZ1)
    return derWeight1, derBias1, derWeight2, derBias2

#Step 3) According to the error margin, we update the parameters while taking into account the learning rate
def NewParamaters(Rate, Weight1, Bias1, Weight2, Bias2, derWeight1, derBias1, derWeight2, derBias2):
    Weight1 = Weight1 - Rate * derWeight1
    Bias1 = Bias1 - Rate * derBias1    
    Weight2 = Weight2 - Rate * derWeight2  
    Bias2 = Bias2 - Rate * derBias2    
    return Weight1, Bias1, Weight2, Bias2


'''Part 3°. Accuracy and Prediction functions'''

#Prediction function: we use np.argmax() to take the prediction label
def Prediction(A2):
    return np.argmax(A2, 0)

#Accuracy function
def Accuracy(Predictions, Matrix):
    print("Prediction: " + str(Predictions) + "\n" + "Reference: " + str(Matrix))
    return np.sum(Predictions == Matrix) / Matrix.size


'''Part 4°. Execute every said function, which happens to find low points on the probability curve using derivatives'''

#LowOnCurve function
def LowOnCurve(Mat1, Mat2, Rate, Iteration):

    #Initialize our parameters
    Weight1, Bias1, Weight2, Bias2 = Parameters()

    #Apply all cited steps
    for i in range(Iteration):
        Z1, A1, Z2, A2 = ForwardPropagation(Mat1, Weight1, Bias1, Weight2, Bias2)
        derWeight1, derBias1, derWeight2, derBias2 = BackwardPropagation(Mat1, Mat2, Z1, A1, Z2, A2, Weight1, Weight2)
        Weight1, Bias1, Weight2, Bias2 = NewParamaters(Rate, Weight1, Bias1, Weight2, Bias2, derWeight1, derBias1, derWeight2, derBias2)

        #Every 100th iteration, we print the prediction and accuracy of the process
        if i % 100 == 0:
            Predictions = Prediction(A2)
            print("Iteration: " + str(i))
            print("Accuracy: " + str(Accuracy(Predictions, Mat2).item()*100) + "%" + "\n")
    
    return Weight1, Bias1, Weight2, Bias2


'''Part 5°. Appendix / Support'''
#Params() function, to import the Neural Network's Weights and Biases to compute.
def Params():

    #Open nn.txt as read
    f = open("nn.txt","r")

    #Create a counter
    counter = 1

    #Iterate through the lines to find Weights and Biases in nn.txt
    for line in f:
        if counter == 3:
            Weight1 = json.loads(line)
        if counter == 4:
            Weight2 = json.loads(line)
        if counter == 5:
            Bias1 = json.loads(line)
        if counter == 6:
            Bias2 = json.loads(line)
        counter = counter + 1

    f.close()

    #Transform the arrays back into numpy arrays
    Weight1 = np.array(Weight1)
    Weight2 = np.array(Weight2)
    Bias1 = np.array(Bias1)
    Bias2 = np.array(Bias2)

    return Weight1, Weight2, Bias1, Bias2