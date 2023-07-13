import os
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.chains import SequentialChain
import streamlit as st

from constants import  openai_key

# Setup OpenAI API key
os.environ["OPENAI_API_KEY"]=openai_key

# User Input
st.title('Public figure Search Results')
input_text=st.text_input("Search the public figure u want to know")












