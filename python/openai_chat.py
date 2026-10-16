"""Chat with any AIFans API model through the official OpenAI SDK.  pip install openai"""
import os

from openai import OpenAI

client = OpenAI(api_key=os.environ["AIFANS_API_KEY"], base_url="https://api.aifans.fan/v1")
resp = client.chat.completions.create(
    model="deepseek-v4.1-flash",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=1000,  # reasoning models think first; thinking counts as output tokens
)
print(resp.choices[0].message.content)
print(resp.usage)
