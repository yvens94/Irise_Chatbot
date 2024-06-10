import json
import os
import requests
import pandas as pd



model_id = "sentence-transformers/all-MiniLM-L6-v2"
hf_token = "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"

api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_id}"
headers = {"Authorization": f"Bearer {hf_token}"}


def query(texts):
    response = requests.post(api_url, headers=headers, json={"inputs": texts, "options":{"wait_for_model":True}})
    return response


def create_embeddings(json_scraped_master):
    #json_scraped_master =r'C:\Users\Owner\OneDrive - Reformed Church of Highland Park Affordable Housing Corporation\Documents\Python Scripts\Refugee_Benefits_ChatBot\Irise_Chatbot\data\Raw_data\master_json.json'
    if not os.path.exists(json_scraped_master):
            print("the specified json_scraped directory does not exist")
    else:
        with open(json_scraped_master,'r') as file:
            text= json.load(file)

            master_strings = [json.dumps(dictionary) for dictionary in text]

            output2 = query(master_strings)

            embeddings = pd.DataFrame(output2)
            return embeddings
        
json_scraped_master =r'C:\Users\Owner\OneDrive - Reformed Church of Highland Park Affordable Housing Corporation\Documents\Python Scripts\Refugee_Benefits_ChatBot\Irise_Chatbot\data\Raw_data\master_json.json'
df=create_embeddings(json_scraped_master)

print(df.head())