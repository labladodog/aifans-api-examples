"""The Anthropic-compatible endpoint, with the official Anthropic SDK.  pip install anthropic"""
import os

import anthropic

client = anthropic.Anthropic(api_key=os.environ["AIFANS_API_KEY"], base_url="https://api.aifans.fan")
msg = client.messages.create(
    model="deepseek-v4.1-flash",
    max_tokens=1000,
    messages=[{"role": "user", "content": "Hello"}],
)
print("".join(b.text for b in msg.content if b.type == "text"))
print(msg.usage)
