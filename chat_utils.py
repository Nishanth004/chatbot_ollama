from langchain_community.llms import Ollama
from langchain.chains import ConversationChain
import streamlit as st
from datetime import datetime
import json
from prompts import CUSTOM_PROMPT

def get_llm_response(user_input):
    """Generate response from LLM."""
    try:
        llm = Ollama(model="llama2")
        conversation = ConversationChain(
            llm=llm,
            memory=st.session_state['memory'],
            prompt=CUSTOM_PROMPT,
            verbose=False  # Changed to False to remove extra output
        )
        response = conversation.predict(input=user_input)
        # Clean up response format
        if isinstance(response, dict) and 'content' in response:
            return response['content']
        return response.strip()
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return "I apologize, but I encountered an error. Please try again."

def save_chat_history():
    """Save chat history to JSON file."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"chat_history_{timestamp}.json"
    with open(filename, "w") as f:
        json.dump(st.session_state['chat_history'], f)
    return filename