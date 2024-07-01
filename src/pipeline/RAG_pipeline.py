import sys
import os
import openai
from openai import OpenAI

from dotenv import load_dotenv, find_dotenv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from components.query_preprocessor import final_query
from components.data_preprocessor import chroma_client
import textwrap

wrapper =textwrap.TextWrapper(width= 70)




_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

openai_client = OpenAI()

def list_2_string(list):
    return ' '.join(str(item) for item in list)


def retriever(client, query):
    chroma_collection= client.get_collection(name = "interfaithrise_info")
    results =chroma_collection.query(query_texts = [query], n_results = 4)

    retrieved_documents = list_2_string(results['documents'])
    return retrieved_documents




def rag(query, retrieved_documents, model ="gpt-3.5-turbo"):

    information = "\n\n".join(retrieved_documents)

    messages = [
        {
            "role": "system",
            "content": "You are a  customer service expert in social service at interfaithrise. Your users are asking questions about information contained in interfaithrise_info"
            "You will be shown the user's question, and the relevant information from the interfaithrise_info. Answer the user's question using only this information. Interfaithrise is sometime referred to as Irise"
            "any question with (you), is actually referring to interfaithrise"
            "be clear and simple answers, translate answer in the language they were asked, english, spanish, haitian creole, or ukrainian"
            "information in interfaithrise_info generally comes with a link, if it is there always provided it a way to find more information"
            " only answer question related to interfaithrise, and our services"
        },
        {"role": "user", "content": f"Question: {query}. \n Information: {information}"}
    ]
    
    response = openai_client.chat.completions.create(
        model=model,
        messages=messages,
    )
    content = response.choices[0].message.content
    return content




if __name__ == '__main__':

    client=chroma_client
    query =final_query

    retrieved_documents = retriever(query, client)

    output_final= rag(query, retrieved_documents)

    final_answer = wrapper.wrap(output_final)

    print(final_answer)