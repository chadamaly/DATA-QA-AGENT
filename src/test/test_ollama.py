import ollama

response = ollama.chat(model="llama3", messages=[{'role': 'user', 'content': "Just Answer 'Hi, it's working'"}])

print(response['message']['content'])