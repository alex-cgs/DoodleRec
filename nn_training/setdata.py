#setdata.py
#Prepares a random set of data of 10000 doodles

#Import needed libraries to exploit data
import csv
import numpy as np
import random
import os

#Initialize the user to choose how many entries need to be generated and shuffled
nb = input("You launched setdata.py! Please enter a number of entries to shuffle (would recommend around 10000): ")

#Verifies if the user has inputted an integer
try:
    nb = int(nb)
except:
    os.sys.exit("Invalid input. Please make sure to only enter integers.")

print("Please wait...")

#Import all the data from .npy files
apple = np.load(os.getcwd() + "\\data\\apple.npy", allow_pickle=True)
basketball = np.load(os.getcwd() + "\\data\\basketball.npy", allow_pickle=True)
circle = np.load(os.getcwd() + "\\data\\circle.npy", allow_pickle=True)
cookie = np.load(os.getcwd() + "\\data\\cookie.npy", allow_pickle=True)
moon = np.load(os.getcwd() + "\\data\\moon.npy", allow_pickle=True)
pizza = np.load(os.getcwd() + "\\data\\pizza.npy", allow_pickle=True)
smileyface = np.load(os.getcwd() + "\\data\\smileyface.npy", allow_pickle=True)
snowman = np.load(os.getcwd() + "\\data\\snowman.npy", allow_pickle=True)
sun = np.load(os.getcwd() + "\\data\\sun.npy", allow_pickle=True)
wheel = np.load(os.getcwd() + "\\data\\wheel.npy", allow_pickle=True)

#Indexing the data in a list
index = [apple, basketball, circle, cookie, moon, pizza, smileyface, snowman, sun, wheel]

#Prepare the header of the csv output file
header = ["label"]

#Add the pixel numbers to the header
for i in range(784):
    header.append("Px" + str(i))

#Prepare the data array
data = []

#Choose random doodles among the .npy files and append them to the data array
for i in range(nb):
    rand1 = random.randint(0, 9)
    rand2 = random.randint(0, 100000)
    toapp = np.insert(index[rand1][rand2], 0, rand1)
    toapp = toapp.tolist()
    data.append(toapp)

#Write the header and the data array in the csv file
with open(os.getcwd() + "\\data\\data.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)

#Inform the user that the process is done
print("Shuffling Done!" + "\n" + "Your data/data.csv file is ready for use! It is composed of a column of label (from 0 being an apple to 9 being a wheel) with pixel values on rows." + "\n" + "You can now safely close this terminal instance." + "\n" + "Please check GitHub for more informations!")