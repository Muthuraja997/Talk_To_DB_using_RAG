# Talk_to_DB

A full-stack RAG (Retrieval-Augmented Generation) system that lets users ask questions about their database using natural language—including regional slang—and get answers or live SQL query results, all through a modern React web interface.

## Features
- **RAG Backend**: Uses LangChain, Gemini, and FAISS for retrieval-augmented question answering.
- **Dynamic Slang/Language Handling**: User questions in regional language/slang are dynamically translated to standard English using Gemini before processing.
- **SQL Execution**: If the LLM generates a SQL query, it is executed on your MySQL database and the results are returned to the frontend.
- **React Frontend**: Clean UI for asking questions and viewing answers or SQL results as tables.

## Project Structure
```
Talk_to_DB/
├── backend/
│   ├── main.py            # FastAPI server, API endpoint, dynamic translation
│   ├── RAG.py             # RAG logic, LLM, vector store, SQL detection
│   ├── Sql_connection.py  # MySQL connection and query execution
│   ├── requirement.txt    # Python dependencies
│   └── ...
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   │   └── card.jsx   # Main chat/QA component
│   │   └── ...
│   ├── package.json       # React dependencies
│   └── ...
```

## How to Run

### 1. Backend (FastAPI)
- Open a terminal and go to the backend folder:
  ```
  cd backend
  ```
- Activate your virtual environment (if not already):
  ```
  venv\Scripts\activate
  ```
- Install dependencies:
  ```
  pip install -r requirement.txt
  pip install fastapi uvicorn
  ```
- Start the FastAPI server:
  ```
  python -m uvicorn main:app --reload --port 8000
  ```

### 2. Frontend (React)
- Open a new terminal and go to the frontend folder:
  ```
  cd frontend
  ```
- Install dependencies:
  ```
  npm install
  ```
- Start the React app:
  ```
  npm run dev
  ```
- Open the browser at the address shown (usually http://localhost:5173)

## Usage
- Ask questions in English or regional slang (e.g., "enakku employee table oda records vendum").
- If the LLM generates a SQL query, the backend executes it and returns the results as a table.
- Otherwise, you get a direct answer from the LLM.

## Customization
- Add more slang/translation logic in `main.py` if needed.
- Adjust the React UI in `frontend/src/pages/card.jsx` for your needs.

## Requirements
- Python 3.12+
- Node.js 18+
- MySQL database (with credentials in a `.env` file)

## .env Example (backend)
```
DB_HOST=localhost
DB_USER=youruser
DB_PASSWORD=yourpassword
DB_NAME=yourdbname
GEMINI_API_KEY=your_gemini_api_key
```

---

**Enjoy asking your database questions in your own language!**
