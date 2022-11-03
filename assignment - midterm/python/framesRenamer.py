#This Script 


import os
import json
import shutil

#Count digits
def digitFinder(frameCount):
    divider = 10
    digitCount = 0
    while frameCount >= 1:
        frameCount = frameCount / divider
        digitCount += 1

    return digitCount 

#Write JSON file
jsonInfo = {
    "FilesDirectory": "C:/Users/ljohn/OneDrive/Desktop/anim-t380-2022-assignments/anim-t380-2022-assignments/assignment - midterm/etc/png_tests",
    "NewName": "jsonTest",
    "ImageType": "png",
    "ZipName" : "jsonZIP"
}

with open("framesJson.json", "w") as outfile:
    json.dump(jsonInfo, outfile)


# Opening JSON file
with open('framesJson.json', 'r') as openfile:
 
    # Reading from json file
    jsonObject = json.load(openfile)


#Get folder path from JSON file
fPath = jsonObject['FilesDirectory']
print(fPath)

#Get list of files in folder
files = os.listdir(fPath)

#Get desired file name from JSON file
fName = jsonObject['NewName']

#Get file type from JSON file
fExt = jsonObject['ImageType']

#Get number of files and determine frame buffer
fCount = len(files)

fPadCount = digitFinder(fCount)

#Rename files
fNum = 1
for file in files:
    #Determine if file is a frame or not
    if file.split('.')[-1] == fExt:

        #Update frame padding
        fPad = ''
        newFrameDig = digitFinder(fNum)
        while fPadCount - newFrameDig >= 0:
            fPad += '0'
            newFrameDig += 1

        #Rename files
        oldFile = fPath + '/' + file
        newFile = fPath + '/' + fName + '_' + fPad + str(fNum) + '.' + fExt
        fNum = int(fNum) + 1
        os.rename(oldFile, newFile)
    else:
        continue



#Zip File
shutil.make_archive(jsonObject['ZipName'], 'zip', fPath)
print('Zipped file at {}'.format(fPath))