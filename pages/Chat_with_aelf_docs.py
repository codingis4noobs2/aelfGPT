import os
import pymongo
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from llama_index.core import Settings, StorageContext, VectorStoreIndex
from langchain_community.embeddings.edenai import EdenAiEmbeddings
from llama_index.vector_stores.mongodb import MongoDBAtlasVectorSearch

# Load environment variables from a .env file
load_dotenv()

# Set up Streamlit page configuration
st.set_page_config(
    page_title="Chat with Aelf Docs 🤖",
    page_icon="https://cryptologos.cc/logos/aelf-elf-logo.png?v=032",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.sidebar.warning("AelfGPT can make mistakes. Double-check important info.")

# Retrieve environment variables
MONGODB_CONN_URI = os.getenv('MONGODB_CONN_URI')
EDEN_AI_API_KEY = os.getenv('EDEN_AI_API_KEY')
AI_ML_API_KEY = os.getenv("AI_ML_API_KEY")

# MongoDB database and collection configuration
DB_NAME = "aelf_knowledgebase"
COLLECTION_NAME = "docs"

# Initialize MongoDB client and collection
client = pymongo.MongoClient(MONGODB_CONN_URI)
collection = client[DB_NAME][COLLECTION_NAME]

# Field name for storing vector embeddings in MongoDB
VECTOR_DATABASE_FIELD_NAME = 'idx_embedding'

# Set up embedding model
embed_model = EdenAiEmbeddings(
    model="1536__text-embedding-ada-002",
    edenai_api_key=EDEN_AI_API_KEY,
    provider="openai"
)
Settings.embed_model = embed_model

# Set up LLM model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.8,
    max_tokens=8192,
    api_key=AI_ML_API_KEY,
    base_url="https://api.aimlapi.com"
)
Settings.llm = llm

# Set up vector store for MongoDB Atlas
vector_store = MongoDBAtlasVectorSearch(
    mongodb_client=client,
    db_name=DB_NAME,
    collection_name=COLLECTION_NAME,
    vector_index_name=VECTOR_DATABASE_FIELD_NAME
)

# Create storage context with the vector store
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# Create a VectorStoreIndex with the vector store
index = VectorStoreIndex.from_vector_store(
    vector_store=vector_store,
    embed_model=embed_model,
    llm=llm
)

# Initialize chat history in session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Streamlit UI components
st.title("🗣️ Chat with Aelf Docs 🤖")
st.subheader("Your AI-powered assistant for exploring Aelf documentation.")
st.markdown("---")

# Define some example prompts to guide users
example_prompts = [
    "What is Aelf?",
    "How to connect to Aelf using Google Cloud?",
    "Summarize Aelf Whitepaper.",
    "How to install Aelf Python SDK?",
    "Which consensus mechanism does Aelf use?",
    "Explain Aelf architecture in detail.",
    "How to deploy a smart contract on Aelf?",
    "What is the API endpoint to get the height of the current chain?"
]

# Arrange the prompts in a grid layout
num_cols = 3  # Define the number of columns you want
prompts_per_col = len(example_prompts) // num_cols + (len(example_prompts) % num_cols > 0)

# Create columns dynamically based on num_cols
cols = st.columns(num_cols)

# Display the example prompts
for i, prompt in enumerate(example_prompts):
    col_idx = i % num_cols
    with cols[col_idx]:
        if st.button(prompt, key=prompt):
            # Immediately display the selected prompt as the user query
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Show the progress bar while processing the request
            with st.spinner("Processing your request..."):
                response = index.as_query_engine().query(prompt)
                st.session_state.messages.append({"role": "assistant", "content": response.response})

# Chat input for user queries
user_input = st.text_input("Enter your query:", placeholder="Type your question about Aelf here...")
if user_input:
    # Add user input to session state and immediately display it
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Show progress bar while processing the request
    with st.spinner("Processing your query..."):
        response = index.as_query_engine().query(user_input)
        st.session_state.messages.append({"role": "assistant", "content": response.response})

# Display chat messages
for message in st.session_state.messages:
    if message['role'] == 'user':
        st.chat_message("user").write(message['content'])
    elif message['role'] == 'assistant':
        st.chat_message("assistant").write(message['content'])
