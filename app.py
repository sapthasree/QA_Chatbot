import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="Ask Your PDF - Gemini", layout="centered")
st.title("Ask Your PDF Anything! (Gemini Free API)")

file = st.file_uploader("Upload a PDF file", type="pdf")
qn = st.text_input("Ask a Question about your Document")

if file and qn:
    with open("temp.pdf", "wb") as f:
        f.write(file.read())

    loader = PyPDFLoader("temp.pdf")
    pages = loader.load()

    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.split_documents(pages)

    # Use Gemini embedding model
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    db = FAISS.from_documents(docs, embeddings)

    # Use Gemini-1.5 chat model for free API
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())

    ans = qa.run(qn)

    st.subheader("Answer")
    st.write(ans)
