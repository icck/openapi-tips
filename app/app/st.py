import streamlit as st

st.title("Hello World")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


prompt = st.chat_input("what is up?")

if prompt:
    # add message to session state
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        response = "hello!!"
        st.markdown(response)

    # add response to session state
    st.session_state.messages.append({"role": "assistant", "content": response})
