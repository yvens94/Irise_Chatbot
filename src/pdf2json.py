import json
import os
from pypdf import PdfReader
from irisewebScrapping import path_json_dir


#read PDF
def extract_text_pdf(pdfs_folder_path):
    curr_path =os.getcwd()
    pdfs_folder_path= pdfs_folder_path
    pdf_folder=os.path.join(curr_path, pdfs_folder_path)

    if not os.path.exists(pdfs_folder_path):
        print("the specified pdf directory does not exist")
    else:
        files =os.listdir(pdf_folder)

        
        for pdf_name in files:
            pdf_path= os.path.join(pdf_folder, pdf_name)
            if pdf_path.endswith('.pdf'):
                reader_pdf=PdfReader(pdf_path)
                text=""
                for i in range(len(reader_pdf.pages)):
                    page = reader_pdf.pages[i]
                    data_pdf = page.extract_text()
                    text += data_pdf

                filepath=os.path.join(path_json_dir, f'{pdf_name}.json')
                print(f"\nScraping:{pdf_name}\n{'-'*40}")
                textscraped ={

                    "title":pdf_name,
                    "url":pdf_name,
                    "body": text
                    
                    }

                with open(filepath, 'w', encoding='utf-8') as json_file:
                    json.dump(textscraped, json_file,ensure_ascii=False, indent=4)

            

