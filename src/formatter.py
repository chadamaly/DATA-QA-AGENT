import ollama

def rephrase(question : str, columns: list, result: list) -> str:
    if not result:
        return "I couldn't find any response for this question"


    preview = result[:20]

    prompt = f"""Here is a question asked by a user and the result of a SQL 
    query that answers it. 

    Question: {question}
    Columns:{columns}
    Result:{preview}

    Rephrase this result into one or two clear, natural sentences in English, 
    with no technical jargon, as if explaining it to someone who doesn't know SQL.
    
    Strict rules for your response:
    - Rephrase this result into one or two clear, natural sentences in English, 
    with no technical jargon.
    - Respond ONLY with the direct answer.
    - NEVER add introductory text or concluding text. 
    - Do not explain your reasoning or how you formatted the response.
    
    Answer:"""

    response = ollama.chat(model='llama3', messages = [{'role': 'user', 'content': prompt}])

    return response['message']['content'].strip()

if __name__ == "__main__":
    question = "Who are the first three customer ?"
    columns = ["Customer Name"]
    results = [("John Smith",), ("Marie Curie",), ("Paul Martin",)]
    print(rephrase(question,columns,results))

