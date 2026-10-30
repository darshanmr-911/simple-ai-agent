import ollama

model_name = "llama3.2:latest"
message = [
    {
        "role" : "system",
        "content" : "You are a friendly assistant."
    },
    
]

while True:

    user_input = input("You: ")
    if user_input.lower() == "exit" or user_input.lower() == "quit" or user_input.lower() == "bye":
        print("Exiting the chat. Goodbye!")
        break
    user_role ={
        "role" : "user",
        "content" : user_input
    }
    message.append(user_role)
    response = ollama.chat(
        model = model_name,
        messages = message,
    )
    print("Assistant: " + response.message.content)
    assistant_role = {
        "role" : "assistant",
        "content" : response.message.content
    }
    message.append(assistant_role)
