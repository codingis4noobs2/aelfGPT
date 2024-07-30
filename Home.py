import streamlit as st

st.set_page_config(
    page_title="Home Page",
    page_icon="https://cryptologos.cc/logos/aelf-elf-logo.png?v=032",
)

st.write("# Welcome to AelfGPT! 👋 ~Hosted on GCP")
st.write("Explore the capabilities of AelfGPT to interact with the Aelf blockchain, chat with Aelf documentation, and debug or generate smart contracts.")

# Add a section for each functionality
st.write("## What Can You Do Here?")

# Chat with Aelf Docs
st.write("### 💬 Chat with Aelf Docs")
st.write("Have questions about Aelf? Chat with our AI assistant to get detailed explanations, summaries, and guidance on various Aelf-related topics.")
st.write("[Go to Chat with Aelf Docs](/Chat_with_aelf_docs)")

# Smart Contract Debugging and Generation
st.write("### 🛠️ Smart Contract Debugging & Generation")
st.write("Paste your .cs smart contract code to debug or generate enhanced versions. Our AI will help you identify issues and suggest improvements.")
st.write("[Go to Smart Contract Debugger](/AI_assisted_smart_contract_debugger)")

# Blockchain Exploring
st.write("### 🌐 Blockchain Exploring")
st.write("Explore the Aelf blockchain with AI assistance. Get real-time insights, check the status of the blockchain, retrieve block information, and more.")
st.write("[Go to Blockchain Explorer](/AI_assisted_block_explorer)")

# Interactive Elements
st.write("## Get Started!")
st.write("Choose a section above to start exploring, chatting, or working with smart contracts.")

st.image("https://cryptologos.cc/logos/aelf-elf-logo.png?v=032", width=150)

st.write("## Need Help?")
st.write("If you have any questions or need assistance, feel free to reach out to my [Github](https://github.com/codingis4noobs2/) and create a Issue.")
