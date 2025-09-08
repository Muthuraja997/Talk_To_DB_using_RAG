# RAG.py
from fastapi import FastAPI
import os
from dotenv import load_dotenv
from Sql_connection import get_schema_docs

from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA


load_dotenv()

app = FastAPI()
schema_docs = get_schema_docs()


embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=os.getenv("GEMINI_API_KEY")
)


vectorstore = FAISS.from_texts(schema_docs, embeddings)
retriever = vectorstore.as_retriever()


llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GEMINI_API_KEY"))


qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever
)



import re
from Sql_connection import execute_any_sql

def is_sql_query(text):
    sql_keywords = [r"^\s*SELECT ", r"^\s*INSERT ", r"^\s*UPDATE ", r"^\s*DELETE "]
    return any(re.match(pattern, text, re.IGNORECASE) for pattern in sql_keywords)

if __name__ == "__main__":
    query = input("Enter your question:")
    result = qa.run(query)
    print("❓ Query:", query)
    # Remove code block markers if present
    cleaned_result = result.strip()

    if cleaned_result.startswith("```sql") and cleaned_result.endswith("```"):
        cleaned_result = cleaned_result[6:-3].strip()
    elif cleaned_result.startswith("```") and cleaned_result.endswith("```"):
        cleaned_result = cleaned_result[3:-3].strip()

    if is_sql_query(cleaned_result):
        print("Detected SQL query. Executing...")
        sql_result = execute_any_sql(cleaned_result)
        print("🗄️ SQL Result:", sql_result)
    else:
        print("🤖 Answer:", result)
