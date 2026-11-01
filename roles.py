import ollama

model_name = "llama3.2:latest"
prompt = input("Enter your prompt: ")

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant."

    },
    {
        "role" : "user",
        "content" : prompt
    }
]

response = ollama.chat(
    model = model_name,
    messages = messages,
)
print(response.message.content)