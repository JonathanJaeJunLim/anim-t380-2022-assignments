#Make Maya file directory

export Foo=boo

python

import os

os.getenv('FOO') 
#envLoc = os.getenv('envSet') 
#envLoc = str(envLoc)
#splitEnv = envLoc.split('/')
#print(splitEnv)
#+ '/assets/$asset/maya/scenes'
#print(envLoc)
#os.makedirs(envLoc)