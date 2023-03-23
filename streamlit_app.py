#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from langchain import OpenAI
from gpt_index import SimpleDirectoryReader, GPTListIndex, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
import openai
import sys
import streamlit as st
import os


# In[ ]:


os.environ["OPENAI_API_KEY"] = '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'


# In[ ]:


st.set_page_config(layout='wide', initial_sidebar_state='expanded')
#st.sidebar.header('Training Bot')
st.header("Welcome to Medical Domain World")


# In[ ]:


import streamlit as st
_emp = st.empty()
text = _emp.text_input("Enter Something here! ")
if text:
    index = GPTSimpleVectorIndex.load_from_disk('D://Trainingbot//Domainbot//index.json')
    response = index.query(text, response_mode="compact")
    st.write(response.response)

