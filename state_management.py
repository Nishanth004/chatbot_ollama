import streamlit as st
from langchain.memory import ConversationBufferWindowMemory  # Changed from ConversationBufferMemory

def initialize_session_state():
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
    
    if 'memory' not in st.session_state:
        st.session_state['memory'] = ConversationBufferWindowMemory(
            return_messages=True,
            k=3  # Only keep last 3 exchanges for faster processing
        )