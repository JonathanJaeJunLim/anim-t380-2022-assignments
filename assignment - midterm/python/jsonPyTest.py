#Tests for JSON files

import json

import os

#  asset_info = {
#  "project": 'testProj',
#  }

# print(asset


# Data to be written
jsonInfo = {
    "Directory": "C:/Users/ljohn/OneDrive/Desktop/anim-t380-2022-assignments/anim-t380-2022-assignments/assignment - midterm\etc",
    "NewName": "jsonVarTest",
    "ImageType": "png"
}

 
with open("framesJson.json", "w") as outfile:
    json.dump(jsonInfo, outfile)


# Opening JSON file
with open('framesJson.json', 'r') as openfile:
 
    # Reading from json file
    json_object = json.load(openfile)
 
print(json_object['NewName'])


# with open(r'C:\Users\ljohn\OneDrive\Desktop\anim-t380-2022-assignments\anim-t380-2022-assignments\assignment - midterm\python\jsonTest.json', 'r') as f:
#   data = json.load(f)

# # Output: {'name': 'Bob', 'languages': ['English', 'French']}
# print(data)
    

# Opening JSON file
#f = open(r'C:\Users\ljohn\OneDrive\Desktop\anim-t380-2022-assignments\anim-t380-2022-assignments\assignment - midterm\python\jsonTest.txt', 'r')
#print(f)


# # returns JSON object as 
# # a dictionary
# data = json.load(f)

# # Iterating through the json
# # list

# for i in data['Directory']:
#     print(i)
   
# # Closing file
# f.close()