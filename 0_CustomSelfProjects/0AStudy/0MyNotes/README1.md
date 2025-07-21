


# Here are examples for Gemini, DeepSeek, Ollama and OpenRouter (https://github.com/ed-donner/agents/blob/main/guides/09_ai_apis_and_ollama.ipynb)

## Example 1: Using Gemini instead of OpenAI
Visit Google Studio to set up an account: https://aistudio.google.com/
Add your key as GOOGLE_API_KEY to your .env
Also add it a second time as GEMINI_API_KEY to your .env - this will be helpful later.
Then:

```python
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv(override=True)

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
google_api_key = os.getenv("GOOGLE_API_KEY")
gemini = OpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)
response = gemini.chat.completions.create(model="gemini-2.5-flash-preview-05-20", messages=[{"role":"user", "content": "what is 2+2?"}])
print(response.choices[0].message.content)
```

## Example 2: Using DeepSeek API instead of OpenAI (cheap, and only $2 upfront)
Visit DeepSeek API to set up an account: https://platform.deepseek.com/
You will need to add an initial $2 minimum balance.
Add your key as DEEPSEEK_API_KEY to your .env

Then:

```python
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv(override=True)

DEEPSEEK_BASE_URL = "https://api.deepseek.com/v1"
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
deepseek = OpenAI(base_url=DEEPSEEK_BASE_URL, api_key=deepseek_api_key)
response = deepseek.chat.completions.create(model="deepseek-chat", messages=[{"role":"user", "content": "what is 2+2?"}])
print(response.choices[0].message.content)
```

## Example 3: Using Ollama to be free and local instead of OpenAI
Ollama allows you to run models locally; it provides an OpenAI compatible API on your machine.
There's no API key for Ollama; there's no third party with your credit card, so no need for any kind of key.

If you're new to Ollama, install it by following the instructions here: https://ollama.com
Then in a Cursor Terminal, do ollama run llama3.2 to chat with Llama 3.2
BEWARE: do not use llama3.3 or llama4 - these are massive models not designed for home computing! They will fill up your disk.

Then:

```python
!ollama pull llama3.2

from openai import OpenAI

OLLAMA_BASE_URL = "http://localhost:11434/v1"
ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key="anything")
response = ollama.chat.completions.create(model="llama3.2", messages=[{"role":"user", "content": "what is 2+2?"}])
print(response.choices[0].message.content)
```

## Example 4: Using the popular service OpenRouter which has an easier billing process instead of OpenAI
OpenRouter is very convenient: it gives you free access to many models, and easy access with small upfront to paid models.

Sign up at https://openrouter.ai
Add the minimum upfront balance as needed
Add your key as OPENROUTER_API_KEY to your .env file

Then:

```python
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv(override=True)

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
openrouter = OpenAI(base_url=OPENROUTER_BASE_URL, api_key=openrouter_api_key)
response = openrouter.chat.completions.create(model="openai/gpt-4.1-nano", messages=[{"role":"user", "content": "what is 2+2?"}])
print(response.choices[0].message.content)
```

## Using different API providers with Agent Frameworks

The Agent Frameworks make it easy to switch between these providers. You can switch LLMs and pick different ones at any point in the course. There are more notes below on each of them. For OpenAI Agents SDK, see a section later in this notebook. For CrewAI, we cover it on the course, but it's easy: just use the full path to the model that LiteLLM expects.