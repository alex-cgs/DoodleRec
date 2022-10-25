# IMPENDING FIRST VERSION OF TECHNICAL DELIVERY BSP1 - DoodleRec-Deep-Learning-Image-Recognition
DoodleRec - A Deep Learning algorithm trained on 10 objects from Google Quick Draw's data set, is my first Bachelor Semester Project at the University of Luxembourg.

Current step: program the training algorithm and train it.
#
## Disclaimer:
This BSP has been produced by Tinouert Alexandre Adrian, under the supervision of PAT PhD Student DeJesus Tiago as well as Pr. Dr. Guelfi Nicolas at the University of Luxembourg.
#

## How to use this program (so far):

### - If you want to try the early version of the user interface:
#### - Easy way:
1. Execute / Double-click DoodleRec.bat or its shortcut.
2. If the page doesn't display the application, refresh the page.

#### - Vanilla way:
1. Run the Flask application from Visual Studio Code or any IDLE.
2. Go to the local port of the application (essentially http://127.0.0.1:5000).
3. Try to input some doodles, your image data array is updated every 500ms on the website and in the console of the terminal where you run the Flask application.


### - If you want to visualize the dataset:

1. Go to https://onedrive.live.com/?id=57F1EE6756D7C71D%2125333&cid=57F1EE6756D7C71D and download the /data folder.
2. Place it aside with the main.py program.
3. In the main.py program, comment/delete the Flask part, and modify the needed parameters. You will then be able to display the 28x28 arrays.