from langchain_sambanova import ChatSambaNovaCloud
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

os.environ["SAMBANOVA_API_KEY"]=os.getenv("SAMBANOVA_API_KEY")

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_KEY"]=os.getenv("LANGCHAIN_KEY")


prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)



st.title('Langchain Demo With OPENAI API')
input_text=st.text_input("Search the topic u want")

# openAI LLm 
llm=ChatSambaNovaCloud(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))