import os
import anthropic
# Create an instance of the Anthropics API client

api_key=os.environ.get("CLAUDE_API_KEY"),
client = anthropic.Anthropic(api_key) 

response = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, world"}]
)