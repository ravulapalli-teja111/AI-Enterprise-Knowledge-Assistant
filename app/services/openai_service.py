from openai import OpenAI

from app.config import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_DEPLOYMENT,
)


client = OpenAI(
    base_url=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY
)


def ask_ai(prompt: str) -> str:

    try:
        response = client.responses.create(
            model=AZURE_OPENAI_DEPLOYMENT,
            input=[
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.output_text

    except Exception as e:
        raise Exception(f"Azure AI Error: {e}")