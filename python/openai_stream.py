"""Streaming, with token usage in the last chunk.  pip install openai"""
import os

from openai import OpenAI

client = OpenAI(api_key=os.environ["AIFANS_API_KEY"], base_url="https://api.aifans.fan/v1")
stream = client.chat.completions.create(
    model="deepseek-v4.1-flash", max_tokens=1000, stream=True,
    stream_options={"include_usage": True},
    messages=[{"role": "user", "content": "Write a short poem about spring"}],
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
    if chunk.usage:
        print("\n", chunk.usage)
