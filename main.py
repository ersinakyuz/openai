import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
    # default is 2
    max_retries=0
)


response = client.with_options(max_retries=2).chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Give me the well known Duke Nukem cheats",
        }
    ],
    model="gpt-3.5-turbo",
    stream = False
)
print(response.choices[0].message.content)
