import os

from smolagents import CodeAgent, LiteLLMModel, tool

@tool
def search_docs(query: str) -> str:
    """TODO: write a one-line description of what this tool does.

    Args:
        query: TODO: describe this argument.
    """
    # TODO: return something based on `query`.
    # For a first run, a hardcoded dict of fake "search results" is fine.
    ...


# TODO: build the model.
# LiteLLMModel(model_id="deepseek/deepseek-chat", api_key=...)
# The key is in os.environ["DEEPSEEK_API_KEY"].
model = ...

# TODO: build the agent. Hand it your tool(s) and the model.
agent = ...

# TODO: ask it something that actually requires calling search_docs.
result = agent.run("...")

print("\n==== FINAL ANSWER ====")
print(result)