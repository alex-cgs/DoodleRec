'''main.py'''
'''Github repository for this BSP: https://github.com/CookNChips/BSP1---DoodleRec-Deep-Learning-Image-Recognition'''
'''For easier use, please execute the DoodleRec.bat file provided with this, or read the README file'''

import os #To open the files needed for the Flask application, as well as the user's matrix yourmatrix.txt file
import json #To receive the JSON data from JavaScript requests
from flask import * #For the web application
import numpy as np #For testing datasets and open the data base that are .npy files


#From training.py, we import the necessary functions in order to have redundancy between main.py and training.py
from doc import Sigmoid, Softmax, OneHot, ForwardPropagation, Prediction, Params

#Import the Weights and Biases from nn.txt
Weight1, Weight2, Bias1, Bias2 = Params()

#Initialize the Flask applications with the static files
app = Flask(__name__)

path_cwd = os.path.dirname(os.path.realpath(__file__))
path_templates = os.path.join(path_cwd,"templates")
path_static = os.path.join(path_cwd,"static")


#List of possible guesses by the software. Will be used to display the result.
names = ["Airplane", "Cookie", "Cat", "Cup", "Hat", "Snowman", "Star", "Stop_sign", "Television", "Tree"]


#Initialize the user's matrix from imported data, which is a 28x28 matrix
usermatrix = []
for i in range(0, 28):
  usermatrix.append([])
  for j in range(0, 28):
    usermatrix[i].append(0)


#Render the main page from the index.html static
@app.route('/')
def hello():
    return render_template('index.html', data="True")

#Receive the data from the JavaScript that arrives every second (1000ms)
@app.route("/", methods = ["post"])
def Compute():
  userdata = request.get_json()
  userinput = userdata['userinput']

  #Open the "yourmatrix.txt" file and write an introductory line
  f = open("yourmatrix.txt", "w")
  f.write("Here is the image data of your doodle, with values ranging from 0 to 255 from the least contrasted to most contrasted parts of your doodle." + 2*"\n")

  #Transform the parsed data by writing the proper usermatrix and yourmatrix.txt file in a matrix format
  for i in range(0, 28):
    for j in range(0, 28):
      usermatrix[i][j] = userinput[28*i + j]
    f.write(str(usermatrix[i]) + "\n")

  #Close the .txt
  f.close()

  #Initialize the Final matrix
  Final = [userinput]

  #Take the user input and transform it into a numpy array to compute
  Final = np.array(Final).T

  #Check if Final is not a 0 matrix
  if not np.any(Final):
    print(None)
    return "None"
  
  #Pass into the Neural Network only one time
  Z1, A1, Z2, A2 = ForwardPropagation(Final, Weight1, Bias1, Weight2, Bias2)

  #Find the prediction according to the Neural Network
  Guess = Prediction(A2)
  Guess = names[Guess[0].item()]
  print(Guess)

  return Guess

#Download function - Downloads yourmatrix.txt
@app.route("/download")
def download_data():
  file = "yourmatrix.txt"
  return send_file(file, as_attachment=True)

#Run the application
app.run()