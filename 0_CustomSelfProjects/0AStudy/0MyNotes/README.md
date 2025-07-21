https://techcommunity.microsoft.com/blog/azure-ai-services-blog/use-azure-openai-and-apim-with-the-openai-agents-sdk/4392537

# Agentic Frameworks

- Semantic Kernel
- AutoGen
- Azure AI Agent

> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦

# What is the openai python client library

The companies behind these LLMs, such as OpenAI, Anthropic, Google and DeepSeek, have built web endpoints. You call their models by making an HTTP request to a Web Address and passing in all the information about your prompts.

But it would be painful if we needed to build HTTP requests every time we wanted to call an API.

To make this simple, the team at OpenAI wrote a python utility known as a "Python Client Library" which wraps the HTTP call. So you write python code and it calls the web.

## It is:

  - A lightweight python utility
  - Turns your python requests into an HTTP call
  - Converts the results coming back from the HTTP call into python objects

## What it is NOT

  - It's not got any code to actually run a Large Language Model! No GPT code! It just makes a web request
  - There's no scientific computing code, and nothing particularly specialized for OpenAI

## How to use it:

**Create an OpenAI python client for making web calls to OpenAI**
> openai = OpenAI()


**Make the call**
> response = openai.chat.completions.create(model="gpt-4.1-mini", messages=[{"role":"user", "content": "what is 2+2?"}])

**Print the result**
> print(response.choices[0].message.content)


## What does this do

When you make the python call: openai.chat.completions.create()
It simply makes a web request to this url: https://api.openai.com/v1/chat/completions
And it converts the response to python objects.

That's it.

Here's the API documentation if you make direct web HTTP calls (https://platform.openai.com/docs/guides/text?api-mode=chat&lang=curl)
And here's the same API documentation if you use the Python Client Library (https://platform.openai.com/docs/guides/text?api-mode=chat&lang=python)


## With that context - how do I use other LLMs?


It turns out - it's super easy!

All the other major LLMs have API endpoints that are compatible with OpenAI.

And so OpenAI did everyone a favor: they said, hey look - you can all use our utility for converting python to web requests. We'll allow you to change the utility from calling https://api.openai/com/v1 to calling any web address that you specify.

And so you can use the OpenAI utility even for calling models that are NOT OpenAI, like this:

```
not_actually_openai = OpenAI(base_url="https://somewhere.completely.different/", api_key="another_providers_key")
```

It's important to appreciate that this OpenAI code is just a utility for making HTTP calls to endpoints. So even though we're using code from the OpenAI team, we can use it to call models other than OpenAI.

Here are all the OpenAI-compatible endpoints from the major providers. It even includes using Ollama, locally. Ollama provides an endpoint on your local machine, and they made it OpenAI compatible too - very convenient.

```
  ANTHROPIC_BASE_URL = "https://api.anthropic.com/v1/"
  DEEPSEEK_BASE_URL = "https://api.deepseek.com/v1"
  GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
  GROK_BASE_URL = "https://api.x.ai/v1"
  GROQ_BASE_URL = "https://api.groq.com/openai/v1"
  OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
  OLLAMA_BASE_URL = "http://localhost:11434/v1"
```

## Costs of APIs

The cost of each API call is very low indeed - most calls to models we use on this course are fractions of cents.

**But it's extremely important to note:**

  - A complex Agentic project could involve many LLM calls - perhaps 20-30 - and so it can add up. It's important to set limits and monitor usage.

  - With Agentic AI, there is a risk of Agents getting into a loop or carrying out more processing than intended. You should monitor your API usage, and never put more budget than you are comfortable with. Some APIs have an "auto-refill" setting that can charge automatically to your card - I strongly recommend you keep this off.

  - You should only spend what you are comfortable with. There is a free alternative in Ollama that you can use as a replacement if you wish. DeepSeek, Gemini 2.5 Flash and gpt-4.1-nano are significantly cheaper.

Keep in mind that these LLM calls typically involve trillions of floating point calculations - someone has to pay the electricity bills!


> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦

# What’s the difference between ChatGPT and the GPT API, both offered by OpenAI?

- ChatGPT is an end-user tool. It’s a Chat product designed for consumers who are AI users.
  -  It has a free plan, and it also has paid subscription plans with more features.
  - The subscription plans give the user near-unlimited access to use the Chat product.


- The API is a service provided for AI engineers - software engineers and data scientists - working on other commercial products.
  - It allows technical people, like you and me, to access the underlying models (like “GPT4.1” and “o3”) so that we can build our own products.
  - If we wanted to, we could build our own version of ChatGPT using the API, and charge our end-users for it.
  - Like most APIs, OpenAI charges a small amount based on API usage. For most examples on the course using gpt-4o-mini, it’s of the order of $0.001 per API call.

- I’m paying $20/month for ChatGPT - why do I need to pay more for the API?
  - Hopefully this is now clear. The API is not for consumers; it’s for engineers to build their own platforms that they can charge for.
  - If you were to have access to the API based on your subscription, then you could offer ChatGPT tools to others at a cheaper price, and put OpenAI out of business!
  - Keep in mind: each API call may require 10,000,000,000,000 floating point calculations - that compute uses electricity!

Instead of calling the API, you can run open source models locally, but typically they have 1,000 times fewer calculations — and even though it’s tiny, that processing still hits your electricity bill..

> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦


# What Are AI Agents?

AI agents are programs that perceive their environment, decide, and act autonomously toward achieving goals .

**Core components:**

- Perception – receives input (user text, API responses, environment data).

- Decision-making – selects the next step or tool to use.

- Action – performs activities (e.g., calls an API, retrieves data).

- Autonomy – operates independently, chaining multiple steps .

> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦

# 🎯 2. Why AI Agents Matter

Able to handle multi-step processes, reason, and use specialized tools.

Provide scalability and power beyond static models—agents are holistic systems, not just LLMs .


> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦

# 📚 3. Real-World Use Cases
Scheduling assistants: scan calendars, propose times, send invites.

Research bots: fetch documents, summarize, validate information.

Developer agents: review code, annotate PRs, suggest improvements .

> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
# Semantic Kernel VS AutoGen VS Azure AI Agent

| Feature / Aspect         | **Semantic Kernel**                                            | **AutoGen**                                                         | **Azure AI Agent**                           |
| ------------------------ | -------------------------------------------------------------- | ------------------------------------------------------------------- | -------------------------------------------- |
| **Publisher / Owner**    | Microsoft                                                      | Microsoft Research                                                  | Microsoft (Azure)                            |
| **Open Source**          | Yes (GitHub)                                                   | Yes (GitHub)                                                        | No (Proprietary; Azure Service)              |
| **Primary Use Case**     | Build AI agents, integrate LLMs with skills, orchestration     | Multi-agent workflow orchestration, agent-to-agent chat, evaluation | Enterprise AI agents, workflow automation    |
| **Programming Language** | C#, Python                                                     | Python                                                              | Azure platform (API-based, SDKs)             |
| **Agent Orchestration**  | Yes (via “skills” and “planners”)                              | Yes (flexible, supports multi-agent conversations)                  | Yes (via workflows, triggers, orchestration) |
| **Integration**          | Plugins, Skills, Connectors for external APIs                  | Custom agents, tools, function-calling                              | Deep Azure integration, other MS services    |
| **LLM Support**          | OpenAI, Azure OpenAI, HuggingFace, local LLMs                  | OpenAI, Azure OpenAI, Anthropic, others                             | Azure OpenAI, Cognitive Services             |
| **Extensibility**        | High (Skills, Planners, custom connectors)                     | Very High (custom agent definition, tool use)                       | Moderate (within Azure ecosystem)            |
| **UI / Frontend**        | No built-in UI                                                 | No built-in UI                                                      | Azure Portal, APIs                           |
| **Best For**             | Developers needing flexible AI integration, skill-based agents | Research, experimentation, multi-agent systems                      | Enterprises, business process automation     |
| **Deployment**           | Cloud, On-Prem, Local                                          | Local, Cloud                                                        | Cloud (Azure only)                           |
| **Pricing**              | Free (OSS)                                                     | Free (OSS)                                                          | Paid (Azure subscription required)           |
| **Community & Support**  | Active OSS community, MS support                               | OSS community, active research                                      | Enterprise support via Microsoft             |
| **Example Use**          | AI copilots, chatbots, workflow automation                     | Agent debates, tool-using agents, agent evaluation                  | Internal/external AI agents for business     |


> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦

# Requirements

- Python 3.12+
- create your venv using python3.12 
  
```python
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
- correct versions are installed from the requirements.txt file
  
```python
pip install -r "D:\0Personal_workfolder\ai_workfolder\ai-agents-for-beginners-main\requirements.txt"
```

- Configure Environment Variables
```
  - Copy .env.example to .env.
  - Add your GitHub personal access token if using local (GitHub Models) or your Azure credentials if using Azure.
```
- A GitHub Account - For Access to the GitHub Models Marketplace
- Azure Subscription - For Access to Azure AI Foundry
- Azure AI Foundry Account - For Access to the Azure AI Agent Service

- install jupyterlab to view or run ipynb

```python
pip install jupyterlab

# Once installed, launch JupyterLab with:

jupyter lab

```

> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦

# 🌍 What Is an Environment Variable?

An environment variable is a key–value pair stored by your operating system that programs can access at runtime. They’re used to configure programs without hardcoding settings in code. Think of them as invisible notes your system uses to tell programs what to do.

## 🐍 Using Environment Variables in Python 

Use the os module:

```python
import os

value = os.getenv("FAVORITE_COLOR")
print("Your favorite color is:", value)

```

## Using load_dotenv(override=True)

In this course, you’ll use python-dotenv. It allows you to load variables from a file named .env into your environment.

```python

from dotenv import load_dotenv
load_dotenv(override=True)

```

- This looks for a file named .env in the current directory.

- It reads each line and sets environment variables.

- override=True means any existing environment variables will be overwritten by values from the .env file.


## 📁 What Is a .env File?

A .env file is a plain text file that contains environment variables:

```ini
OPENAI_API_KEY=sk-123abc456def
DEBUG=True
```

## 🕵️ Hidden Files

Files starting with . are hidden in UNIX-like systems (Mac, Linux). You won’t see them unless you:

  - Use ls -a on the terminal.

  - Press ⌘+Shift+. in Finder (Mac).

  - Enable hidden items in File Explorer (Windows).

You can create one like this:

```bash
touch .env
```

Or just create a file called .env in Cursor or VS Code.

## ❌ The .gitignore File and Why It Should Include .env

Your .env file must not be shared publicly. It may contain secrets like API keys or passwords.

You should add .env to your .gitignore file:

```bash
.env

```

This tells Git to ignore the .env file and not include it in commits.

✅ Good practice:

  - Put .env in .gitignore

  - Share a .env.example file with placeholder values so teammates can fill in their own secrets.



## Environment Variables and the .env file


- Environment variables store config outside of your code
- Use os.getenv() in Python to read them
- Use .env files for development with python-dotenv
- Never commit .env files to Git—use .gitignore
- Works cross-platform on Windows and Mac
- uv handles package dependencies; .env handles configuration



## Example 

```python

import os
from dotenv import load_dotenv

load_dotenv(override=True)

api_key = os.getenv("OPENAI_API_KEY")
print(api_key)


```



> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦

# Python Client Libraries

## What is a Client Library?

A client library is a Python package that wraps HTTP calls for an API.

Instead of this:

```python
import requests
requests.post(
    "https://api.sendgrid.com/v3/mail/send",
    headers={...},
    json={...}
)
```

You do this:

```python
import sendgrid
sg = sendgrid.SendGridAPIClient(api_key)
sg.send(message)

```

## Why Use Them?

  - They abstract away raw HTTP

  - They handle auth headers, request formats, errors

  - They’re more readable and often safer


> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦

# 🧭 Part 5: Typical Steps to Use an API

- Sign up on the API provider’s website (e.g., OpenAI, SendGrid)
- Read the documentation to find available endpoints and example usage
- Get your API key (usually from a dashboard or developer console)
- Add the key to .env in your project
- Install the client library with uv add

```sh
uv add openai
uv add python-dotenv
```

- Import and use the client library in your Python code
  - The library sends requests to the endpoint using your key


> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦


# Example – Use the OpenAI API

1. Set up your environment
  
```bash

uv add openai python-dotenv

```

2. Save your key in .env

```ini

OPENAI_API_KEY=sk-abc123...


```

3. Write Python code to make the API call

```python

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What's the capital of France?"}
    ]
)

print(response.choices[0].message.content)


```



> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦


#  Example – Send Email with SendGrid

1. Sign up at https://sendgrid.com/
   
   - Get your API key

   - Enable "Mail Send" permissions

2. Save the key in .env
```ini
SENDGRID_API_KEY=SG.abc123...

```


3. Install the library
```bash

uv add sendgrid python-dotenv

```

4. Send an email
   
```python

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

load_dotenv()

message = Mail(
    from_email='you@example.com',
    to_emails='student@example.com',
    subject='Hello from Python!',
    plain_text_content='This is a test email sent via SendGrid API.'
)

try:
    sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(f"Status Code: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")

```



> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦

# Notebooks vs Scripts/Modules

| Feature                 | Notebook (`.ipynb`)                            | Script/Module (`.py`)                                    |
| ----------------------- | ---------------------------------------------- | -------------------------------------------------------- |
| Format                  | JSON-based, cell-oriented                      | Plain text, line-by-line code                            |
| Execution Style         | Interactive, cell-by-cell                      | Runs top to bottom as one program                        |
| Best Use                | Exploratory coding, data analysis, prototyping | Production code, reusable functions, structured projects |
| Visibility of Variables | Variables persist across cells                 | Variables last only during one run                       |
| Visuals & Output        | Shows plots and outputs inline                 | Outputs only to terminal/console                         |


> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦

# Common Tips & Techniques in Cursor

| Task                 | How to do it in Cursor                                      |
| -------------------- | ----------------------------------------------------------- |
| Open Terminal        | `Ctrl + backtick` or View > Terminal                        |
| Run a script with uv | `uv run your_script.py`                                     |
| Add a new package    | `uv add package_name`                                       |
| Sync environment     | `uv sync`                                                   |
| Create a notebook    | Right-click > New File > name it `something.ipynb`          |
| Set kernel           | Click “Select Kernel” in top-right of notebook              |
| Run notebook cell    | `Shift + Enter`                                             |
| Restart kernel       | Top menu in notebook > Restart Kernel                       |
| Run all cells        | Top menu in notebook > Run All                              |
| Comments             | Use `# comment` in scripts, and Markdown cells in notebooks |



> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦


# Jupyter Notebooks 

## Use Notebooks to Explore, Modules to Structure: If your notebook gets long or messy, move functions into a .py file.


Move the reusable code into helpers.py
For example:
In your notebook:

```python
def clean_text(text):
    return text.lower().strip()
```


Move that into helpers.py:


```python
# helpers.py
def clean_text(text):
    return text.lower().strip()
```

Import the function back into your notebook
In your notebook cell:

```python
from helpers import clean_text

clean_text("   Hello World!  ")
```

🧩 If helpers.py is in the same folder (directory) as your notebook file, you can import from it using:

```python
from helpers import clean_text
```

But there are a few things to understand to make sure it works smoothly:

✅ 1. File Location Matters
Your notebook must be running in the same directory as helpers.py, or helpers.py must be in a folder that’s on the Python path.

So if your structure looks like this:

```markdown
project/
├── test.ipynb
└── helpers.py
```

Then you can directly do:

```python
from helpers import clean_text
```

🧪 To check what the current working directory is inside your notebook, run:

```python
import os
os.getcwd()
```


⚠️ 2. If your file is in a subfolder

Say you have:

```markdown
project/
├── test.ipynb
└── utils/
    └── helpers.py
```

Then you’d need an init.py in utils/ to make it a Python package, and import like this:

```python
from utils.helpers import clean_text
```


🔁 3. Reloading after edits (during development)

If you change helpers.py while your notebook is still running, Python won’t automatically reload it. Use IPython’s autoreload magic:

At the top of your notebook:

```python
%load_ext autoreload
%autoreload 2
```
This will auto-reload imported modules every time you run a cell, so you don’t have to restart the kernel.


🧪 4. What if it still can’t find the file?

You can manually add the directory to sys.path:

```python
import sys
sys.path.append("/path/to/your/helpers/file")
```
But this is usually unnecessary if the file is in the same folder or a subfolder.


## The exclamation point

There's a super useful feature of jupyter labs; you can type a command with a ! in front of it in a code cell, like:

!ls
!pwd

And it will run it at the command line (as if in Windows Powershell or Mac Terminal) and print the result

```python
!ping cnn.com

```

## The package tqdm will print a nice progress bar if you wrap any iterable.

```python
# Here's some code with no progress bar
# It will take 10 seconds while you wonder what's happpening..

import time

spams = ["spam"] * 1000

for spam in spams:
    time.sleep(0.01)
```

```python
# And now, with a nice little progress bar:

import time
from tqdm import tqdm

spams = ["spam"] * 1000

for spam in tqdm(spams):
    time.sleep(0.01)
```

```python
# On a different topic, here's a useful way to print output in markdown

from IPython.display import Markdown, display

display(Markdown("# This is a big heading!\n\n- And this is a bullet-point\n- So is this\n- Me, too!"))

```


> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦

# python import

1. import xxx


```python
import math

```

Then, to use a function from math, you must include math. before the function name.


```python
# Using math.sqrt to calculate the square root of 16
result = math.sqrt(16)
print(result)  # Output: 4.0

```


2. from xxx import yyy

```python
from math import sqrt

```

Now, you can call sqrt directly without the math. prefix:

```python
# Directly using sqrt to calculate the square root of 16
result = sqrt(16)
print(result)  # Output: 4.0

```

# import xxx as zz

Sometimes, you might want to use a shorter name for a module. You can use as to rename the module when importing.


```python
import numpy as np

```

Now, you can use np instead of numpy:

```python
# Using numpy's array function
import numpy as np

my_array = np.array([1, 2, 3])
print(my_array)  # Output: [1 2 3]

```





> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦

# Python functions including default arguments:

## Defining a Function

To define a function in Python, we use the def keyword, followed by the function's name, parentheses (), and a colon :. Inside the parentheses, you can specify arguments (inputs the function can accept). The code inside the function is indented.

Here's a basic example:

```python
def greet():
    print("Hello, world!")

greet()

```

## Adding Arguments to a Function

```python
def greet(name):
    print("Hello, " + name + "!")


greet("Alice")

```

## Multiple Arguments

You can add more than one argument by separating them with commas. For example:

```python
def add_numbers(a, b):
    result = a + b
    print(result)


add_numbers(5, 10)

```


## Return Values

Sometimes, instead of just printing the result, we want the function to return a value so we can use it elsewhere. To do this, we use the return keyword. Here’s an example that returns the sum of two numbers:


```python
def add_numbers(a, b):
    result = a + b
    return result

```
Now, when we call add_numbers(5, 10), we can store the result in a variable or use it in other expressions:

```python
sum_result = add_numbers(5, 10)
print(sum_result)

```

Output:

```python
30

```


### Default Arguments

You can also set default values for arguments. If an argument with a default value is not provided, Python will use the default. This can make functions more flexible.

```python
def greet(name="stranger"):
    print("Hello, " + name + "!")

greet()

```


> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦

# Python f-strings including number and date formatting:

In Python, f-strings (formatted string literals) make it easy to insert variables and expressions directly into strings. 

```python
name = "Alice"
age = 30
message = f"Hello, my name is {name} and I am {age} years old."
print(message)

```

Output:

```python
Hello, my name is Alice and I am 30 years old.

```

**Example with Expressions**

You can even include expressions (like calculations) within the curly braces:

```python
width = 5
height = 10
area_message = f"The area of a {width}x{height} rectangle is {width * height}."
print(area_message)

```

Output:

```python
The area of a 5x10 rectangle is 50.

```

## Formatting Numbers

f-strings allow you to format numbers directly inside the string. For example, you can format a number with commas and set the number of decimal places.


**Example with :,.2f**

The format specifier :,.2f does the following:

   - : signals that you’re starting a format specification.
   - , adds comma separators for thousands.
   - .2f formats the number as a floating point with 2 decimal places.


```python
price = 1234567.8912
formatted_price = f"The price is ${price:,.2f}"
print(formatted_price)

```

Output:

```python
The price is $1,234,567.89

```

## Formatting Dates

You can also use f-strings to format dates. For this, you’ll typically use the datetime module.

```python
from datetime import datetime

current_date = datetime.now()
formatted_date = f"Today’s date is {current_date:%B %d, %Y}."
print(formatted_date)

```

Output (if today’s date is November 9, 2024):

```python
Today’s date is November 09, 2024.

```

Here’s what’s happening in {current_date:%B %d, %Y}:

  - %B represents the full month name (e.g., "November").
  - %d is the day of the month (with leading zero if necessary).
  - %Y is the four-digit year.

**Summary of Common Formatting Options**

   - {value:.2f}: Format as a float with 2 decimal places.
   - {value:,.2f}: Add commas as thousands separators, with 2 decimal places.
   - {date:%B %d, %Y}: Format a datetime object to display month, day, and year.



> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦

# Python files including modes, encoding, context managers, Path, glob.glob:

## 1. Using the open() Function

The open() function is used to open a file for reading, writing, or other operations. Its basic syntax is:

```python
file = open('filename', mode, encoding='optional')

```

**Common Modes**

   - 'r' (read): Default mode. Opens the file for reading. File must exist.
   - 'w' (write): Opens the file for writing. Overwrites if the file exists, creates a new one if it doesn’t.
   - 'a' (append): Opens the file to append data. Creates a new file if it doesn’t exist.
   - 'x' (exclusive creation): Creates a new file. Fails if the file exists.

**Specifying Encoding**

Windows often uses a different default encoding (e.g., cp1252) than many other systems (utf-8). To ensure compatibility, specify the encoding:

```python
file = open('filename.txt', 'r', encoding='utf-8')

```

## 2. Using Context Managers

The best practice for working with files in Python is to use a context manager with the with statement. 

   - Automatically closes the file when the block is exited, even if an error occurs.
   - Is cleaner and safer.
   - Avoids resource leaks.


**Example: Reading a File**


```python
with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

```

**Example: Writing to a File**
```python
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write("Hello, World!")

```

**Example: Appending to a File**

```python
with open('output.txt', 'a', encoding='utf-8') as file:
    file.write("\nThis is an appended line.")

```

## 3. Reading Line by Line
If the file is large, you may want to read it line by line instead of loading the entire file into memory:


```python
with open('example.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip())  # Strip removes newline characters

```

## 4. Handling Paths

Paths can vary depending on the operating system (Windows uses \, while Linux/Mac use /). Python's os and pathlib libraries make handling paths platform-independent.

### Using os.path

```python
import os

# Construct a file path
file_path = os.path.join('folder', 'subfolder', 'example.txt')
print(file_path)

```

### Using pathlib

The pathlib library (introduced in Python 3.4) offers an object-oriented approach:

```python
from pathlib import Path

# Construct a file path
file_path = Path('folder') / 'subfolder' / 'example.txt'
print(file_path)

# Check if a file exists
if file_path.exists():
    print(f"{file_path} exists!")

```

## 5. Listing Files in a Directory

To list files matching a pattern (e.g., all .txt files), use glob.glob:


```python
import glob

# List all .txt files in the current directory
txt_files = glob.glob('*.txt')
print(txt_files)

```

For subdirectories, use the ** wildcard with the recursive=True argument:

```python
# List all .txt files in current directory and subdirectories
all_txt_files = glob.glob('**/*.txt', recursive=True)
print(all_txt_files)

```

## 6. Putting It All Together

Here’s a complete example that:

   - Reads a file line by line.
   - Writes new content to another file.
   - Uses platform-independent paths and lists files in a directory.

```python
from pathlib import Path
import glob

# Define file paths using pathlib
input_file = Path('data') / 'input.txt'
output_file = Path('data') / 'output.txt'

# Ensure the directory exists
output_file.parent.mkdir(parents=True, exist_ok=True)

# Read the input file and write to the output file
if input_file.exists():
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            outfile.write(line.upper())  # Example: Write uppercase content
else:
    print(f"File {input_file} not found.")

# List all text files in the directory
txt_files = glob.glob(str(Path('data') / '*.txt'))
print("Text files in the 'data' directory:", txt_files)

```

**Summary**

   - Use open() with appropriate modes for reading, writing, or appending files.
   - Always specify encoding='utf-8' for cross-platform compatibility.
   - Use with for safer file handling.
   - Utilize os or pathlib for platform-independent paths.
   - Use glob for listing files matching patterns.


> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦

# Python classes:

A class is a blueprint for creating objects. Objects are instances of classes, and each object can have attributes (variables) and methods (functions defined in the class).

Think of a class as a recipe for making a cake. The class defines the ingredients and steps, but you can make multiple cakes (objects) based on that recipe, each with its own specific details (like flavor, size, etc.).


## **Creating a Basic Class in Python**
Let's say we're creating a class for a simple concept: a Dog. Each Dog object we create could have attributes like name and age.

Here’s what a basic class might look like in Python:

```python
class Dog:
    pass

```

This code defines an empty class called Dog. The pass statement tells Python to do nothing – it's a placeholder, so we don't get an error.


## **Adding the __init__ Method**

The __init__ method is a special method in Python that is called automatically every time a new object is created. It’s often referred to as the "initializer" or "constructor" of the class. This method is where we set up the initial values of our object's attributes.

Let's update our Dog class to include some attributes: name and age.


```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

```

Here’s what’s happening:

   - def __init__(self, name, age): defines the __init__ method.
   - self represents the instance of the class (the specific Dog object we’re creating).
   - self.name = name sets the name attribute for the object, and self.age = age sets the age attribute.


**Using self**

self is a reference to the current instance of the class. It lets you access the instance’s attributes and methods from within the class.

When you call a method on an object, Python automatically passes the object as the first argument, which we call self. You don’t have to explicitly pass it; Python does it for you.


## **Adding a Method to Our Class**

Now, let’s add a simple method to make our dog "speak."

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} says woof!")

```

  - speak is a method, just like a function, but it’s defined within a class.
  - self is used as the first parameter, allowing the method to access the object's attributes.


## Creating an Object (Instance) of the Class

To create an object, we call the class like a function, passing in any required arguments. Let’s make a dog named “Buddy” who is 3 years old.

```python
my_dog = Dog("Buddy", 3)

```

Here’s what happens:

   - Dog("Buddy", 3) calls the __init__ method.
   - Inside __init__, self.name is set to "Buddy", and self.age is set to 3.

Now my_dog is an instance of Dog with its own unique name and age.

**Using the Object’s Methods and Attributes**

Once we have an object, we can access its attributes and call its methods.

```python
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 3
my_dog.speak()      # Output: Buddy says woof!
```

## **Full Example Code**

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f"{self.year} {self.make} {self.model}"

    def start_engine(self):
        print(f"The engine of the {self.model} is now running.")

# Creating a Car object
my_car = Car("Toyota", "Camry", 2021)

# Accessing attributes and calling methods
print(my_car.description())  # Output: 2021 Toyota Camry
my_car.start_engine()        # Output: The engine of the Camry is now running.

```



## ✅ So when to use what?

| Use a **function** when...                                      | Use a **class** when...                                                          |
| --------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| You just need a simple task (like add numbers, print something) | You’re dealing with things (like dogs, cars, games) that have **data + actions** |
| The code is small and focused                                   | You want to create **many similar things** with their own data                   |
| You don’t need to remember state between calls                  | You want each object to **remember its own info**                                |



## 💡 What is Inheritance?

Inheritance means you can create a new class (child) that inherits things from an existing class (parent), and then add or change whatever you want.

Think of it like this:

   - You have a basic Dog class 🐶
   - You want to make a PoliceDog 🚓🐶 that is still a dog, but can also sniff for danger
   - Instead of rewriting all the dog stuff again, you reuse it and add new powers


**✅ Full Working Example**

```python
# Parent class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says: Woof!")

    def sit(self):
        print(f"{self.name} sits down.")

# Child class that inherits from Dog
class PoliceDog(Dog):
    def __init__(self, name, age, badge_number):
        # Call the parent class __init__ to set name and age
        super().__init__(name, age)
        self.badge_number = badge_number

    def sniff(self):
        print(f"{self.name} is sniffing for bad guys! 👃")

    def show_badge(self):
        print(f"Officer {self.name}, Badge #{self.badge_number}")

# Using the classes
d1 = Dog("Buddy", 3)
d1.bark()
d1.sit()

print("----")

pd1 = PoliceDog("Rex", 5, 112)
pd1.bark()          # Inherited from Dog
pd1.sit()           # Inherited from Dog
pd1.sniff()         # New method in PoliceDog
pd1.show_badge()    # Another new method

```

**🧪 Output:**

```markdown
Buddy says: Woof!
Buddy sits down.
----
Rex says: Woof!
Rex sits down.
Rex is sniffing for bad guys! 👃
Officer Rex, Badge #112

```

## Example: Supply inputs to both Parent Class 1 and Parent Class 2

```python
# Parent class 1
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Dog initialized: {self.name}, Age: {self.age}")

    def bark(self):
        print(f"{self.name} says: Woof!")

    def sit(self):
        print(f"{self.name} sits down.")

# Parent class 2
class Tracker:
    def __init__(self, tracking_level):
        self.tracking_level = tracking_level
        print(f"Tracker initialized with level {self.tracking_level}")

    def track(self):
        print("Tracking the scent trail... 🐾")

    def scan_area(self):
        print("Scanning the area for clues. 🔍")

# Child class
class PoliceDog(Dog, Tracker):
    def __init__(self, name, age, badge_number, tracking_level):
        Dog.__init__(self, name, age)  # Call Dog's constructor
        Tracker.__init__(self, tracking_level)  # Call Tracker's constructor
        self.badge_number = badge_number
        print(f"PoliceDog ready: Badge #{self.badge_number}")

    def sniff(self):
        print(f"{self.name} is sniffing for bad guys! 👃")

    def show_badge(self):
        print(f"Officer {self.name}, Badge #{self.badge_number}")

```


**🐾 Using the class:**

```python
pd = PoliceDog("Rex", 5, 112, "Expert")

pd.bark()        # From Dog
pd.sit()         # From Dog
pd.sniff()       # From PoliceDog
pd.show_badge()  # From PoliceDog
pd.track()       # From Tracker
pd.scan_area()   # From Tracker

```

**🧪 Output:**

```python
Dog initialized: Rex, Age: 5
Tracker initialized with level Expert
PoliceDog ready: Badge #112
Rex says: Woof!
Rex sits down.
Rex is sniffing for bad guys! 👃
Officer Rex, Badge #112
Tracking the scent trail... 🐾
Scanning the area for clues. 🔍

```




> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦

# Pickling Python objects and converting to JSON:

## What is Pickling?

Pickling is a way to serialize (convert) a Python object into a binary format so that it can be saved to a file and later reloaded. This is especially useful when you want to save complex objects like lists, dictionaries, or instances of classes to a file.


**Why Use Pickling?**

   - Efficiency: Pickling is faster than converting objects to text formats like JSON for saving.
   - Flexibility: It can handle many Python-specific types, including objects of custom classes.


## Basics of Pickling in Python

The pickle module is built into Python, and it provides methods to serialize and deserialize objects.

**Steps for Pickling:**

   - Serialize an object: Save it to a file.
   - Deserialize an object: Load it back into memory.


## Example: Pickling a Python Object

1. Create a Class
Here’s an example of a class that we’ll pickle.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

```

2. Pickle an Object
Here’s how to save an instance of the Person class to a pickle file.


```python
import pickle

# Create an instance of the class
person = Person("Alice", 30)

# Open a file in binary write mode
with open("person.pkl", "wb") as file:
    pickle.dump(person, file)  # Serialize and write to file

print("Object pickled successfully.")

```

3. Unpickle the Object
Here’s how to read the object back.

```python
# Open the file in binary read mode
with open("person.pkl", "rb") as file:
    loaded_person = pickle.load(file)  # Deserialize and load

print("Loaded object:", loaded_person)

```

## JSON Serialization: An Alternative

The json module can serialize Python objects to text. However, it only works with basic data types: lists, dictionaries, strings, numbers, and None.

1. Save a Dictionary as JSON
Here’s how to save a dictionary to a JSON file.

```python
import json

# Example dictionary
data = {"name": "Alice", "age": 30, "hobbies": ["reading", "cycling"]}

# Save to a JSON file
with open("data.json", "w") as file:
    json.dump(data, file)

print("Data saved as JSON.")

```

2. Load the JSON Data
Here’s how to load it back.

```python
# Read from the JSON file
with open("data.json", "r") as file:
    loaded_data = json.load(file)

print("Loaded JSON data:", loaded_data)

```

3. Convert JSON String to Python Object
If you’re working with JSON strings instead of files, use json.dumps() and json.loads().

```python
# Convert Python object to JSON string
json_string = json.dumps(data)
print("JSON String:", json_string)

# Convert JSON string back to Python object
python_obj = json.loads(json_string)
print("Python Object:", python_obj)

```

## Comparing Pickling and JSON

| **Feature**        | **Pickle**                              | **JSON**                                     |
| ------------------ | --------------------------------------- | -------------------------------------------- |
| **Format**         | Binary                                  | Text                                         |
| **Human-readable** | No                                      | Yes                                          |
| **Speed**          | Faster                                  | Slower                                       |
| **Compatibility**  | Python-specific                         | Language-independent                         |
| **Custom objects** | Yes, supports any Python object         | Limited to basic types like dict, list, etc. |
| **Use cases**      | Saving Python-specific data efficiently | Sharing data across languages                |


## Summary Code Comparison

```python
# Pickling example
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)  # Save as binary

with open("data.pkl", "rb") as f:
    loaded_data = pickle.load(f)  # Load from binary
print("Pickle Loaded:", loaded_data)

# JSON example
with open("data.json", "w") as f:
    json.dump(data, f)  # Save as JSON

with open("data.json", "r") as f:
    loaded_data = json.load(f)  # Load from JSON
print("JSON Loaded:", loaded_data)

```

## Key Takeaways

   - Pickle is great for Python-specific tasks where speed and flexibility matter.
   - JSON is better for interoperability and human readability.
   - Use pickle for saving objects locally and json for sharing data with other systems or languages.




> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦

# Vibe coding and debugging

"Vibe coding" is the affectionate term for coding with the assistance of LLMs. It's particularly easy and wonderful to do with Cursor! But there are some good techniques to make it work well, which I cover on the course. Here are a few essential tips:

## 1. Include the current date and ask for latest APIs
   
 If you're prompting an LLM like ChatGPT or Claude to write code, include the current date in your prompt, and instruct the LLM to generate code that uses the latest versions of APIs. This is particularly important with the OpenAI API! ChatGPT frequently tries to use outdated versions of its own API...


**Prompt:**

> "Today is July 20, 2025. Please write a Python script that uses the latest version of the OpenAI API to generate a completion from a prompt. Keep it simple."

**Why it works:**

This ensures the model uses the most up-to-date API version (like openai.ChatCompletion.create() with gpt-4o) rather than outdated ones.


## 2. Ask for short and simple code

Also in your prompts, ask LLMs to keep their code as short and simple as possible. LLMs seem to love to add lots of extra, unnecessary checks that clutters code and makes it hard to find problems.

**Prompt:**

> "Write the shortest possible Python function to count the number of words in a given string. Avoid extra checks or verbose logic."

**Likely output:**

```python

def word_count(s):
    return len(s.split())

```

**Why it works:**

Directs the model to avoid overengineering like checking for types or empty strings unless necessary.


## 3. Ask the same question to multiple LLMs
   
Ask the same question to multiple LLMs, and pick the answer that is clearest and simplest.
**Prompt to ChatGPT and Claude:**

> "Write a Python function that checks if a number is prime."

**Example outputs:**

- ChatGPT:

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

```

- Claude:

```python
def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))

```

**Action:**

Pick the one that's more readable and correct for your use case.


## 4. Verify with another LLM

Similar: take the answer from 1 LLM, and ask another LLM to verify it for correctness and whether it could be simpler or clearer.

**Prompt to Claude (after ChatGPT gives an answer):**

> "Can you verify if this prime-checking function from ChatGPT is correct and suggest if it can be made clearer or simpler?"

**Claude might respond:**

> "Yes, it's correct. The logic is solid. For clarity, using explicit conditionals might help less experienced readers."



## 5. Ask for 3 variations

Ask an LLM to give you 3 variations for ways to solve a problem, and pick the one that is clearest.


**Prompt:**

> "Give me 3 different ways to reverse a string in Python."

**Output:**

```python
# Method 1: Slice
def reverse1(s):
    return s[::-1]

# Method 2: Built-in reversed()
def reverse2(s):
    return ''.join(reversed(s))

# Method 3: Manual loop
def reverse3(s):
    res = ''
    for ch in s:
        res = ch + res
    return res

```

**Action:**

Pick the version you or your team finds easiest to read/maintain.


# Vibe Coding for a larger project

Try to avoid having an LLM generate 100-200 lines of code or more; it will be so hard for you to debug and figure out what's going wrong (unless you're already knowledgable).

Instead: start by breaking down your problem into small, independently testable steps, that are each relatively small. If you're not sure how to break down your problem - this is something you can ask the LLM to do!

Then for each of these building blocks:

  - Use the tips above to have the LLM build the code
  - Also have the LLM write tests to test and verify the code
  - Test it yourself and satisfy yourself that it's working correctly
  - 
This will allow you to build a larger project with confidence.



> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦

# Exceptions, Stack Traces, Exception Handling and more

📘 Python Exception Handling — A Comprehensive Tutorial
For technical students working in Python notebooks or modules, using uv for package management, and developing in Cursor (Windows or Mac)

## Part 1: 🚨 What is an Exception?

In Python, an exception is an error that occurs during execution. When Python encounters an unexpected condition (like trying to divide by zero or access a missing file), it raises an exception to alert the programmer.

You can manually raise an exception like this:


```python
raise ValueError("This is an example exception")

```
When this code runs, Python halts execution in that cell and prints a stack trace explaining what went wrong. You’ve just experienced the basics of how Python communicates errors.



## Part 2: 🧯 Handling Exceptions with try / except / finally
Python gives you tools to handle exceptions so your program doesn't crash. This is called exception handling.

**Syntax Overview**

```python
try:
    # Code that may raise an error
    ...
except SomeException:
    # Code that runs if the exception occurs
    ...
finally:
    # Code that runs no matter what
    ...

```

**Example: Handling Division Errors**

```python
try:
    x = 5 / 0
except ZeroDivisionError:
    print("You can't divide by zero.")
finally:
    print("This code runs no matter what.")

```

💡 finally is commonly used for cleanup (e.g., closing files, closing connections).


1. Handling Multiple Exception Types

```python
try:
    number = int("not_a_number")
except ValueError:
    print("Invalid conversion.")
except TypeError:
    print("Wrong type.")

```

2. Catching All Exceptions (Cautiously)

```python
try:
    do_something()
except Exception as e:
    print(f"Error occurred: {e}")

```

Be careful with this — it can hide bugs. Use when necessary, especially for logging.


## Part 3: 🔍 Reading and Understanding Stack Traces

Let’s intentionally create a function that fails:

```python
def level_one():
    level_two()

def level_two():
    raise RuntimeError("Something failed deep down.")

level_one()

```

This produces a stack trace like:

```python
Traceback (most recent call last):
  File "<stdin>", line 7, in <module>
    level_one()
  File "<stdin>", line 2, in level_one
    level_two()
  File "<stdin>", line 5, in level_two
    raise RuntimeError("Something failed deep down.")
RuntimeError: Something failed deep down.


```

**📌 How to read it:**

   - Start at the bottom: the type and message of the exception.
   - Move up to see where the error originated and how the code got there.
   - Each frame tells you the file, line number, and function.

🛠 Tip: In Cursor and many IDEs, clicking the file and line in the trace jumps you directly to the error.


## Part 4: 💣 Common Exceptions and How to Debug Them

1. ZeroDivisionError

```python
a = 10 / 0

```

**Output:**

```python
ZeroDivisionError: division by zero

```
🛠 Fix: Add checks to prevent dividing by zero.


2. TypeError

```python
x = "5" + 5

```

Output:

```python
TypeError: can only concatenate str (not "int") to str

```
🛠 Fix: Ensure types match (use int(), str(), etc.).

3. ValueError

```python
int("not a number")

```

Output:

```python
ValueError: invalid literal for int() with base 10: 'not a number'

```
🛠 Fix: Validate inputs before converting.


4. FileNotFoundError

```python
with open("missing.txt", "r") as f:
    data = f.read()

```

Output:

```python
FileNotFoundError: [Errno 2] No such file or directory: 'missing.txt'

```
🛠 Fix: Use pathlib or os.path to check for file existence:

```python
from pathlib import Path

if Path("missing.txt").exists():
    ...

```

5. SSL Connection Error

```python
import urllib.request

try:
    urllib.request.urlopen("https://expired.badssl.com/")
except Exception as e:
    print(e)

```

Output may include:

```python
ssl.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED]

```

🛠 Fix: For test purposes only (not secure!):

```python
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

```
🔒 Never use this in production — it disables certificate validation.


## Part 5: 🧠 Advanced Tips and Best Practices

1. Always Read the Bottom of the Stack Trace First
That's where the actual error is described.

2. Use print() or Logging for Context

```python
try:
    do_something_risky()
except Exception as e:
    print(f"Error while processing {input_data=}: {e}")

```

3. Use Debuggers (Cursor, VSCode, pdb)
Insert a breakpoint:

```python
import pdb; pdb.set_trace()

```

You can step through the code and inspect variables.

4. Inspect the Exception Object

```python
try:
    open("missing.txt")
except FileNotFoundError as e:
    print(f"Missing file: {e.filename}")

```

5. Print a Custom Stack Trace

```python
import traceback

try:
    risky_thing()
except Exception:
    traceback.print_exc()

```

Useful when logging errors in modules or services.

6. Clean Up with finally

```python
f = open("file.txt")
try:
    # work with file
    ...
finally:
    f.close()

```

Or use context managers (preferred):

```python
with open("file.txt") as f:
    ...

```

7. Write Custom Exceptions

```python
class InvalidDataError(Exception):
    pass

raise InvalidDataError("This data is not valid for processing.")

```

Use them in your own modules to clearly describe issues.


> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦

# Ollama: Free alternative to Paid APIs (but please see Warning about llama version)

Ollama is a product that runs locally on your machine. It can run open-source models, and it provides an API endpoint on your computer that is compatible with OpenAI.

First, download Ollama by visiting: **https://ollama.com**

Then from your Terminal in Cursor (View menu >> Terminal), run this command to download a model:

ollama pull llama3.2
WARNING: Be careful not to use llama3.3 or llama4 - these are much larger models that are not suitable for home computers.

And now, any time that we have code like:

```Python
openai = OpenAI()
```

You can use this as a direct replacement:

```Python
openai = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')
```

And also replace model names like gpt-4o-mini with llama3.2.

You don't need to put anything in your .env file for this; with Ollama, everything is running on your computer. You're not calling out to a third party on the cloud, nobody has your credit card details, so there's no need for a secret key! The code api_key='ollama' above is only required because the OpenAI client library expects an api_key to be passed in, but the value is ignored by Ollama.

Below is a full example:

```Python
# You need to do this one time on your computer
!ollama pull llama3.2

from openai import OpenAI
MODEL = "llama3.2"
openai = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

response = openai.chat.completions.create(
 model=MODEL,
 messages=[{"role": "user", "content": "What is 2 + 2?"}]
)

print(response.choices[0].message.content)

```

You will need to make similar changes to use Ollama within any of the Agent Frameworks - you should be able to google for an exact example, or ask me.


> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦

# OpenRouter: Convenient gateway platform for OpenAI and others

OpenRouter is a third party service that allows you to connect to a wide range of LLMs, including OpenAI.

It's known for having a simpler billing process that may be easier for some countries outside the US.

First, check out their website:

> https://openrouter.ai/

Then, take a peak at their quickstart:

> https://openrouter.ai/docs/quickstart

And add your key to your .env file:

```
OPENROUTER_API_KEY=sk-or....
```

And now, any time you have code like this:

```python
MODEL = "gpt-4o-mini"
openai = OpenAI()
You can replace it with code like this:

MODEL = "openai/gpt-4o-mini"
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
openai = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=openrouter_api_key)

response = openai.chat.completions.create(
 model=MODEL,
 messages=[{"role": "user", "content": "What is 2 + 2?"}]
)

print(response.choices[0].message.content)

```

You will need to make similar changes to use OpenRouter within any of the Agent Frameworks - you should be able to google for an exact example, or ask me.




> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦

# OpenAI Agents SDK - specific instructions

With OpenAI Agents SDK (weeks 2 and 6), it's particularly easy to use any model provided by OpenAI themselves. Simply pass in the model name:

```python
agent = Agent(name="Jokester", instructions="You are a joke teller", model="gpt-4o-mini")
```

You can also substitute in any other provider with an OpenAI compatible API. You do it in 3 steps like this:

```python
DEEPSEEK_BASE_URL = "https://api.deepseek.com/v1"
deepseek_client = AsyncOpenAI(base_url=DEEPSEEK_BASE_URL, api_key=deepseek_api_key)
deepseek_model = OpenAIChatCompletionsModel(model="deepseek-chat", openai_client=deepseek_client)
```

And then you simply provide this model when you create an Agent.

```python
agent = Agent(name="Jokester", instructions="You are a joke teller", model=deepseek_model)
```
And you can use a similar approach for any other OpenAI compatible API, with the same 3 steps:

```python
# extra imports
from agents import OpenAIChatCompletionsModel
from openai import AsyncOpenAI

# Step 1: specify the base URL endpoints where the provider offers an OpenAI compatible API
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
GROK_BASE_URL = "https://api.x.ai/v1"
GROQ_BASE_URL = "https://api.groq.com/openai/v1"
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
OLLAMA_BASE_URL = "http://localhost:11434/v1"

# Step 2: Create an AsyncOpenAI object for that endpoint
gemini_client = AsyncOpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)
grok_client = AsyncOpenAI(base_url=GROK_BASE_URL, api_key=grok_api_key)
groq_client = AsyncOpenAI(base_url=GROQ_BASE_URL, api_key=groq_api_key)
openrouter_client = AsyncOpenAI(base_url=OPENROUTER_BASE_URL, api_key=openrouter_api_key)
ollama_client = AsyncOpenAI(base_url=OLLAMA_BASE_URL, api_key="ollama")

# Step 3: Create a model object to provide when creating an Agent
gemini_model = OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=gemini_client)
grok_3_model = OpenAIChatCompletionsModel(model="grok-3-mini-beta", openai_client=openrouter_client)
llama3_3_model = OpenAIChatCompletionsModel(model="llama-3.3-70b-versatile", openai_client=groq_client)
grok_3_via_openrouter_model = OpenAIChatCompletionsModel(model="x-ai/grok-3-mini-beta", openai_client=openrouter_client)
llama_3_2_local_model = OpenAIChatCompletionsModel(model="llama3.2", openai_client=ollama_client)
```

## To use Azure with OpenAI Agents SDK

**See instructions here:**

https://techcommunity.microsoft.com/blog/azure-ai-services-blog/use-azure-openai-and-apim-with-the-openai-agents-sdk/4392537


Such as this:

```python
from openai import AsyncAzureOpenAI
from agents import set_default_openai_client
from dotenv import load_dotenv
import os
 
# Load environment variables
load_dotenv()
 
# Create OpenAI client using Azure OpenAI
openai_client = AsyncAzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT")
)
 
# Set the default OpenAI client for the Agents SDK
set_default_openai_client(openai_client)
```

# CrewAI setup

Here's Crew's docs for LLM connections with the model names to use for all models. As student Sadan S. pointed out (thank you!), it's worth knowing that for Google you need to use the environment variable GEMINI_API_KEY instead of GOOGLE_API_KEY:

> https://docs.crewai.com/concepts/llms

And here's their tutorial with some more info:

> https://docs.crewai.com/how-to/llm-connections


# LangGraph setup
To use LangGraph with Ollama (and follow similar for other models):
https://python.langchain.com/docs/integrations/chat/ollama/#installation

First add the package:

```
uv add langchain-ollama
```

Then in the lab, make this replacement:

from langchain_ollama import ChatOllama

```
# llm = ChatOpenAI(model="gpt-4o-mini")
llm = ChatOllama(model="gemma3:4b")
```

And obviously run **!ollama pull gemma3:4b** (or whichever model) beforehand.

Many thanks to Miroslav P. for adding this, and to Arvin F. for the question!

# LangGraph with other models

Just follow the same recipe as above, but use any of the models from here:

> https://python.langchain.com/docs/integrations/chat/


# AutoGen with other models

Here's another contribution from Miroslav P. (thank you!) for using Ollama + local models with AutoGen, and Miroslav has a great example showing gemma3 performing well.

```
# model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
 
from autogen_ext.models.ollama import OllamaChatCompletionClient


model_client = OllamaChatCompletionClient(
    model="gemma3:4b",
    model_info={
        "vision": True,
        "function_calling": False,
        "json_output": True,
        "family": "unknown",
    },
)
```

> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦


# Intermediate Level Python

## A briefing on more advanced features of Python

This section assumes you're up to speed on the foundations - and now we cover some important features of python that we use on the course.

  - Comprehensions
  - Generators
  - Sub-classes, Type Hints, Pydantic
  - Decorators
  - Docker (not really python, but we use it to run python code!)

```python
# First let's create some things:

fruits = ["Apples", "Bananas", "Pears"]

book1 = {"title": "Great Expectations", "author": "Charles Dickens"}
book2 = {"title": "Bleak House", "author": "Charles Dickens"}
book3 = {"title": "An Book By No Author"}
book4 = {"title": "Moby Dick", "author": "Herman Melville"}

books = [book1, book2, book3, book4]
```


## Part 1: List and dict comprehensions

```python
# Simple enough to start

for fruit in fruits:
    print(fruit)
```

```python
# Let's make a new version of fruits

fruits_shouted = []
for fruit in fruits:
    fruits_shouted.append(fruit.upper())

fruits_shouted
```

```python
# You probably already know this
# There's a nice Python construct called "list comprehension" that does this:

fruits_shouted2 = [fruit.upper() for fruit in fruits]
fruits_shouted2
```

```python
# But you may not know that you can do this to create dictionaries, too:

fruit_mapping = {fruit: fruit.upper() for fruit in fruits}
fruit_mapping
```

```python
# you can also use the if statement to filter the results

fruits_with_longer_names_shouted = [fruit.upper() for fruit in fruits if len(fruit)>5]
fruits_with_longer_names_shouted
```

```python
fruit_mapping_unless_starts_with_a = {fruit: fruit.upper() for fruit in fruits if not fruit.startswith('A')}
fruit_mapping_unless_starts_with_a
```

```python
# Another comprehension

[book['title'] for book in books]
```

```python
# This code will fail with an error because one of our books doesn't have an author

[book['author'] for book in books]
```

```python
# But this will work, because get() returns None

[book.get('author') for book in books]
```

```python
# And this variation will filter out the None

[book.get('author') for book in books if book.get('author')]
```

```python
# And this version will convert it into a set, removing duplicates

set([book.get('author') for book in books if book.get('author')])
```

```python
# And finally, this version is even nicer
# curly braces creates a set, so this is a set comprehension

{book.get('author') for book in books if book.get('author')}
```












```python

```

```python

```

```python

```


```python

```

> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦




```python

```

> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦




```python

```

> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦





> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦




```python

```

> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦




```python

```

> 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
