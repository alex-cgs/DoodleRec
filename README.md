# DoodleRec Beta is live! - DoodleRec-Deep-Learning-Image-Recognition
DoodleRec - A Deep Learning algorithm trained on 10 objects from Google Quick Draw's data set, is my first Bachelor Semester Project at the University of Luxembourg.
#
## Disclaimer:
This BSP has been produced by Tinouert Alexandre Adrian, under the supervision of PAT PhD Student De Jesus Tiago as well as Pr. Dr. Guelfi Nicolas at the University of Luxembourg.
#

## How to use this program (so far):

### - If you want to try the early version of the user interface:
#### - Easy way (only on Windows, might upload a .sh soon):
1. Execute / Double-click DoodleRec.bat or its shortcut.
2. If the page doesn't display the application, refresh the page.
3. Enjoy!

#### - Vanilla way:
1. Run the Flask application from Visual Studio Code or any IDLE.
2. Go to the local port of the application (essentially http://127.0.0.1:5000).
3. Try to input some doodles, your image data array is updated every second on the website and in the console of the terminal where you run the Flask application, you can download your image data by clicking the button "Retrieve your Data".
4. DoodleRec's guess is on the page or on yourmatrix.txt.
5. Enjoy!


### - If you want to create a random data set to train the Neural Network with:
1. Go to https://onedrive.live.com/?id=57F1EE6756D7C71D%2125333&cid=57F1EE6756D7C71D and download the /data folder.
2. Place all .npy files (which are numpy array files) into the nn_training/data folder (remark the beacon txt file to guide located at where you should put the .npy files).
3. Launch setdata.py with an IDLE (make sure that your IDLE has the nn_training folder opened) and choose parameters.
4. The data.csv file is updated (located in nn_training/data).

### - If you want to train the Neural Network on said data:
1. Make sure that the data.csv file is not empty or corrupted. The provided .csv file contains the data of 10000 random doodles you can use and is a perfect fit.
2. Launch training.py with an IDLE.
3. Choose Learning Rate and Iterations
4. Enjoy!

### - If you want to test the Neural Network on said data:
1. Make sure that the data.csv file is not empty or corrupted. The provided .csv file contains the data of 10000 random doodles you can use and is a perfect fit.
2. Make sure the Neural Network is trained, nn.txt shall not be empty.
3. Choose how many image to test the Neural Network on.
4. Close the image (Pyplot popup) if you want to continue testing.

### - Important! To change the data set (if you don't want to download the .npy):
1. Different data.csv are furnished with different sizes. Rename the wanted data set to "data.csv".
