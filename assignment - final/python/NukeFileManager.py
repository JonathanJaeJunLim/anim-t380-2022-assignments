#Creates menu in Nuke

#import nuke
#import 'YOUR PY SCRIPT NAME'
import os

#Pop Up Window for File Path
p = nuke.Panel('File Import Manager')

p.addFilenameSearch('file path', '/tmp')
# p.addSingleLineInput('Enter version:', '')
popWindow = p.show()

#Assign Directory path to variable
fPath = p.value('file path')
files = os.listdir(fPath)

#Get unique sequence names
sequences = []
baseName = 'Nothing'
fileBaseNum = ''
num = '1234567890'
fileBase = ''
firstFile = files[0]
fExt = firstFile.split('.')[-1]

for file in files:
    if baseName in file:
        continue
    
    else:
        fileBaseNum = file.split('.')
        fileBaseNum.pop()
        charList = list(fileBaseNum[0])
        while charList[-1] in num:
            charList.pop()
        for i in charList:
            fileBase += i
        sequences.append(fileBase)
        baseName = fileBase
        fileBase = ''

#Pop Up Window for User to Select which elements to bring in
class ShapePanel(nukescripts.PythonPanel):
    def __init__(self, node):
                nukescripts.PythonPanel.__init__(self, 'RotoPaint Elements')
                self.rpNode = node

                self.typeKnob = nuke.Bitmask_Knob('element', 'File Sequences', sequences)
                self.addKnob(self.typeKnob)

p = ShapePanel(node)
p.showModalDialog()

sFiles = p.typeKnob.value()
sFiles = sFiles.split()


fileNum = 0
fPath = fPath.replace( '\\' , '/' )
for i in sFiles:
    # for file in files:
    #     if i in file:
    #         fileNum += 1
    #     else:
    #         continue
    sFilePath = fPath + '/' + i + '####' + '.' + fExt
    #  + ' ' + '1-' + fileNum
    # sFilePath = '{}/{}####{} 1-{}'.format()
    nuke.nodes.Read (file=sFilePath)


#Create write output, destination and naming convention, by reading the JSON file