from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
import os
from dotenv import load_dotenv
from llama_index.llms.groq import Groq
import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from llama_index.core import Settings

load_dotenv()





class GroqAgent():
    def __init__(self):
        self.HF_TOKEN = os.getenv('HF_TOKEN')
        self.GROQ = os.getenv('GROQ')
        self.embeddings = HuggingFaceInferenceAPIEmbeddings(
                            api_key=self.HF_TOKEN, model_name="BAAI/bge-large-en-v1.5"
                            )
        Settings.embed_model = self.embeddings

        self.reasoning_model_name = "llama-3.1-405b-reasoning"
        self.reasoning_model = Groq(model=self.reasoning_model_name, api_key=self.GROQ)

        self.moe_model_name = "Mixtral-8x7b-Instruct-v0.1"
        self.moe_model = Groq(model=self.moe_model_name, api_key=self.GROQ)