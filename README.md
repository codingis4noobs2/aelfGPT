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
   git clone https://github.com/your-username/aelfgpt.git
   cd aelfgpt
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

Yes, you’re right. The `requirements.txt` file is used to install dependencies within the Docker container for Cloud Run deployment. Let's clarify the deployment process for Cloud Run by including the setup for `requirements.txt` in the Dockerfile and instructions. 

Here’s the updated README section with precise details for Cloud Run deployment:

---

## Deployment

### Deploy on Google Cloud Platform (GCP)

**Streamlit** can be deployed on Google Cloud Platform (GCP) using two popular services: **App Engine** and **Cloud Run**.

#### App Engine Deployment

1. **Install Required Tools**:
   - Install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/install).
   - Install Streamlit:

     ```bash
     pip install streamlit
     ```

2. **Create a Streamlit App**:
   - Write a simple Streamlit app and save it as `app.py`:

     ```python
     import streamlit as st

     st.title("Hello, Streamlit on App Engine!")
     st.write("This is a simple Streamlit app running on Google App Engine.")
     ```

3. **Create an `app.yaml` Configuration File**:
   - Create a file named `app.yaml` with the following content:

     ```yaml
     runtime: python39

     entrypoint: streamlit run app.py --server.enableCORS false --browser.serverAddress 0.0.0.0 --browser.gatherUsageStats false --server.port $PORT
     ```

4. **Deploy the App to App Engine**:
   - Authenticate with Google Cloud:

     ```bash
     gcloud auth login
     ```

   - Initialize your project:

     ```bash
     gcloud init
     ```

   - Deploy the app:

     ```bash
     gcloud app deploy
     ```

5. **Access the App**:
   - Open your app in a browser:

     ```bash
     gcloud app browse
     ```

#### Cloud Run Deployment

1. **Install Required Tools**:
   - Install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/install).
   - Install [Docker](https://docs.docker.com/get-docker/).
   - Install Streamlit:

     ```bash
     pip install streamlit
     ```

2. **Create a Streamlit App**:
   - Follow the same steps as in the App Engine deployment.

3. **Create a `Dockerfile`**:
   - Create a `Dockerfile` with the following content:

     ```dockerfile
     # Use the official Python image from the Docker Hub
     FROM python:3.9-slim

     # Set the working directory in the container
     WORKDIR /app

     # Copy the requirements.txt file into the container
     COPY requirements.txt .

     # Install dependencies from requirements.txt
     RUN pip install -r requirements.txt

     # Copy the rest of the application code into the container
     COPY . .

     # Run the Streamlit app
     CMD ["streamlit", "run", "app.py", "--server.enableCORS", "false", "--browser.serverAddress", "0.0.0.0", "--browser.gatherUsageStats", "false", "--server.port", "8080"]
     ```

   - Create a `requirements.txt` file in the root directory with the following content:

     ```
     streamlit
     ```

4. **Build and Deploy the Container to Cloud Run**:
   - Authenticate with Google Cloud:

     ```bash
     gcloud auth login
     ```

   - Initialize your project:

     ```bash
     gcloud init
     ```

   - Build the container:

     ```bash
     gcloud builds submit --tag gcr.io/PROJECT-ID/streamlit-app
     ```

   - Deploy the container:

     ```bash
     gcloud run deploy --image gcr.io/PROJECT-ID/streamlit-app --platform managed --allow-unauthenticated
     ```

5. **Access the App**:
   - The deployment output will display the URL of your app.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.
