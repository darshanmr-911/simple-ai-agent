import ollama

model_name = "llama3.2:latest"
prompt = input("Enter your prompt: ")
response = ollama.generate(
    model = model_name,
    prompt = prompt,
)
print(response.response)