import streamlit as st
from datetime import datetime
from styles import get_css
from state_management import initialize_session_state
from chat_utils import get_llm_response
from ui_components import render_sidebar, render_chat_message
from llm_utils import get_llm_response

def main():
    st.markdown(get_css(), unsafe_allow_html=True)
    st.header("🤖 Masterpiece of Divith version 25")
    
    render_sidebar()
    initialize_session_state()

    # Chat display
    for message in st.session_state['chat_history']:
        render_chat_message(message)

    # Chat input
    if prompt := st.chat_input("Type your message here..."):
        render_chat_message({"role": "human", "content": prompt})
        
        with st.spinner("🤖 Thinking..."):  # Changed from Processing to hide debug
            try:
                with st.empty():  # Hide intermediate output
                    response = get_llm_response(prompt)
                render_chat_message({"role": "assistant", "content": response})
                
                st.session_state['chat_history'].extend([
                    {'role': 'human', 'content': prompt},
                    {'role': 'assistant', 'content': response}
                ])
            except Exception as e:
                st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()