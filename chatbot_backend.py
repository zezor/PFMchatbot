# chatbot_backend.py

from openai import OpenAI
from openai import RateLimitError, OpenAIError
import streamlit as st

# Create a client instance
#client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize OpenAI client using the API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def generate_response(user_input):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4"
            messages=[
                {"role": "system", "content": "You are a helpful financial and business advisor."},
                {"role": "user", "content": user_input},
            ]
        )
        return response.choices[0].message.content.strip()

    except RateLimitError:
        return "⚠️ We've hit the API rate or quota limit. Please try again later or check the OpenAI account quota."

    except OpenAIError as e:
        return f"🚫 An unexpected error occurred: {str(e)}"

    except Exception as e:
        return f"❗ An internal error occurred. Please try again later.\n\nError details: {str(e)}"
