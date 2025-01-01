def get_css():
    """Return CSS styling."""
    return """
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
    """