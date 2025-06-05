import streamlit as st
import os
import cohere
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import CohereEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import Cohere
import tempfile

# Load API key
load_dotenv()
cohere_api_key = os.getenv("COHERE_API_KEY")

st.set_page_config(page_title="📚 BharatBot - Legal Assistant", layout="centered")
st.title("🇮🇳 BharatBot – Ask Any Legal Document")

uploaded_pdf = st.file_uploader("📤 Upload a Legal PDF", type=["pdf"])

query = st.text_input("❓ Ask a question based on the uploaded document")
ask_button = st.button("Ask BharatBot")

if uploaded_pdf:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_pdf.read())
        pdf_path = tmp_file.name

    @st.cache_resource
    def process_pdf(pdf_path):
        loader = PyPDFLoader(pdf_path)
        pages = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=400)
        chunks = text_splitter.split_documents(pages)

        embeddings = CohereEmbeddings(cohere_api_key=cohere_api_key,user_agent='langchain')
        vector_db = FAISS.from_documents(chunks, embeddings)
        return vector_db

    db = process_pdf(pdf_path)
    retriever = db.as_retriever()

    qa_chain = RetrievalQA.from_chain_type(
        llm=Cohere(cohere_api_key=cohere_api_key, model="command-r", temperature=0.3,user_agent='langchain'),
        retriever=retriever,
        return_source_documents=True
    )

    if ask_button and query:
        with st.spinner("🤖 Generating answer..."):
            result = qa_chain(query)
            st.subheader("📘 Answer:")
            st.success(result["result"])

            with st.expander("📄 Source Context"):
                for doc in result["source_documents"]:
                    st.markdown(doc.page_content.strip())

elif ask_button:
    st.warning("Please upload a legal document first.")
