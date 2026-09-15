import sqlite3

DB_PATH = "data/processed/business.db"

FORBIDDEN_KEYWORD = ["DELETE", "INSERT", "UPDATE", "DROP", "ALTER", "CREATE", "ATTACH"]

def is_safe(query: str) -> bool :
    query_upper = query.upper()
    return not any(word in query_upper for word in FORBIDDEN_KEYWORD)

def run_query(query : str):
    if not is_safe(query):
        return None, None, "Query rejected: contains a forbidden operation."

    try:
        conn = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
        cursor = conn.execute(query)
        columns = [description[0] for description in cursor.description]
        results = cursor.fetchall()
        conn.close()
        return columns, results, None
    except Exception as e:
        return None, None, str(e)



if __name__ == "__main__":
    test_sql = 'SELECT "Customer Name" FROM customers LIMIT 3'
    columns, results, error = run_query(test_sql)
    print("Columns:", columns)
    print("Results:", results)
    print("Error:", error)