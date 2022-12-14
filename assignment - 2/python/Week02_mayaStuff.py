#Creating Torus Tree in Maya standalone mode

import argparse

#Get Tree height input from user
parser = argparse.ArgumentParser(description='This script creates a torus tree.')
parser.add_argument('treeHeight', type=int, help='Number of toruses')

args = parser.parse_args()

#Initialize Maya Standalone
import maya.standalone
maya.standalone.initialize()

#Print Tree Creation
import maya.cmds as cmds

print('Creating a {} torus high tree'.format(args.treeHeight))

mainRadius = 1
sectionRadius = 0.2

#Create Torus Tree
for i in range(args.treeHeight):
    print('Created #{} level'.format(i))
    cmds.polyTorus(sx = 36, sy = 16, r = mainRadius, sr = sectionRadius)
    cmds.move(0, -mainRadius , 0)
    mainRadius += 1
    sectionRadius += 0.1
    cmds.select( clear=True )


#Print meshes in scene
print('Meshes in the Maya scene:')
print(cmds.ls(geometry=True))


#Save file
cmds.file(rename = 'TorusTree')
cmds.file(save = True, de = False, type = 'mayaAscii')