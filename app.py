# app.py

import streamlit as st
from chatbot_backend import generate_response

st.set_page_config(page_title="PFM_App", layout="centered")
st.title("Finance Buddy", layout="centered")

st.title("💰 Your Accounting & Finance Buddy")
st.write("Ask me anything about budgeting, savings, investments, business finance...")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", "")

if st.button("Send") and user_input:
    response = generate_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

for sender, message in st.session_state.chat_history[::-1]:
    st.markdown(f"**{sender}:** {message}")
