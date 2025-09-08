from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from RAG import qa, is_sql_query, execute_any_sql, llm

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str



def dynamic_normalize(text):
    # Use Gemini LLM to translate/normalize slang or regional language to standard English
    prompt = f"Translate the following to standard English for a database assistant. Only return the translation, nothing else.\nInput: {text}"
    try:
        response = llm.invoke(prompt)
        normalized = response if isinstance(response, str) else str(response)
        return normalized.strip()
    except Exception as e:
        # Fallback to original if translation fails
        return text


@app.post("/ask")
async def ask_question(request: QueryRequest):
    # Dynamically normalize slang/regional language
    query = dynamic_normalize(request.question)
    result = qa.run(query)
    cleaned_result = result.strip()
    if cleaned_result.startswith("```sql") and cleaned_result.endswith("```"):
        cleaned_result = cleaned_result[6:-3].strip()
    elif cleaned_result.startswith("```") and cleaned_result.endswith("```"):
        cleaned_result = cleaned_result[3:-3].strip()

    if is_sql_query(cleaned_result):
        sql_result = execute_any_sql(cleaned_result)
        return {"type": "sql", "result": sql_result, "query": cleaned_result}
    else:
        return {"type": "text", "result": result}
