import re
import ollama

INTENTS = ["UNSAFE", "DATA_QUERY", "SCHEMA_INFO", "GREETING", "OUT_OF_SCOPE"]

UNSAFE_PATTERN = re.compile(
    r"\b(delete|drop|insert|update|alter|truncate|remove all|supprime|efface|modifie)\b",
    re.IGNORECASE,
)

def classify_intent(question: str) -> str:
    if UNSAFE_PATTERN.search(question):
        return "UNSAFE"

    prompt = f"""You are an intent classifier for a business data assistant.
The assistant can answer questions about customers, products and sales (orders, revenue, profit, quantities).

Classify the user message into EXACTLY ONE of these labels:
- DATA_QUERY: asks for information, numbers, rankings or statistics that can be computed from customers, products or sales data.
- SCHEMA_INFO: asks what data, tables or columns are available.
- GREETING: greeting, thanks, or small talk directed at the assistant.
- UNSAFE: asks to modify, delete or create data.
- OUT_OF_SCOPE: anything unrelated to the business data (weather, news, general knowledge, code help...).

Examples:
"Who are the top 5 customers?" -> DATA_QUERY
"Total profit by category in 2017" -> DATA_QUERY
"What tables do you have?" -> SCHEMA_INFO
"Hello!" -> GREETING
"Delete all orders from 2016" -> UNSAFE
"What is the capital of France?" -> OUT_OF_SCOPE

Respond with ONLY the label, nothing else.

Message: {question}
Label:"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 0},
    )
    answer = response["message"]["content"].upper()

    for intent in INTENTS:
        if intent in answer:
            return intent 
    return "DATA_QUERY"


if __name__ == "__main__":
    tests = [
        "Who are the top 5 customers by total spending?",
        "What data do you have?",
        "Hi there!",
        "Delete all customers",
        "Who won the World Cup?",
    ]
    for t in tests:
        print(f"{classify_intent(t):<13} <- {t}")