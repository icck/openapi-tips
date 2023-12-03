import os

import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

load_dotenv()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


st.title("Hello World")

prompt = st.chat_input("what is up?")

if prompt:
    # add message to session state
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        chat = ChatOpenAI(
            model_name=os.environ.get("OPENAI_API_MODEL"),
            api_key=os.environ.get("OPENAI_API_KEY"),
            temperature=os.environ.get("OPENAPI_API_TEMPERATURE"),
        )
        messages = [HumanMessage(content=prompt)]

        response = chat(messages)
        st.markdown(response.content)

    # add response to session state
    st.session_state.messages.append({"role": "assistant", "content": response.content})
