import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
)

deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

def get_llm_response(messages: list[dict]) -> str:
    chat_messages = [
        {
            "role": "system",
            "content": (
                "You are a medical assistant. ONLY answer questions related to health or symptoms.\n"
                "If the user's question is not medical-related, respond with:\n"
                "'Sorry, I can only help with medical and health-related questions.'"
            )
        }
    ] + messages  

    response = client.chat.completions.create(
        model=deployment,
        messages=chat_messages,
        max_tokens=800,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

    return response.choices[0].message.content.strip()

