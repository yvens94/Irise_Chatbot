import os
import openai
from openai import OpenAI
import textwrap

wrapper= textwrap.TextWrapper(width=70)

from dotenv import load_dotenv, find_dotenv
_=load_dotenv(find_dotenv())
openai.api_key = os.environ['OPENAI_API_KEY']
openai_client = OpenAI()


def query_expansor(query, model="gpt-3.5-turbo"):
    messages =[
        {
            "role":"system",
            "content": "You are a helpful expert customer service assistant at interfaithrise which an agency that help with refugee and immigrant resettlement, Provide an example answer to the given question,that might be found in the documentation of an agency like that."
            " only answer question related to interfaithrise, and our services"
            "keep your answer to 2 phrases"
        },
        {"role":"user","content":query}
    ]
    response =openai_client.chat.completions.create(
        model=model,
        messages= messages
    )

    content=response.choices[0].message.content

    return content



def query_jointer(query, augment_query):
    return f"{query} {augment_query}"


def augment_multiple_query(query, model ="gpt-3.5-turbo"):
    messages =[
        {
            "role": "system",
            "content": (
                "you are a helpful customer service ervice assistant at interfaithrise which an agency that help with refugee and immigrant resettlement"
            "Suggest up to 2 additional related questions to help them find the information they need, for the provided question. "
            "Suggest only short questions without compound sentences. Suggest a variety of questions that cover different aspects of the topic."
            "Make sure they are complete questions, and that they are related to the original question."
            "Output one question per line. Do not number the questions."
            )
        },
        {"role": "user", "content": query}
    ]

    response = openai_client.chat.completions.create(
        model=model,
        messages=messages
    )
    content = response.choices[0].message.content
    content = content.split("\n")
    return content


def list_2_string(list):
    return ' '.join(str(item) for item in list)






original_query= str(input('Ask a question to David: '))

augmented_queries = augment_multiple_query(original_query)

augmented_queries=list_2_string(augmented_queries)

expanded_query = query_expansor(augmented_queries)

joint_query = query_jointer(original_query, expanded_query)

final_query= wrapper.wrap(joint_query)


print(original_query)

print('--'*100)
print(augmented_queries)
print('--'*100)
print(expanded_query)
print('--'*100)
print(joint_query)
print('--'*100)
print(final_query)






