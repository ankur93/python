############################################################################################
#### Merge individual JSON files(chunks) for the same timestamp into a single JSON file ####
############################################################################################

import os
import json
from datetime import timedelta
import time
from datetime import datetime
from collections import defaultdict

timestamps = [(datetime.strptime("02/01/23", "%m/%d/%y").date() - timedelta(days=90*offset)).strftime("%m_%d_%y") for offset in range(0,20)]
folder_path = "/nail/tmp/ankur_new1/review_export/to_merge"
files = []
for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        files.append(filename)


file_name_registry= defaultdict(list)
for timestamp in timestamps:
    for file_name in files:
        if file_name not in ['.DS_Store'] and file_name.startswith(f"reviews_{timestamp}"):
            file_name_registry[timestamp].append(file_name)


for timestamp,value in file_name_registry.items():
    merged_json_attributes = {}
    for file_name in value:
        with open(f'{folder_path}/{file_name}', 'r') as file:
            for line in file:
                try:
                    merged_json_attributes.update(json.loads(line.strip()))
                    print(f"merged file {file_name}")
                except json.JSONDecodeError as e:
                    print(f'Error: {e}')
    print(f"merged json attributes length: {len(merged_json_attributes)}")
    with open(f'{folder_path}/review_export_merged_0/{timestamp}_attributes', 'w') as file_merged:
        print(f"writing to file: {folder_path}/{timestamp}_reviews")
        file_merged.write(json.dumps(merged_json_attributes))


