#This Script 


import os

#Count digits
def digitFinder(frameCount):
    divider = 10
    digitCount = 1
    while frameCount > 1:
        frameCount = frameCount / divider
        divider *= 10
        digitCount += 1

    fPadding = digitCount + 1
    return fPadding

#Get folder path from user
print('Enter target folder: ')
fPath = input()

#Get desired file name from user
print('File name: ')
fName = input()

#Get list of files in folder
files = os.listdir(fPath)

#Get file type
firstFile = files[0]
fExt = firstFile.split('.')[-1]

#Get number of files and determine frame buffer
fCount = len(files)

fPadCount = digitFinder(fCount)

#Rename files
fNum = 1
for file in files:
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