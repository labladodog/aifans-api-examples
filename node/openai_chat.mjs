// Chat with the official OpenAI SDK.  npm install openai
import OpenAI from "openai";

const client = new OpenAI({ apiKey: process.env.AIFANS_API_KEY, baseURL: "https://api.aifans.fan/v1" });
const resp = await client.chat.completions.create({
  model: "deepseek-v4.1-flash",
  messages: [{ role: "user", content: "Hello" }],
  max_tokens: 1000,
});
console.log(resp.choices[0].message.content);
console.log(resp.usage);
