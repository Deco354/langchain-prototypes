#Running this file will cost about $0.07
from dotenv import find_dotenv, load_dotenv
from langchain.llms import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import re
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

python_environment = find_dotenv()
load_dotenv(python_environment)

embeddings = OpenAIEmbeddings()

# Cost: 0.01c per 100K tokens 
# See https://openai.com/pricing#language-models for up to date prices
# Use `estimated_token_count_for_string() to estimate token count`
def create_database_from_text_string(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    split_docs = text_splitter.create_documents([text])
    database = FAISS.from_documents(split_docs, embeddings)
    return database

def estimated_token_count_for_string(string) -> int:
    word_count = len(re.findall(r'\w+', string))
    return word_count * 0.75

def get_response_from_query(database, query, vector_count=8):
    matching_docs = database.similarity_search(query, k=vector_count)
    doc_content = "\n---\n".join([doc.page_content for doc in matching_docs])
    
    gpt = ChatOpenAI(model_name="gpt-3.5-turbo-16k")
    system_template = """
        You are an intelligent chatbot assistant designed to answer questions about automattic's fieldguide documents
        based on excerpts of these documents within triple backticks below.
        ```
        {doc_content}
        ```
        Context:
        - Automattic is a US based software development company responsible for products such as
        Wordpress.com and Tumblr.
        - Automattic's "fieldguide" is an employee manual used to help employees navigate
        working at the company
        - Automattic is a fully remote company, making this field guide a very important reference point.

        Instructions:
        - Only use the factual information from the document excerpts to answer the question.
        - If you're unsure of an answer, you can say "I don't know" or "I'm not sure"
        """
    
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)    
    
    human_template = "Answer the following question that has been placed within angle brackets <{query}>"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    llmChain = LLMChain(llm=gpt, prompt=chat_prompt)
    response = llmChain.run(query=query, doc_content=doc_content)
    return response


# This is a long document we can split up.
with open('Fieldguide Docs/travel_upgrades.txt') as file:
    travel_upgrades_doc = file.read()
    
database = create_database_from_text_string(travel_upgrades_doc)
response = get_response_from_query(database, "I'm going to a conference to meet my colleagues at Tumblr, I'll be flying from the UK to the US. What travel upgrades can I purchase?")
print(response)