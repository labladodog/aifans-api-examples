"""DeepSeek V4 family: switch thinking off for simple tasks (faster and cheaper).  pip install openai"""
import os

from openai import OpenAI

client = OpenAI(api_key=os.environ["AIFANS_API_KEY"], base_url="https://api.aifans.fan/v1")
resp = client.chat.completions.create(
    model="deepseek-v4.1-flash",
    messages=[{"role": "user", "content": "Translate to French: good morning"}],
    max_tokens=200,
    extra_body={"thinking": {"type": "disabled"}},
)
print(resp.choices[0].message.content)
