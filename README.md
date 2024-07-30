# AelfGPT

AelfGPT is a powerful tool designed to enhance the development experience for Aelf blockchain developers. This application integrates advanced AI technologies to offer intelligent code debugging, code generation, and blockchain exploration functionalities. 

## Key Features

1. **Smart Contract Debugger**: Analyze and debug Aelf smart contract code written in C#. Get detailed insights into potential issues and suggestions for code improvements.

2. **Smart Contract Generator**: Generate and enhance Aelf smart contract code based on user input. Receive AI-driven suggestions for code enhancements.

3. **Chat with Aelf Documentation**: Interact with the Aelf documentation through an AI-powered chat interface. Ask questions and get responses based on the Aelf documentation.

4. **Aelf Block Explorer**: Explore and retrieve Aelf blockchain data, including:
   - **Chain Status**: View the current status of the blockchain.
   - **Block Information**: Retrieve block information by block hash or block height.
   - **Transaction Details**: Get details of specific transactions.
   - **Transaction Pool Status**: Check the status of transactions in the pool.

## Technologies

- **OpenAI GPT-4o**: For advanced code debugging and generation.
- **Google Gemini**: For enhanced AI capabilities and response accuracy.
- **MongoDB Atlas**: For managing vector embeddings and the knowledge base.
- **Streamlit**: For building the interactive web interface.

## Setup and Deployment

### 1. Fork and Clone the Repository

1. **Fork** this repository on GitHub to your own account.
2. **Clone** your forked repository:

   ```bash
   git clone https://github.com/your-username/smart-contract-debugger-generator.git
   cd smart-contract-debugger-generator
   ```

### 2. Create and Configure the `.env` File

Create a `.env` file in the root directory of your project using the provided example:

1. **Copy** the example `.env` file:

   ```bash
   cp .env.example .env
   ```

2. **Fill in** the environment variables:

   - **MONGODB_CONN_URI**: Your MongoDB connection URI.
   - **EDEN_AI_API_KEY**: Your Eden AI API key. Obtain it from [Eden AI](https://app.edenai.run/bricks/default).
   - **AI_ML_API_KEY**: Your GPT-4 API key from [AIML API](https://aimlapi.com/app/keys).
   - **GOOGLE_API_KEY**: Your Google API key from [Google Cloud](https://aistudio.google.com/app/prompts/new_chat).

### 3. Set Up Dependencies

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 4. Create Embeddings and Configure MongoDB Atlas

1. **Run** the Jupyter notebook provided to create and store embeddings into MongoDB.

2. **Configure MongoDB Atlas**:

   - **Create a Vector Search**:
     - Go to MongoDB Atlas and navigate to the search section.
     - Create a new vector search with the provided JSON configuration:

       ```json
       {
         "fields": [
           {
             "numDimensions": 1536,
             "path": "embedding",
             "similarity": "cosine",
             "type": "vector"
           }
         ]
       }
       ```

   - **Create Atlas Search**:
     - Select the `docs` collection and create an Atlas Search.
     - This process may take 1-2 hours. Once done, your vector search should be ready for use.

### 5. Run the Application Locally

Run the Streamlit application:

```bash
streamlit run app.py
```

Access the application at `http://localhost:8501`.

## Usage

1. **Smart Contract Debugging**:
   - Paste your .cs code into the text area.
   - Select "Debug Code" and click "Submit Debug Request".
   - View the debugging results provided by the AI.

2. **Smart Contract Generation**:
   - Paste your .cs code into the text area.
   - Select "Generate Code" and click "Submit Generate Request".
   - View the generated code improvements.

3. **Chat with Aelf Documentation**:
   - Navigate to the chat section to interact with Aelf documentation.
   - Ask questions and receive AI-powered responses based on the documentation.

4. **Aelf Block Exploration**:
   - Use the block explorer functionalities to retrieve and view various blockchain data.

## Deployment

To deploy the Streamlit application using Google Cloud Run:

1. **Deploy the App**:
   - Follow the Google Cloud Run documentation to deploy your Streamlit app. 

2. **Access the Deployed App**:
   - Once deployed, you will receive a URL to access your application online.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.
