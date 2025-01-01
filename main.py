import streamlit as st
from langchain_community.llms import Ollama
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
from datetime import datetime
import json
import time

# Enhanced CSS for professional look
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    }
    .chat-message {
        padding: 1.2rem;
        border-radius: 12px;
        margin-bottom: 1.2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border: 1px solid rgba(255,255,255,0.1);
        transition: all 0.3s ease;
    }
    .chat-message:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0,0,0,0.2);
    }
    .human-message {
        background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%);
        margin-left: 20px;
    }
    .bot-message {
        background: linear-gradient(135deg, #16213e 0%, #1a1a2e 100%);
        margin-right: 20px;
    }
    .timestamp {
        color: rgba(255,255,255,0.6);
        font-size: 0.7rem;
        text-align: right;
        margin-top: 5px;
    }
    .confidence-score {
        color: #4CAF50;
        font-size: 0.8rem;
        margin-top: 5px;
    }
    .copy-button {
        float: right;
        padding: 4px 8px;
        background: rgba(255,255,255,0.1);
        border: none;
        border-radius: 4px;
        color: white;
        cursor: pointer;
    }
    .system-status {
        padding: 10px;
        background: rgba(0,0,0,0.2);
        border-radius: 8px;
        margin-bottom: 20px;
    }
    .stButton>button {
        background: linear-gradient(135deg, #3498db 0%, #2c3e50 100%);
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# Custom prompt template to incorporate memory and context
CUSTOM_PROMPT = PromptTemplate(
    input_variables=["history", "input"], 
    template="""Your name is divith. 
Previous conversation:
{history}

Current conversation:
Human: {input}
Assistant:"""
)

def initialize_session_state():
    """Initialize Streamlit session state variables.""" 
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
    
    if 'memory' not in st.session_state:
        st.session_state['memory'] = ConversationBufferMemory(return_messages=True)

def get_llm_response(user_input):
    """Generate response from local Llama model.""" 
    # Initialize Ollama with Llama 3.2 model
    llm = Ollama(model="llama3.2")
    
    # Create conversation chain with memory
    conversation = ConversationChain(
        llm=llm,
        memory=st.session_state['memory'],
        prompt=CUSTOM_PROMPT,
        verbose=True
    )
    
    # Get response
    response = conversation.predict(input=user_input)
    
    return response

def save_chat_history():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"chat_history_{timestamp}.json"
    with open(filename, "w") as f:
        json.dump(st.session_state['chat_history'], f)
    return filename

def main():
    st.header("🤖 Masterpiece of Divith version 25")
    
    # System status
    with st.sidebar:
        st.markdown("### System Information")
        st.markdown('<div class="system-status">', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("*System Status:*")
            st.markdown("*Memory Usage:*")
        with col2:
            st.markdown("🟢 Online")
            st.markdown(f"💾 {len(st.session_state.get('chat_history', []))} messages")
        st.markdown("</div>", unsafe_allow_html=True)
        
        if st.button("💾 Save Chat History"):
            filename = save_chat_history()
            st.success(f"Chat saved to {filename}")
        
        if st.button("🗑 Clear Chat"):
            st.session_state['chat_history'] = []
            st.rerun()

    initialize_session_state()

    # Chat display
    for message in st.session_state['chat_history']:
        with st.chat_message(message["role"]):
            st.markdown(f"""
            <div class="chat-message {'human-message' if message['role']=='human' else 'bot-message'}">
                {message['content']}
                <div class="timestamp">{datetime.now().strftime('%H:%M:%S')}</div>
                <button class="copy-button" onclick="navigator.clipboard.writeText('{message['content']}')">📋</button>
            </div>
            """, unsafe_allow_html=True)

    # Chat input
    if prompt := st.chat_input("Type your message here..."):
        with st.chat_message("human"):
            st.markdown(f"""
            <div class="chat-message human-message">
                {prompt}
                <div class="timestamp">{datetime.now().strftime('%H:%M:%S')}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with st.spinner("🤖 Processing..."):
            try:
                response = get_llm_response(prompt)
                with st.chat_message("assistant"):
                    st.markdown(f"""
                    <div class="chat-message bot-message">
                        {response}
                        <div class="timestamp">{datetime.now().strftime('%H:%M:%S')}</div>
                        <div class="confidence-score">✓ High Confidence</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                st.session_state['chat_history'].extend([
                    {'role': 'human', 'content': prompt},
                    {'role': 'assistant', 'content': response}
                ])
            except Exception as e:
                st.error(f"Error: {str(e)}")

if _name_ == "_main_":
    main()