import ollama

model_name = "llama3.2:latest"
prompt = "What is the capital of germany?"
response = ollama.generate(
    model = model_name,
    prompt = prompt,
)
print(response.response)