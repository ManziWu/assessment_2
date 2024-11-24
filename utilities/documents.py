import streamlit as st
import os
import PyPDF2
import io
import docx2txt

# Define a function to read content from different types of documents
def read_document(file):
    if file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page].extract_text()
        return text
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return docx2txt.process(file)
    else:
        return "Unsupported file type. Please upload a PDF or DOCX file."