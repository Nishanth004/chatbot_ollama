import streamlit as st
from datetime import datetime
from chat_utils import save_chat_history

def render_sidebar():
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
        return show_sidebar_buttons()

def show_sidebar_buttons():
    if st.button("💾 Save Chat History"):
        filename = save_chat_history()
        st.success(f"Chat saved to {filename}")
    
    if st.button("🗑 Clear Chat"):
        st.session_state['chat_history'] = []
        st.rerun()

def render_chat_message(message):
    """Render a single chat message."""
    with st.chat_message(message["role"]):
        # Clean up message content
        content = message["content"]
        if isinstance(content, dict) and 'content' in content:
            content = content['content']
        
        st.markdown(f"""
        <div class="chat-message {'human-message' if message['role']=='human' else 'bot-message'}">
            {content.strip()}
            <div class="timestamp">{datetime.now().strftime('%H:%M:%S')}</div>
        </div>
        """, unsafe_allow_html=True)