import json
import os

#putting all  the json files together

workdir = os.getcwd()
json_folder = r'data\Raw_data\json_scraped'
json_scraped_folder = os.path.join(workdir, json_folder)
if not os.path.exists(json_scraped_folder):
        print("the specified json_scraped directory does not exist")
else:
    json_files = os.listdir(json_scraped_folder)

master_json = []


for file in json_files:
      file_path_json = os.path.join(json_scraped_folder,file)
      with open(file_path_json, 'r', encoding ='utf-8') as f:
            data = json.load(f)
            #put the data in the master Json list, all json files into one list
            master_json.append(data)

curr_path = os.getcwd()
master_json_file = os.path.join(curr_path,r'data\Raw_data\master_json.json' )

with open(master_json_file, 'w') as f:
      json.dump(master_json,f, indent=4)