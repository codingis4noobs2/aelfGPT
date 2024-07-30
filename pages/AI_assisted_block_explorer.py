import os
from dotenv import load_dotenv
import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI


# Load environment variables from a .env file
load_dotenv()
AI_ML_API_KEY = os.getenv("AI_ML_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Set up Streamlit page configuration
st.set_page_config(
    page_title="AI-Assisted Blockchain Explorer 🧑‍💻",
    page_icon="https://cryptologos.cc/logos/aelf-elf-logo.png?v=032",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.sidebar.warning("AelfGPT can make mistakes. Double-check important info.")
st.sidebar.write("Supported Network URLs:")
st.sidebar.write("Mainnet: [https://aelf-public-node.aelf.io/](https://aelf-public-node.aelf.io/)")
st.sidebar.write("Testnet: [https://aelf-test-node.aelf.io](https://aelf-test-node.aelf.io)")

template = """
__ASK__
Given a query, strictly generate the required code for the task as per the requirement.
If not, you should respond that you are not able to generate the required code for the task. But if the out-of-context query is a greeting or farewell respond to the greeting.

__CONTEXT__
Url for mainnet: https://aelf-public-node.aelf.io/
Url for testnet: https://aelf-test-node.aelf.io
get_chain_status: 
Get the current status of the block chain.
Web API path:
/api/blockChain/chainStatus

Parameters:
Empty

Returns:
json
ChainId - String
Branches - json
NotLinkedBlocks - json
LongestChainHeight - Number
LongestChainHash - String
GenesisBlockHash - String
GenesisContractAddress - String
LastIrreversibleBlockHash - String
LastIrreversibleBlockHeight - Number
BestChainHash - String
BestChainHeight - Number

Example:
from aelf import AElf
aelf = AElf(url)
chain_status = aelf.get_chain_status()
print('# get_chain_status', chain_status)
---
get_block_height:
Get current best height of the chain.

Web API path:
/api/blockChain/blockHeight

Parameters:
Empty

Returns:
Number

Example:
from aelf import AElf
aelf = AElf(url)
block_height = aelf.get_block_height()
print('# get_block_height', block_height)
---
get_block:
Get block information by block hash.

Web API path:
/api/blockChain/block

Parameters:
block_hash - String
include_transactions - Boolean :
true require transaction ids list in the block
false Doesn’t require transaction ids list in the block

Returns:
json
BlockHash - String
Header - json
PreviousBlockHash - String
MerkleTreeRootOfTransactions - String
MerkleTreeRootOfWorldState - String
Extra - List
Height - Number
Time - json
ChainId - String
Bloom - String
SignerPubkey - String
Body - json
TransactionsCount - Number
Transactions - List
transactionId - String

Example:
from aelf import AElf
aelf = AElf(url)
block = aelf.get_block(blockHash)
print('# get_block', block)
---

get_block_by_height:
Web API path:
/api/blockChain/blockByHeight
Get block information by block height.

Parameters:
block_height - Number
include_transactions - Boolean :
true require transaction ids list in the block
false Doesn’t require transaction ids list in the block

Returns:
json
BlockHash - String
Header - json
PreviousBlockHash - String
MerkleTreeRootOfTransactions - String
MerkleTreeRootOfWorldState - String
Extra - List
Height - Number
Time - json
ChainId - String
Bloom - String
SignerPubkey - String
Body - json
TransactionsCount - Number
Transactions - List
transactionId - String

Example:
from aelf import AElf
aelf = AElf(url)
block_by_height = aelf.get_block_by_height(12, false)
print('# get_block_by_height', block_by_height)
---
get_transaction_result:
Get the result of a transaction

Web API path:
/api/blockChain/transactionResult

Parameters:
transactionId - String

Returns:
json
TransactionId - String
Status - String
Logs - List
Address - String
Name - String
Indexed - List
NonIndexed - String
Bloom - String
BlockNumber - Number
Transaction - List
From - String
To - String
RefBlockNumber - Number
RefBlockPrefix - String
MethodName - String
Params - json
Signature - String
ReadableReturnValue - json
Error - String

Example:
from aelf import AElf
aelf = AElf(url)
transaction_result = aelf.get_transaction_result(transactionId)
print('# get_transaction_results', transaction_result)
---
get_transaction_results:
Get multiple transaction results in a block

Web API path:
/api/blockChain/transactionResults

Parameters:
blockHash - String
offset - Number
limit - Number

Returns:
List - The array of method descriptions:
the transaction result object

Example:
from aelf import AElf
aelf = AElf(url)
transaction_results = aelf.get_transaction_results(blockHash, 0, 2)
print('# get_transaction_results', transaction_results)
---
get_transaction_pool_status:
Get the transaction pool status.

Web API path:
/api/blockChain/transactionPoolStatus

Example:
from aelf import AElf
aelf = AElf(url)
tx_pool_status = aelf.get_transaction_pool_status()
print('# get_transaction_pool_status', tx_pool_status)
---

__CONSTRAINTS__
Do not output anything other than python code, but it should be indented.
Do not use formatting using backticks, output as plain text.
If the query is not related to Aelf or Aelf Explorer, simply deny.
If you have not mentioned mainnet/testnet, ask them to reprompt with the network name.
If there are any parameters required, and if user has not provided them reprompt.

query: {query}
"""

prompt_template = PromptTemplate.from_template(template=template)

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.8,
    max_tokens=8192,
    api_key=AI_ML_API_KEY,
    base_url="https://api.aimlapi.com"
)

gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=GOOGLE_API_KEY,
)

chain = ({"query": RunnablePassthrough()}
         | prompt_template
         | llm
         | StrOutputParser()
         )

def run_code(code):
    try:
        # Capture the output of the exec code
        from io import StringIO
        import sys

        old_stdout = sys.stdout
        sys.stdout = StringIO()

        exec(code, globals())

        output = sys.stdout.getvalue()
        sys.stdout = old_stdout

        return output
    except Exception as e:
        return f"Error executing code: {e}"

def main():

    st.sidebar.subheader("Supported Tasks")
    supported_tasks = [
        "Get the current status of the blockchain",
        "Get current best height of the chain",
        "Get block information by block hash",
        "Get block information by block height",
        "Get the result of a transaction",
        "Get multiple transaction results in a block",
        "Get the transaction pool status"
    ]
    st.sidebar.write(supported_tasks)
    # Streamlit UI components
    st.title("Aelf Assistant 🤖")
    st.subheader("Chat with Aelf Explorer, Powered by GPT-4o and Gemini, Hosted on GCP")
    st.write("Sample Query:")
    st.code("What is the Status of the transaction? transaction hash: 5991909d5f752204f00d7837a622022dbf49dd26abe0e60513b3b125ee79912b, network: testnet")
    # Chat input for user queries
    user_input = st.chat_input("Say something")
    if user_input:
        # Generate code based on query
        generated_code = chain.invoke({"query": user_input})

        # Display the generated code
        st.subheader("Generated Code")
        st.code(generated_code, language='python')

        # Execute the generated code and handle errors
        execution_result = run_code(generated_code)
        
        if "Error executing code" in execution_result:
            st.error("The generated code had an error. Please try again.")
            # Optionally, re-prompt GPT to generate new code or handle the error
        else:
            st.subheader("Execution Output")
            st.code(execution_result)

            # Show spinner while waiting for Gemini response
            with st.spinner("Processing with Gemini..."):
                # Send output to Gemini and get response
                messages = [
                    (
                        "system",
                        "You are a helpful assistant that interprets execution results and answers user questions.",
                    ),
                    ("human", execution_result)
                ]
                gemini_response = gemini_llm.invoke(messages)
                
            st.subheader("Gemini Response")
            st.markdown(gemini_response.content)

if __name__ == "__main__":
    main()
