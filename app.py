import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth
import os
from dotenv import load_dotenv
import streamlit.components.v1 as components

# Load environment variables
load_dotenv()

# Initialize Firebase
if not firebase_admin._apps: 
    cred = credentials.Certificate("chatbot-a42f1-firebase-adminsdk-fbsvc-e3459041d6.json")  # Use your Firebase JSON file
    firebase_admin.initialize_app(cred)

# Custom styling for better UI
st.set_page_config(page_title="Secure Pritam's Chatbot ", page_icon="💬", layout="wide")
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f7fb;
        }
        .login-container {
            background-color: #ffffff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-top: 40px;
        }
        .chatbot-container {
            background-color: #ffffff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-top: 40px;
        }
        .footer {
            text-align: center;
            font-size: 12px;
            color: #777;
            padding-top: 20px;
        }
        .button-container {
            display: flex;
            justify-content: center;
        }
    </style>
""", unsafe_allow_html=True)

# Title and header
st.title("🔐 Secure Pritam's Chatbot")
st.markdown("""
    Welcome to the Pritam's Chatbot!  
    "Hi there! Let's chat and get to know more about anything. Feel free to ask me anything!"
""")

# User Authentication Section
if "user" not in st.session_state:
    st.session_state.user = None

# Function for Login
def login():
    st.subheader("Login to your account")
    with st.form("login_form", clear_on_submit=True):
        email = st.text_input("📧 Email")
        password = st.text_input("🔑 Password", type="password")
        submit_button = st.form_submit_button("Login")
        
        if submit_button:
            try:
                user = auth.get_user_by_email(email)
                st.session_state.user = user.email
                st.success(f"✅ Logged in as {user.email}")
                st.rerun()  # Trigger a rerun to display the chatbot
            except Exception:
                st.error("❌ Invalid credentials or user not found.")

# Function for Registration
def register():
    st.subheader("Create a new account")
    with st.form("register_form", clear_on_submit=True):
        email = st.text_input("📧 Email")
        password = st.text_input("🔑 Password", type="password")
        submit_button = st.form_submit_button("Register")
        
        if submit_button:
            try:
                user = auth.create_user(email=email, password=password)
                st.success("✅ Registration successful! Please login.")
            except Exception:
                st.error("❌ Error: User may already exist.")

# Main App Logic
if st.session_state.user:
    st.sidebar.success(f"👋 Welcome, {st.session_state.user}")

    # Display the iframe for the chatbot
    st.subheader("Chat with PRITAM'S BOT")
    
    # Chatbot Iframe
    chatbot_url = "https://copilotstudio.microsoft.com/environments/Default-06943ac0-3679-4445-9507-60447807fa0d/bots/cre42_chatBotPritam/webchat?__version__=2"
    components.iframe(chatbot_url, width=800, height=600)

    #  Thank You section
    st.markdown("""
        <div style="text-align:center; margin-top: 20px;">
            <button onclick="window.location.reload();" style="padding: 10px 20px; font-size: 16px; background-color: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer;">
                Thank You from ChatBot!!
            </button>
        </div>
    """, unsafe_allow_html=True)

    # Go back to login screen
    if st.button("Back to Login/Signup"):
        st.session_state.user = None
        st.rerun()  # Trigger rerun to go back to login/signup screen

else:
    # Display Login or Register options 
    option = st.radio("Choose an option:", ["Login", "Register"], horizontal=True)

    if option == "Login":
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        login()
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        register()
        st.markdown('</div>', unsafe_allow_html=True)

# Footer Section
st.markdown("""
    <div class="footer">
        Made by Pritam
    </div>
""", unsafe_allow_html=True)
