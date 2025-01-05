from datasets import Dataset
import sys
import os
import textwrap
from rag_pipeline import rag, retriever
from components.data_preprocessor import chroma_client
from dotenv import load_dotenv, find_dotenv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from components import query_preprocessor 
from components.data_preprocessor import chroma_client

def main():
    question =str(input('Ask a question to David: '))

    query = query_preprocessor.query_prepo(original_query = question)

    retrieved_documents1 = retriever(chroma_client, query)

    output_final1= rag(query, retrieved_documents1)

    wrapper =textwrap.TextWrapper(width= 70)

    final_answer1 = wrapper.wrap(output_final1)

    print(final_answer1)

if __name__ == '__main__':
    main()