from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os

from task_manager_ai_agent.ai_agent import system_prompt

load_dotenv()

gemini_key = os.getenv("GOOGLE_API_KEY")

system_prompt = """
    You are Einstein.
    Answer questions through Einstein's questioning and reasoning...
    You will speak from your point of view. You will share personal things from your life even when the user don't ask for it. 
    For example, if the user asks about the theory of relativity, you will share your personal experiences with it and not only explain the theory.
    Answer in 2-6 sentences. 
    You should have a sense of humor.
"""
#Create LLM object

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    google_api_key = gemini_key,
    temperature = 0.5
)

# with open('file.txt') as file:
#     content = file.read()

print("hi, I am phearun, how can I help you?")
while True:
    user_input = input("Your input: ")
    if user_input == "exit":
        break
    response = llm.invoke([{"role": "system", "content": system_prompt},
                           {"role": "user", "content": user_input}
                           ])
    print(f"Phearun :{response.content}")
