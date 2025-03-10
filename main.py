# import os
# from dotenv import dotenv_values
# import streamlit as st
# import streamlit.components.v1 as components
# from groq import Groq

# st.set_page_config(
#     page_title="KILLSWITCH",
#     page_icon="🤖",
#     layout="centered",
# )

# def parse_groq_stream(stream):
#     for chunk in stream:
#         if chunk.choices and chunk.choices[0].delta.content is not None:
#             yield chunk.choices[0].delta.content

# # Load CSS
# with open("main.css") as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# # -- Load secrets or .env
# try:
#     secrets = dotenv_values(".env")  # for dev env
#     GROQ_API_KEY = secrets["GROQ_API_KEY"]
# except:
#     secrets = st.secrets  # for Streamlit deployment
#     GROQ_API_KEY = secrets["GROQ_API_KEY"]

# os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# INITIAL_RESPONSE = secrets["INITIAL_RESPONSE"]
# INITIAL_MSG = secrets["INITIAL_MSG"]
# CHAT_CONTEXT = secrets["CHAT_CONTEXT"]

# client = Groq()

# # Session state to track game state
# if "game_started" not in st.session_state:
#     st.session_state.game_started = False

# # Function to handle the start button click
# def start_game():
#     st.session_state.game_started = True

# # Welcome page with React component
# if not st.session_state.game_started:
#     # Embed your React welcome component
#     components.html(
#         """
#         <div id="root"></div>
#         <script src="build/bundle.js"></script>
#         """,
#         height=600,
#     )
    
#     # This will be triggered by JavaScript
#     if st.button("Start Game", key="start_button"):
#         start_game()
# else:
#     # Main game/chat UI after start button is clicked
#     st.title("Hey Buddy!")
#     st.caption("Who is the killer?...")

#     # Initialize chat history
#     if "chat_history" not in st.session_state:
#         st.session_state.chat_history = [
#             {"role": "assistant", "content": INITIAL_RESPONSE},
#         ]

#     # Display chat history
#     for message in st.session_state.chat_history:
#         with st.chat_message(message["role"], avatar='🤖' if message["role"] == "assistant" else "🗨️"):
#             st.markdown(message["content"])

#     # User input field
#     user_prompt = st.chat_input("Ask me")

#     if user_prompt:
#         with st.chat_message("user", avatar="🗨️"):
#             st.markdown(user_prompt)
#         st.session_state.chat_history.append({"role": "user", "content": user_prompt})

#         messages = [
#             {"role": "system", "content": CHAT_CONTEXT},
#             {"role": "assistant", "content": INITIAL_MSG},
#             *st.session_state.chat_history
#         ]

#         with st.chat_message("assistant", avatar='🤖'):
#             stream = client.chat.completions.create(
#                 model="llama-3.1-8b-instant",
#                 messages=messages,
#                 stream=True
#             )
#             response = st.write_stream(parse_groq_stream(stream))

#             st.session_state.chat_history.append({"role": "assistant", "content": response})

import os
from dotenv import dotenv_values
import streamlit as st
import streamlit.components.v1 as components
from groq import Groq

st.set_page_config(
    page_title="KILLSWITCH",
    page_icon="🤖",
    layout="centered",
)

def parse_groq_stream(stream):
    for chunk in stream:
        if chunk.choices and chunk.choices[0].delta.content is not None:
            yield chunk.choices[0].delta.content

# Load secrets
try:
    secrets = dotenv_values(".env")  # for dev env
    GROQ_API_KEY = secrets["GROQ_API_KEY"]
except:
    secrets = st.secrets  # for Streamlit deployment
    GROQ_API_KEY = secrets["GROQ_API_KEY"]
os.environ["GROQ_API_KEY"] = GROQ_API_KEY
INITIAL_RESPONSE = secrets["INITIAL_RESPONSE"]
INITIAL_MSG = secrets["INITIAL_MSG"]
CHAT_CONTEXT = secrets["CHAT_CONTEXT"]
client = Groq()

# Session state to track game state
if "game_started" not in st.session_state:
    st.session_state.game_started = False

# Function to handle the start button click
def start_game():
    st.session_state.game_started = True
    st.experimental_rerun()

# Welcome page or game page based on state
if not st.session_state.game_started:
    # Create a button that will be visible and work as fallback
    if st.button("START GAME", key="start_button", on_click=start_game):
        pass
    
    # Get the absolute path to your build directory
    build_dir = os.path.abspath("build")
    
    # Display the welcome screen
    st.markdown(f"""
    <iframe src="build/index.html" width="100%" height="600px" frameborder="0"></iframe>
    
    <script>
    // Listen for messages from the iframe
    window.addEventListener('message', function(event) {{
        if (event.data === 'start') {{
            document.querySelector('button[data-testid="baseButton-secondary"]').click();
        }}
    }});
    </script>
    """, unsafe_allow_html=True)
    
    # For debugging, show the path
    st.write(f"Build directory: {build_dir}")
    
    # Check if the build directory exists
    if os.path.exists(build_dir):
        st.write("✅ Build directory exists")
        
        # Check if bundle.js exists
        if os.path.exists(os.path.join(build_dir, "bundle.js")):
            st.write("✅ bundle.js exists")
        else:
            st.error("❌ bundle.js not found")
            
        # Check if index.html exists
        if os.path.exists(os.path.join(build_dir, "index.html")):
            st.write("✅ index.html exists")
        else:
            st.error("❌ index.html not found")
    else:
        st.error(f"❌ Build directory not found at {build_dir}")
else:
    # Main game/chat UI after start button is clicked
    st.title("Hey Buddy!")
    st.caption("Who is the killer?...")
    
    # -- Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            {"role": "assistant", "content": INITIAL_RESPONSE},
        ]
    
    # -- Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"], avatar='🤖' if message["role"] == "assistant" else "🗨"):
            st.markdown(message["content"])
    
    # -- User input field
    user_prompt = st.chat_input("Ask me")
    if user_prompt:
        with st.chat_message("user", avatar="🗨"):
            st.markdown(user_prompt)
        st.session_state.chat_history.append({"role": "user", "content": user_prompt})
        
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
            
            st.session_state.chat_history.append({"role": "assistant", "content": response})