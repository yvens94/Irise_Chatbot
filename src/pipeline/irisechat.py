import streamlit as st
import textwrap
import os
import sys
from dotenv import load_dotenv, find_dotenv

# Add src to the system path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from rag_pipeline import rag, retriever
from components import query_preprocessor
from components.data_preprocessor import chroma_client

# Load environment variables if needed
load_dotenv(find_dotenv())

# Streamlit app
st.header("IriseChat 1.0")
st.subheader(
    "Irise chat can answer questions about our services and other areas. "
    "You can ask questions in Haitian Creole, English, or Spanish."
)

st.text("")
st.chat_message("user").write("Hello, Bonjou, Hola 👋\nHow can I help? Komanm ka ede? Como puedo ayudar?")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Main app function
def main():
    user_message = st.chat_input("Type your question here...")

    if user_message:
        # Add the user's message to the chat history
        st.session_state.messages.append({"role": "user", "content": user_message})

        # Display the user's message
        with st.chat_message("user"):
            st.write(user_message)

        # Process the user's message
        with st.spinner("Processing your question..."):
            query = query_preprocessor.query_prepo(original_query=user_message)
            retrieved_documents = retriever(chroma_client, query)
            output_final = rag(query, retrieved_documents)

            # Format the output
            wrapper = textwrap.TextWrapper(width=70)
            final_answer = "\n".join(wrapper.wrap(output_final))

        # Add the AI's response to the chat history
        st.session_state.messages.append({"role": "assistant", "content": final_answer})

        # Display the AI's response
        with st.chat_message("assistant"):
            st.write(final_answer)

    # Display the chat history
    for message in st.session_state.messages:
        role = message["role"]
        content = message["content"]
        with st.chat_message(role):
            st.write(content)

if __name__ == "__main__":
    main()
