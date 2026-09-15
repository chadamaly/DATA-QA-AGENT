import ollama

SCHEMA = """
TABLE customers ("Customer ID", "Customer Name", "Segment", "City", "State", "Country")
TABLE products ("Product ID", "Product Name", "Category", "Sub-Category")
TABLE sales ("Order ID", "Order Date", "Customer ID", "Product ID", "Sales", "Quantity", "Profit")
"""

def generate_sql(question : str) -> str:
    prompt = f"""You are SQL query generator for SQLite.

Here is the database schema :
{SCHEMA}

Strict rules :
- Respond ONLY with the SQL query, no explanation or extra text
- Only use the tables and columns listed above
- Never use INSERT, UPDATE, DELETE, DROP, ALTER, or CREATE
- ALWAYS enclose columns or table names that contain spaces in double quotes 
(e.g., "Customer ID")
- For questions about "best-selling" products or "top spending" customers, always 
calculate the cumulative total using SUM() instead of looking at individual transaction rows.
- ALWAYS prefix columns with their table alias when doing a JOIN to avoid ambiguous errors.
- When calculating totals (SUM) or counts (COUNT) per entity, ALWAYS use GROUP BY before ORDER BY.
- If the question is ambiguous, make the most reasonable interpretation.

Question : {question}

SQL:"""

    response = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': prompt }])

    raw_sql = response['message']['content']
    return clean_sql(raw_sql)

def clean_sql(text:str) -> str:
    text = text.replace("```sql", "").replace("```","")
    return text.strip()


if __name__ == "__main__":
    question = "Who are the top 5 customers by total spending ?"
    sql = generate_sql(question)
    print("Question:", question)
    print("Generate SQL:\n", sql)

    