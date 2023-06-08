import subprocess

import os
from PIL import Image

def jarWrapper(arr_steg):
    try:
        subprocess.call(['java', '-jar', arr_steg[0], arr_steg[1], arr_steg[2], arr_steg[3], arr_steg[4]])

    except:
        print("StegExpose - Error!")


arr_steg = ['StegExpose.jar', 'testFolder', 'default', '0.2', 'check.csv']  # Any number of args to be passed to the jar file
jarWrapper(arr_steg)


# Set the directory path
directory = "/home/kali/PycharmProjects/checkCombain/testFolder/"

# Loop over all files in the directory
for filename in os.listdir(directory):
    # Check if the file is an image (PNG or JPEG)
    if filename.endswith(".png"):
        # Print the file name

        targetImage = Image.open(directory+filename)
        print(targetImage.text)
