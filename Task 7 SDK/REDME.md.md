OpenAI Agents SDK - Task 07 Explanation

What is an SDK?

**SDK (Software Development Kit)** is a set of tools that helps developers build applications for a specific platform or service.

Example:

from openai import Agent
agent = Agent(instructions="You are a helpful assistant.")


Why is the Agent class a @dataclass?

Using `@dataclass` makes it easier to define classes that are mainly used to store data. It automatically creates the `__init__`, `__repr__`, and other useful methods.

Example:

from dataclasses import dataclass

@dataclass
class Agent:
    instructions: str
    tools: list


Why is `instructions` stored in the Agent and can be a callable (function)?

* `instructions` are system messages that tell the AI what role it should play.
* Sometimes we want these instructions to change depending on the context, so we can pass a function instead of plain text.

Static Example:

agent = Agent(instructions="You are a math tutor.")

Dynamic Example:

agent = Agent(instructions=lambda context: f"You are helping with task: {context['task']}")



Why is the user input passed to `Runner.run()` and why is it a classmethod?

* User input changes every time, so it’s passed directly to the method.
* `run()` is a classmethod so it can be used without creating an instance of `Runner`.

Example:

from openai import Runner
Runner.run(agent=agent, input="What is 2 + 2?")


What does the Runner class do?

Runner is responsible for executing the agent. It combines the agent's instructions, tools, and user input to generate a response.

Example:

Runner.run(agent=agent, input="Translate 'hello' to French")


What are Generics in Python? Why use them for TContext?

Generics allow your code to work with any type while keeping it type-safe.
`TContext` is a placeholder for the context type (e.g., dict, object).

Example:

from typing import TypeVar, Generic

TContext = TypeVar('TContext')

class Agent(Generic[TContext]):
    def __init__(self, instructions: str, context: TContext):
        self.instructions = instructions
        self.context = context