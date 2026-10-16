# AIFans API examples

Copy-paste setups for [AIFans API](https://platform.aifans.fan/?utm_source=github&utm_medium=readme&utm_campaign=examples):
one OpenAI- and Anthropic-compatible API for DeepSeek, GLM, Kimi, MiniMax and Hunyuan models.

| | |
|---|---|
| OpenAI-compatible base URL | `https://api.aifans.fan/v1` |
| Anthropic-compatible base URL (Claude Code, Anthropic SDK) | `https://api.aifans.fan` |
| API key | create one in the [console](https://platform.aifans.fan/console#/keys) |

Most examples read the key from `AIFANS_API_KEY`:

```bash
export AIFANS_API_KEY="YOUR_API_KEY"          # macOS / Linux
$env:AIFANS_API_KEY = "YOUR_API_KEY"          # Windows PowerShell
```

## Coding tools

| Tool | Setup |
|---|---|
| Claude Code | [claude-code/](claude-code/) |
| OpenCode | [opencode/](opencode/) |
| Continue | [continue/](continue/) |
| Aider | [aider/](aider/) |
| Cline, Roo Code, Cursor and more | [guides](https://platform.aifans.fan/guides) |

## Code

| Language | Example |
|---|---|
| Python, OpenAI SDK | [python/openai_chat.py](python/openai_chat.py), [streaming](python/openai_stream.py), [thinking off](python/no_thinking.py) |
| Python, Anthropic SDK | [python/anthropic_messages.py](python/anthropic_messages.py) |
| Python, LangChain | [python/langchain_chat.py](python/langchain_chat.py) |
| Node, OpenAI SDK | [node/openai_chat.mjs](node/openai_chat.mjs) |
| Node, Vercel AI SDK | [node/ai_sdk.mjs](node/ai_sdk.mjs) |
| curl | [curl/](curl/) |

## Models

Send the model ID as `model`. Prices, peak hours and context sizes: [platform.aifans.fan/models](https://platform.aifans.fan/models).

| Model ID | Name | APIs |
|---|---|---|
| `deepseek-v4.1-flash` | DeepSeek V4.1 Flash | OpenAI, Anthropic |
| `deepseek-v4-pro` | DeepSeek V4 Pro | OpenAI, Anthropic |
| `hy3` | Hunyuan Hy3 | OpenAI, Anthropic |
| `hy4-preview` | Hunyuan Hy4 Preview | OpenAI, Anthropic |
| `hy-mt2-pro` | Hunyuan MT2 Pro (translation) | OpenAI |
| `hy-mt2-plus` | Hunyuan MT2 Plus (translation) | OpenAI |
| `hy-mt2-lite` | Hunyuan MT2 Lite (translation) | OpenAI |
| `glm-5.3` | GLM-5.3 | OpenAI, Anthropic |
| `glm-5.3-flash` | GLM-5.3 Flash | OpenAI, Anthropic |
| `minimax-m2.7` | MiniMax M2.7 | OpenAI, Anthropic |
| `kimi-k3` | Kimi K3 | OpenAI, Anthropic |

## Good to know

- Reasoning models think before they answer and thinking is billed as output tokens: give `max_tokens` 1000 or more.
- Each key has per-minute limits; when you hit one you get HTTP 429 with a `Retry-After` header. The SDKs and Claude Code
  retry on their own.
- Failed calls are never billed. Every call is listed in the console with its tokens and price.
- Top-ups carry a payment processing fee, shown at checkout.

AIFans API is an independent service and is not affiliated with or endorsed by the model makers named here.
Questions: support@platform.aifans.fan

## License

MIT: copy anything you like.
