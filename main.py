#To properly use this program to visualize the set of data, please find them here: https://1drv.ms/u/s!Ah3H11Zn7vFXgcV1ZtpBQygZ8jSusw?e=SE4IxR
#And place the /data folder aside with the main.py program.

import os
import json
from flask import *
import numpy as np

app = Flask(__name__)

path_cwd = os.path.dirname(os.path.realpath(__file__))
path_templates = os.path.join(path_cwd,"templates")
path_static = os.path.join(path_cwd,"static")

@app.route('/')
def hello():
    return render_template('index.html')

@app.route("/", methods = ["post"])
def printer():
  userdata = request.get_json()
  print(userdata["userinput"])
  return userdata

A = np.load("data/cookie.npy", allow_pickle=True)
c = len(A)
a = A[0]
B = np.reshape(a, (28,28))
"""print(B)
print(c)"""


app.run()