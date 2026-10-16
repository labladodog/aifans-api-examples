"""LangChain.  pip install langchain-openai"""
import os

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="deepseek-v4.1-flash", base_url="https://api.aifans.fan/v1",
                 api_key=os.environ["AIFANS_API_KEY"], max_tokens=2000)
print(llm.invoke("Introduce yourself in one sentence").content)
