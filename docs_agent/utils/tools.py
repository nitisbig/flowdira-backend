import os
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
load_dotenv()
embeddings = GoogleGenerativeAIEmbeddings(google_api_key=os.getenv('GEMINI_API_KEY'), model='gemini-embedding-001')


def load_web(url: str) ->str:
    loader = WebBaseLoader(url)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
    )
    chunks =  text_splitter.split_documents(documents)
    vector_store = FAISS.from_documents(chunks, embeddings)
    return vector_store





load_web('https://docs.langchain.com/oss/python/langgraph/application-structure#python-requirements-txt')