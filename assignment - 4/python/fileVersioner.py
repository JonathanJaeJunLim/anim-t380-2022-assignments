#This script saves your file as a new version
import maya.cmds as cmds


#Extract file name from file path
filepath = cmds.file

oldFilePath = filepath(q=True, exn = True)
oldFilePathSplit = (oldFilePath.split('/'))
oldFile = oldFilePathSplit.pop()

asset, state, style, version = oldFile.split("_")
version, ext = version.split(".")


#Version up the current file
ver = int(version) + 1

if ver <= 9:
    newVer = str(0) + str(ver)
else:
    newVer = ver

newFile = asset + '_' + state + '_' + style + '_' + newVer + '.' + ext




#Save as new Version
cmds.file(rename = newFile)
cmds.file(save = True, type = 'mayaAscii')