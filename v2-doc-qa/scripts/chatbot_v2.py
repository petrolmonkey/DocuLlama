
import streamlit as st
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

# Streamlit decorator caches the return value of a function that produces a global 
# resource, such as a database connection or a machine learning model. Prevents the 
# resource from being re-created on every app rerun, making the app more performant. 

@st.cache_resource

# Load and cache the index
def load_index():
    documents = SimpleDirectoryReader("./manuals").load_data()
    index = VectorStoreIndex.from_documents(documents)
    return index.as_query_engine(similarity_top_k=5)

query_engine = load_index()

# Streamlit Chat
st.title('Instruction Manuals and Reference')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# User input captured: The chatbot interface captures the user's question
if prompt := st.chat_input('Enter your question...'):
    st.session_state.messages.append({'role':'user', 'content':prompt})
    with st.chat_message('user'):
        st.markdown(prompt)
    
    # Response generated: The LLM synthesizes an answer using the retrieved context
    response = query_engine.query(prompt)
    
    st.session_state.messages.append({'role':'assistant','content':str(response)})   
    # Response displayed: The chatbot displays the response to the user
    with st.chat_message('assistant'):
        st.markdown(str(response))
        
