
import streamlit as st

st.title('Echo Bot')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for message in st.session_state.messages:
    # Formatting defaults for containers are loaded depending on the 'speaker'
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input box ':=' checks if prompt is not empty, then assigns it to the variable prompt
if prompt := st.chat_input("Ready for your command..."):
    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt) # Shows the message in a container
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Bot repeats the user input
    response = f"Echo: {prompt}"
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add response to chat history
    st.session_state.messages.append({"role":"assistant", "content":response})
