import os                                   # read environment variables (like your API key) from your system or .env file.
import random                               # Import Random module, for generating random vacation destinations.
from typing import Annotated                # Imports Annotated from the typing module. Used for better function annotations/hints, especially with plugins in semantic_kernel.
from dotenv import load_dotenv              # load environment variables from a .env file (e.g., your API keys) into your program.

from semantic_kernel.agents import ChatCompletionAgent, ChatHistoryAgentThread  # Imports ChatCompletionAgent and ChatHistoryAgentThread from semantic_kernel.agents. These are used to create and manage AI agents that can handle chat completions and maintain conversation history.
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion          # Imports OpenAIChatCompletion from semantic_kernel.connectors.ai.open_ai. This is used to connect to OpenAI's chat completion service, allowing the agent to generate responses based on user input.
from semantic_kernel.functions import kernel_function                           # Imports kernel_function from semantic_kernel.functions. This is used to define functions that can be called by the AI agent, such as plugins that provide additional functionality.
from openai import AsyncOpenAI                                                  # Imports AsyncOpenAI from the openai module. This is used to create an asynchronous client for OpenAI's API, allowing for non-blocking calls to the AI service.



# ---- Plugins ----

class CalculatorPlugin:
    """A simple calculator plugin."""
    @kernel_function(description="Evaluates a simple math expression.")
    def calculate(self, expression: Annotated[str, "A math expression to evaluate"]) -> Annotated[str, "The result as a string."]:
        try:
            allowed_chars = set("0123456789+-*/(). ")
            if not set(expression).issubset(allowed_chars):
                return "Only basic arithmetic expressions allowed."
            result = eval(expression, {"__builtins__": {}})
            return str(result)
        except Exception as e:
            return f"Error: {str(e)}"

# ---- Load .env and set up LLM ----

load_dotenv()
client = AsyncOpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url="https://models.github.ai/inference"
)

chat_completion_service = OpenAIChatCompletion(
    ai_model_id="openai/gpt-4.1",
    async_client=client,
)

agent = ChatCompletionAgent(
    service=chat_completion_service,
    plugins=[CalculatorPlugin()], # DestinationsPlugin(), # # Add your plugin here
    name="HelperAgent",
    instructions=(
        # "You are a helpful AI Agent that can help plan vacations for customers at random destinations, "
        "you can also perform basic calculations when asked."
    ),
)

# ---- Conversation Loop ----

import asyncio

async def main():
    thread = None
    user_inputs = [
        # "Where should I go on vacation?",
        "What is 23 * (7 + 5)?",
        # "Suggest another place to travel!",
        "Can you calculate (15 + 8) / 3 for me?"
    ]
    for user_input in user_inputs:
        print(f"\n# User: {user_input}\n")
        first_chunk = True
        async for response in agent.invoke_stream(
            messages=user_input, thread=thread,
        ):
            if first_chunk:
                print(f"# {response.name}: ", end="", flush=True)
                first_chunk = False
            print(f"{response}", end="", flush=True)
            thread = response.thread
        print()
    await thread.delete() if thread else None

if __name__ == "__main__":
    asyncio.run(main())
