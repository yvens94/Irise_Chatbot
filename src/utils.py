import json
import os
from pypdf import PdfReader
import textwrap
from pathlib import Path

#read PDF
def extract_text_pdf(pdfs_folder_path):
    curr_path =os.getcwd()
    pdfs_folder_path= pdfs_folder_path
    pdf_folder=os.path.join(curr_path, pdfs_folder_path)

    if not os.path.exists(pdfs_folder_path):
        print("the specified pdf directory does not exist")
    else:
        files =os.listdir(pdf_folder)

        text=""
        for pdf_name in files:
            pdf_path= os.path.join(pdf_folder, pdf_name)
            if pdf_path.endswith('.pdf'):
                reader_pdf=PdfReader(pdf_path)
                for i in range(len(reader_pdf.pages)):
                    page = reader_pdf.pages[i]
                    data_pdf = page.extract_text()
                    text += data_pdf

    return(text)
                

# pdfs_folder_path = 'data\Raw_data\data_pdfs'






def text_wraper(text):
    wrapper =textwrap.TextWrapper(width=70)
    text2embed=wrapper.wrap(text=text)
    return text2embed



def get_project_root() -> Path:
    return os.path.dirname(os.path.abspath(os.curdir))