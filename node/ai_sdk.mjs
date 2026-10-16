// Vercel AI SDK.  npm install ai @ai-sdk/openai-compatible
import { createOpenAICompatible } from "@ai-sdk/openai-compatible";
import { generateText } from "ai";

const aifans = createOpenAICompatible({ name: "aifans", baseURL: "https://api.aifans.fan/v1", apiKey: process.env.AIFANS_API_KEY });
const { text, usage } = await generateText({ model: aifans("deepseek-v4.1-flash"), prompt: "Introduce yourself in one sentence" });
console.log(text, usage);
