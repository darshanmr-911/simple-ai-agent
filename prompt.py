import ollama

model_name = "llama3.2:latest"

#role
system_prompt = "You are a helpful assistant."

#task
user_prompt_v1 = "Write an introduction to Karnataka's wildlife for first-time visitors."

#constaints
user_prompt_v2 = """
Write an introduction to Karnataka's wildlife for first-time visitors.
150 words. Audience:
city dwellers who have never been on a spfari. Warm, vivid tone. Exactly three parks. No jargon.
"""

#format

user_prompt_v3 = """ rite an introduction to Karnataka's wildlife for first-time visitors.
150 words, city audience, warm and vivid, exactly three parks, no jargon.
Format: three bullets (park, signature animal, best month), then a one-line closing tip.
 """

#example
user_prompt_v4 = """ Write an introduction to Karnataka's wildlife for first-time visitors.
150 words, city audience, warm and vivid, no jargon. Exactly three parks (Bandipur, Nagarhole, Dandeli), each with one signature animal and the best Format: three bullets, then a closing line.
Example bullet: Bandipur: Wild elephants graze at dusk along the forest edge. Best in Nov-feb.| I
 """

messages = [
    {
        "role": "system",
        "content": system_prompt
    },
    {
        "role" : "user",
        "content" : user_prompt_v4
    }
]

response = ollama.chat(
    model = model_name,
    messages = messages,
)
print(response.message.content)