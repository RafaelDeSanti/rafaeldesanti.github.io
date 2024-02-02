import streamlit as st
    

if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
if sendInput := st.chat_input("write here..."):
    # Display user message in chat message container
    st.chat_message("user").markdown(sendInput)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": sendInput})
