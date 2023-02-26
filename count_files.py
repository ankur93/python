###################################################
#### Print line count all files in a directory ####
###################################################

import json
import os

folder_path = "/nail/home/ankuragrawal/review_export_0"
files = []
for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        files.append(filename)


for file_name in files:
    if file_name not in ['.DS_Store']:
        with open(f'{folder_path}', 'r') as file:
            line_count=0
            for line in file:
                line_count=line_count+1
            print(line_count)


