from agent.llm_engine import generate_sql, SCHEMA
from agent.sql_executor import run_query
from agent.formatter import rephrase
from agent.intent_classifier import classify_intent

CANNED_RESPONSES = {
    "GREETING": "Hello! Ask me anything about your customers, products or sales.",
    "UNSAFE": "I can only read data, not modify it.",
    "OUT_OF_SCOPE": "I can only answer questions about customers, products and sales.",
}


def answer(question: str)->tuple[str | None, str]:
    print(f"n\Question: {question}")

    intent = classify_intent(question)
    print(f"Intent: {intent}")

    # Intents qui ne nécessitent pas de SQL
    if intent in CANNED_RESPONSES:
        return None, CANNED_RESPONSES[intent]

    if intent == "SCHEMA_INFO":
        return None, f"I can query these tables:\n{SCHEMA.strip()}"

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