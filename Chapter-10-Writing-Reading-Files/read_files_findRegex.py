import re
import os

baseFolder = "Chapter-10-Writing-Reading-Files/"
txtFiles = [file for file in os.listdir(baseFolder) if "txt" in file]

for txtFile in txtFiles:
    with open(txtFile,)