import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    #api_key=os.environ.get("OPENAI_API_KEY"),
    #api_key="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"
    api_key="sk-proj-bF3cGeEfrQueOJZghNFNT3BlbkFJAXSR9hLbxBkE3LuwWxaM"
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)