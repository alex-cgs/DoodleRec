# IMPENDING FIRST VERSION OF TECHNICAL DELIVERABLE BSP1 - DoodleRec-Deep-Learning-Image-Recognition
DoodleRec - A Deep Learning algorithm trained on 10 objects from Google Quick Draw's data set, is my first Bachelor Semester Project at the University of Luxembourg.

Current step: program the training algorithm and train it. Main GUI and UX done! You can use the web app to input doodles!
#
## Disclaimer:
This BSP has been produced by Tinouert Alexandre Adrian, under the supervision of PAT PhD Student DeJesus Tiago as well as Pr. Dr. Guelfi Nicolas at the University of Luxembourg.
#

## How to use this program (so far):

### - If you want to try the early version of the user interface:
#### - Easy way (only on Windows, might upload a .sh soon):
1. Execute / Double-click DoodleRec.bat or its shortcut.
2. If the page doesn't display the application, refresh the page.

#### - Vanilla way:
1. Run the Flask application from Visual Studio Code or any IDLE.
2. Go to the local port of the application (essentially http://127.0.0.1:5000).
3. Try to input some doodles, your image data array is updated every second on the website and in the console of the terminal where you run the Flask application, you can download your image data by clicking the button "Retrieve your Data".


### - If you want to create a random data set to train the Neural Network with:
1. Go to https://onedrive.live.com/?id=57F1EE6756D7C71D%2125333&cid=57F1EE6756D7C71D and download the /data folder...
2. Place all .npy files (which are numpy array files) into the nn_training/data folder (remark the beacon txt file to guide located at where you should put the .npy files).
3. Launch setdata.py with an IDLE (make sure that your IDLE has the nn_training folder opened) and choose parameters.
4. The data.csv file is updated (located in nn_training/data file).

### - If you want to train the Neural Network on said data:
1. Make sure that the data.csv file is not empty or corrupted.
2. Launch training.py with an IDLE.
3. Choose Learning Rate and Iterations
4. Enjoy!
