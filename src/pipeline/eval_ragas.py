from datasets import Dataset
import sys
import os

import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from logger import logging
from RAG_pipeline import rag, retriever
from components.data_preprocessor import chroma_client
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_recall,
    context_precision,
)

questions = [

    "What are the services you offer?",
    "what services are offered by the employment team?",
    'why wait befor applying for cash assistance?'
]


ground_truth =[
    'Long-term case management, Health and medical interventions,Mental health interventions,Social adjustment services',
    'resume writing, job searching,  job application assistance, job readiness workshops, interview preparation classes, job orientation, information about childcare & public transportation',
    ' since I-RISE offers two forms of assistance and we want to assure the client chooses the best option. If they receive GA or TANF (cash assistance) they won’t be eligible for our cash assistance programs.']


answers =[]

contexts = []

#inference

for qry in questions:
    retrieved_documents_eval = [retriever(chroma_client, qry)]
    output_final_eval= rag(qry, retrieved_documents_eval)
    answers.append(output_final_eval)
    contexts.append(retrieved_documents_eval)

print(contexts)

# To dict
data = {
    "question": questions,
    "answer": answers,
    "contexts": contexts,
    "ground_truth": ground_truth
}

#Convert dict to dataset
dataset = Dataset.from_dict(data)


print(dataset)


logging.info('evaluation started')
result = evaluate(
    dataset, 
    metrics=[
        context_precision,
        context_recall,
        faithfulness,
        answer_relevancy,
    ]
)

df = result.to_pandas()

print(df.head())

df.to_csv('eval_result')