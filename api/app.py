from langchain_sambanova import ChatSambaNovaCloud
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["SAMBANOVA_API_KEY"]= os.getenv("SAMBANOVA_API_KEY")

os.environ["LANGCHAIN_KEY"]= os.getenv("LANGCHAIN_KEY")

os.environ["LANGCHAIN_TRACING_V2"]="true"


prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are helpful assistant. Please provide response to user query"),
        ("user","Question:{question}")
    ]
)


st.title("Langchain Demo for Q&A")
input_text=st.text_input("Searh the topic you want")

llm =ChatSambaNovaCloud(model="DeepSeek-V3-0324")
output_parser=StrOutputParser()

chain=prompt|llm|output_parser
if input_text:
    st.write(chain.invoke({'question':input_text}))