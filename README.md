# langchain-prototypes
A repository for me to experiment with Langchain

## Installation

#### 1. Clone the repository

```bash
git clone https://github.com/deco354/langchain-prototypes.git
```

#### 2. Create a Python environment

Python 3.6 or higher using `venv` or `conda`. Using `venv`:

Using `conda`:
``` bash
cd langchain-prototypes
conda create -n langchain-env python=3.8
conda activate langchain-env
```

#### 3. Install the required dependencies
``` bash
pip install -r requirements.txt
```

#### 4. Set up the keys in a .env file

First, create a `.env` file in the root directory of the project. Inside the file, add your OpenAI API key:

```makefile
OPENAI_API_KEY="your_api_key_here"
```

Save the file and close it. In your Python script or Jupyter notebook, load the `.env` file using the following code:
```python
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
```

## Using Flowise chatbot
Download and Install [NodeJS](https://nodejs.org/en/download) >= 18.15.0

1. Install Flowise
    ```bash
    npm install -g flowise
    ```
2. Start Flowise

    ```bash
    npx flowise start
    ```
3. Open [http://localhost:3000](http://localhost:3000)
4. Within Flowise go to Setttings -> Load Chatflow and select "Document Chatbot Chatflow.json"
