'''setdata.py'''
'''Prepares a random set of data of 10000 doodles from .npy files to a .csv file'''

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
airplane = np.load(os.getcwd() + "\\data\\airplane.npy", allow_pickle=True)
cookie = np.load(os.getcwd() + "\\data\\cookie.npy", allow_pickle=True)
cat = np.load(os.getcwd() + "\\data\\cat.npy", allow_pickle=True)
cup = np.load(os.getcwd() + "\\data\\cup.npy", allow_pickle=True)
hat = np.load(os.getcwd() + "\\data\\hat.npy", allow_pickle=True)
snowman = np.load(os.getcwd() + "\\data\\snowman.npy", allow_pickle=True)
star = np.load(os.getcwd() + "\\data\\star.npy", allow_pickle=True)
stop_sign = np.load(os.getcwd() + "\\data\\stop_sign.npy", allow_pickle=True)
television = np.load(os.getcwd() + "\\data\\television.npy", allow_pickle=True)
tree = np.load(os.getcwd() + "\\data\\tree.npy", allow_pickle=True)

#Indexing the data in a list
index = [airplane, cookie, cat, cup, hat, snowman, star, stop_sign, television, tree]

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