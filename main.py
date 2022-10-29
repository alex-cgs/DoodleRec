'''main.py'''
'''Github repository for this BSP: https://github.com/CookNChips/BSP1---DoodleRec-Deep-Learning-Image-Recognition'''
'''For easier use, please execute the DoodleRec.bat file provided with this, or read the README file'''

import os #To open the files needed for the Flask application, as well as the user's matrix yourmatrix.txt file
import json #To receive the JSON data from JavaScript requests
from flask import * #For the web application
import numpy as np #For testing datasets and open the data base that are .npy files


#Initialize the Flask applications with the static files
app = Flask(__name__)

path_cwd = os.path.dirname(os.path.realpath(__file__))
path_templates = os.path.join(path_cwd,"templates")
path_static = os.path.join(path_cwd,"static")


#Initialize the user's matrix from imported data, which is a 28x28 matrix
usermatrix = []
for i in range(0, 28):
  usermatrix.append([])
  for j in range(0, 28):
    usermatrix[i].append(0)


#Render the main page from the index.html static
@app.route('/')
def hello():
    return render_template('index.html')

#Receive the data from the JavaScript that arrives every second (1000ms)
@app.route("/", methods = ["post"])
def printer():
  userdata = request.get_json()
  userinput = userdata['userinput']

  #Open the "yourmatrix.txt" file and write an introductory line
  f = open("yourmatrix.txt", "w")
  f.write("Here is the image data of your doodle, with values ranging from 0 to 255 from the least contrasted to most contrasted parts of your doodle." + 2*"\n")

  #Transform the parsed data by writing the proper usermatrix and yourmatrix.txt file in a matrix format
  for i in range(0, 28):
    for j in range(0, 28):
      usermatrix[i][j] = userinput[28*i+j]
    f.write(str(usermatrix[i]) + "\n")
  print(usermatrix)

  #Close the .txt and return
  f.close()
  return usermatrix

#Download function - Downloads yourmatrix.txt
@app.route("/download")
def download_data():
  file = "yourmatrix.txt"
  return send_file(file, as_attachment=True)

#Run the application
app.run()