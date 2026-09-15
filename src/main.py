from agent.llm_engine import generate_sql
from agent.sql_executor import run_query
from agent.formatter import rephrase

def answer(question: str)->str:
    print(f"n\Question: {question}")

    sql=generate_sql(question)
    print(f"Generated SQL :\n{sql}")

    columns, results, error = run_query(sql)
    if error:
        return sql, f"Error while executing the query : {error}"

    response = rephrase(question, columns, results)

    return sql, response

def interactive_loop():
    print("=== Data Q&A Agent ===")
    print("Ask a question about sales, customers, or products.")
    print("Type 'quit' to exit.\n")

    while True:
        question = input("Your question: ")
        if question.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break

        sql, response = answer(question)
        print(f"\nAnswer: {response}\n")


if __name__ == "__main__":
    interactive_loop()