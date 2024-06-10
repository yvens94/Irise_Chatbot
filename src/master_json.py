import json
import os


json_scraped_folder =r'C:\Users\Owner\OneDrive - Reformed Church of Highland Park Affordable Housing Corporation\Documents\Python Scripts\Refugee_Benefits_ChatBot\Irise_Chatbot\data\Raw_data\json_scraped'
if not os.path.exists(json_scraped_folder):
        print("the specified json_scraped directory does not exist")
else:
    json_files =os.listdir(json_scraped_folder)

master_json = []


for file in json_files:
      file_path_json=os.path.join(json_scraped_folder,file)
      with open(file_path_json, 'r', encoding='utf-8') as f:
            data= json.load(f)
            master_json.append(data)

curr_path = os.getcwd()
master_json_file= os.path.join(curr_path,r'data\Raw_data\master_json.json' )

with open(master_json_file, 'w') as f:
      json.dump(master_json,f, indent=4)