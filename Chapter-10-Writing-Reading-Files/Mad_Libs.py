from pathlib import Path
import re
import os

base_fileName = "Chapter-10-Writing-Reading-Files/MadLibs-Output"
counter = 1
filename = f"{base_fileName}.txt"

with open(Path.cwd() / "Chapter-10-Writing-Reading-Files/MadLibs-Input.txt","r",encoding="utf-8") as mad_libs_fileObject:
    MadLibs_content = mad_libs_fileObject.read()

def replace_placeholder(match):
    return input(f"Enter a {match.group().lower()}: ")

result = re.sub(r'\b[A-Z]{2,}\b',replace_placeholder,MadLibs_content)
print(result)

while os.path.exists(filename):
    filename = f"{base_fileName}_{counter}.txt"
    counter+=1

with open(filename,"w",encoding="utf-8") as fileObj:
    fileObj.write(result)





""" for mad_word in ["ADJECTIVE", "VERB","NOUN","ADVERB"]: # , "VERB","NOUN","ADVERB"
    while mad_word in MadLibs_content:
        if mad_word == "ADVECTIVE":
            user_input = input(f"Enter an {mad_word.lower()}")
        else:
            user_input = input(f"Enter a {mad_word.lower()}")
        MadLibs_content = MadLibs_content.replace(mad_word,user_input,1)

print(MadLibs_content) """