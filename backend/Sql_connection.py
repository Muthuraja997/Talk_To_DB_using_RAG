import mysql.connector as sql_connect 
import os
from dotenv import load_dotenv
load_dotenv()

def get_schema_docs():
    conn=sql_connect.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    cursor=conn.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    schema_docs = []
    for table in tables:
        cursor.execute(f"DESCRIBE {table[0]}")
        schema_info = cursor.fetchall()
        schema_docs.append(f"Table: {table[0]}, Columns: {schema_info}")
    return schema_docs



def execute_any_sql(query):
    conn = sql_connect.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        if cursor.description:  # SELECT queries
            columns = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            result = [dict(zip(columns, row)) for row in rows]
            return result
        else:
            conn.commit()
            return f"Query executed successfully."
    except Exception as e:
        return f"SQL Error: {e}"
    finally:
        cursor.close()
        conn.close()


# def fetch_employees():
#     create_connection()
#     conn = create_connection()
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM Employees LIMIT 5;")
#     results = cursor.fetchall()
#     print("Fetched Employees:", results)
#     cursor.execute("SHOW TABLES;")
#     tables = cursor.fetchall()
#     print("Tables in the database:", tables)
#     cursor.close()
#     conn.close()
# fetch_employees()
