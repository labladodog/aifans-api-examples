#!/bin/sh
# Anthropic-compatible messages call. export AIFANS_API_KEY=... first.
curl https://api.aifans.fan/v1/messages \
  -H "x-api-key: $AIFANS_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{"model": "deepseek-v4.1-flash", "max_tokens": 1000, "messages": [{"role": "user", "content": "Hello"}]}'
