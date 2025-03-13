import os
from dotenv import dotenv_values
import streamlit as st
from groq import Groq

def parse_groq_stream(stream):
    for chunk in stream:
        if chunk.choices:
            if chunk.choices[0].delta.content is not None:
                yield chunk.choices[0].delta.content

st.set_page_config(
    page_title="Hot Bot",
    page_icon="🤖",
    layout="centered",
)

# 1. Insert your GIF at the top
st.image("C:\Users\jasle\OneDrive - Simon Fraser University (1sfu)\HotBot\hotbot\Lottie Lego.webm", use_column_width=True)

# 2. Add vertical spacing
st.write("")  
st.write("")  # Each st.write("") adds a line of spacing
# Or you can do: st.markdown("<br><br>", unsafe_allow_html=True)

# For local dev
try:
    secrets = dotenv_values(".env")  
    GROQ_API_KEY = secrets["GROQ_API_KEY"]
except:
    secrets = st.secrets  # For Streamlit deployment
    GROQ_API_KEY = secrets["GROQ_API_KEY"]

os.environ["GROQ_API_KEY"] = GROQ_API_KEY

INITIAL_RESPONSE = secrets["INITIAL_RESPONSE"]
INITIAL_MSG = secrets["INITIAL_MSG"]
CHAT_CONTEXT = secrets["CHAT_CONTEXT"]

client = Groq()

# 3. Page title, caption, etc.
st.title("Hey Buddy!")
st.caption("Who is the killer?...")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "content": INITIAL_RESPONSE},
    ]

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"], avatar='🤖'):
        st.markdown(message["content"])

# User input field
user_prompt = st.chat_input("Ask me")

if user_prompt:
    with st.chat_message("user", avatar="🗨️"):
        st.markdown(user_prompt)
    st.session_state.chat_history.append(
        {"role": "user", "content": user_prompt}
    )

    messages = [
        {"role": "system", "content": CHAT_CONTEXT},
        {"role": "assistant", "content": INITIAL_MSG},
        *st.session_state.chat_history
    ]

    with st.chat_message("assistant", avatar='🤖'):
        stream = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            stream=True
        )
        response = st.write_stream(parse_groq_stream(stream))

    st.session_state.chat_history.append(
        {"role": "assistant", "content": response}
    )
