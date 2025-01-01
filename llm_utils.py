from langchain_community.llms import Ollama
from langchain.chains import ConversationChain
import streamlit as st
from prompts import CUSTOM_PROMPT

@st.cache_resource
def get_llm():
    return Ollama(
        model="llama2",
        temperature=0.7,
        num_ctx=2048,
        num_thread=4
    )

def clean_response(response):
    """Clean up response by removing prefixes and extra whitespace."""
    prefixes_to_remove = ['AI:', 'Assistant:', 'Divith:']
    for prefix in prefixes_to_remove:
        if response.startswith(prefix):
            response = response[len(prefix):].strip()
    return response.strip()

@st.cache_data(ttl=3600, show_spinner=False)
def get_llm_response(user_input):
    try:
        llm = get_llm()
        conversation = ConversationChain(
            llm=llm,
            memory=st.session_state.get('memory'),
            prompt=CUSTOM_PROMPT,
            verbose=False
        )
        response = conversation.predict(input=user_input)
        return clean_response(response)
    except Exception as e:
        return f"Error: {str(e)}"