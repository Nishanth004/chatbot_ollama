from langchain.prompts import PromptTemplate
import streamlit as st

@st.cache_data
def get_prompt_template():
    return PromptTemplate(
        input_variables=["history", "input"],
        template="""You are Divith, an AI assistant. Be concise and direct. Do not prefix your responses.
Last context: {history}
Human: {input}
Assistant:"""
    )

CUSTOM_PROMPT = get_prompt_template()