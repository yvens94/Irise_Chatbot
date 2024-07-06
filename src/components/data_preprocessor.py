

import json
import os
import textwrap
import re
from unidecode import unidecode

from langchain.text_splitter import RecursiveCharacterTextSplitter, SentenceTransformersTokenTextSplitter
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

wrapper =textwrap.TextWrapper(width=70)

def master_json_loader(path) -> list:
    if not os.path.exists(path):
        print("The specified JSON file does not exist")
        return []
    else:
        with open(path, 'r') as file:
            text = json.load(file)
            master_strings = [json.dumps(dictionary) for dictionary in text]
    return master_strings

def master_string2text(master_strings):
    return ''.join(master_strings)

def clean_text(text2cha):
    if not text2cha:
        return ""

    try:
        text = text2cha.encode('utf-8').decode('unicode_escape')
    except UnicodeDecodeError:
        print("Unicode decode error encountered")
        return ""

    text = unidecode(text)
    text = re.sub(r'\\u[0-9a-fA-F]{4}', '', text)
    text = text.replace('\xa0', ' ')
    text = re.sub(r'\s+', ' ', text).strip()

    return text

def character_splitter(text):
    text2embed = wrapper.wrap(text)
    character_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ". ", " ", ""],
        chunk_size=8000,
        chunk_overlap=1000
    )
    character_split_texts = character_splitter.split_text('\n\n'.join(text2embed))
    return character_split_texts

def token_splitter(character_split_texts):
    token_splitter = SentenceTransformersTokenTextSplitter(chunk_overlap=0, tokens_per_chunk=256)
    token_split_texts = []

    for text in character_split_texts:
        token_split_texts += token_splitter.split_text(text)

    print(f"\nTotal chunks: {len(token_split_texts)}")
    return token_split_texts

# root = os.path.dirname(os.path.abspath(os.curdir))
 

wk_dir =os.getcwd()

master_json_path  = r'data\Raw_data\master_json.json'
path =os.path.join(wk_dir,master_json_path)

chromadir= os.path.join(wk_dir, "interfaithrise_rag_imfo")
os.makedirs(chromadir, exist_ok=True)
chroma_client = chromadb.PersistentClient(path=chromadir)

master_strings = master_json_loader(path)
if master_strings:
    text2cha = master_string2text(master_strings)
    text = clean_text(text2cha)
    character_split_texts = character_splitter(text)
    token_split_texts = token_splitter(character_split_texts)
    ids = [str(i) for i in range(len(token_split_texts))]
  
    
    embedding_function = SentenceTransformerEmbeddingFunction()
    chroma_collection = chroma_client.get_or_create_collection(name="interfaithrise_info", embedding_function=embedding_function)
    chroma_collection.add(ids=ids, documents=token_split_texts)
    print(chroma_collection.count())
else:
    print("No data loaded from JSON")

