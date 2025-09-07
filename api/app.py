from langchain_sambanova import ChatSambaNovaCloud
from langchain_core.prompts import ChatPromptTemplate
from fastapi import FastAPI
from langserve import add_routes
import uvicorn
from langchain_community.llms import Ollama






import os
from dotenv import load_dotenv

load_dotenv()

os.environ["SAMBANOVA_API_KEY"]= os.getenv("SAMBANOVA_API_KEY")


app=FastAPI(
    title="Langchain Server",
    version="1.0",
    discription="A Simple API SERVER"
)

# chain the output of diffrent llm model and provide api

add_routes(
    app, 
    ChatSambaNovaCloud(),
    path="/SambaNovaCloud"
)
model= ChatSambaNovaCloud()
llm=Ollama(model='llama2')

prompt1= ChatPromptTemplate.from_template("write essay about {topic} with 100 word")
prompt2= ChatPromptTemplate.from_template("write poem  on {topic}  for 5 year old kid")

add_routes(
    app,
    prompt1|model,
    path='/essay'
)

add_routes(
    app,
    prompt2|model,
    path='/poem'
)

if __name__=="__main__":
    uvicorn.run(app,host='localhost', port=8000)