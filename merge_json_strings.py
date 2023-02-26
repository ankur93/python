####################################################################
#### Merge individual JSON line strings into a single JSON line ####
####################################################################

import json
import os

leaf_dir="review_export"
folder_path = "/nail/tmp/ankur_new1/review_export"
files = []
for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        files.append(filename)

for file_name in files:
    if file_name not in ['.DS_Store']:
        print(f"opening file: {file_name}")
        with open(f'{file_name}', 'r') as file:
            with open(f'{folder_path}/{file_name}', 'w') as file_merged:
                merged_object = {}
                # line_count=0
                for line in file:
                    try:
                        json_object = json.loads(line.strip())
                        merged_object.update(json_object)
                    except json.JSONDecodeError as e:
                        print(f'Error: {e}')
                try:
                    file_merged.write(json.dumps(merged_object))
                    print(f"wrote to file: {folder_path}/{file_name}_merged")
                except Exception as e:
                    print(f"Exception: {e}")


