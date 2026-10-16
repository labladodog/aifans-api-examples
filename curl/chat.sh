#!/bin/sh
# OpenAI-compatible chat completion. export AIFANS_API_KEY=... first.
curl https://api.aifans.fan/v1/chat/completions \
  -H "Authorization: Bearer $AIFANS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "deepseek-v4.1-flash", "max_tokens": 1000, "messages": [{"role": "user", "content": "Hello"}]}'
