from langchain import hub
from langchain.agents import AgentExecutor, create_openai_tools_agent, tool
from langchain.callbacks.tracers import ConsoleCallbackHandler

from genosclient.langchain_plugin import jsguruGenAIChatV2


@tool
def multiply_special(a: int, b: int) -> int:
    """Multiply two numbers specially."""
    return a * b + 23


@tool
def get_weather() -> str:
    """Get the current weather"""
    return "35.555 degrees"


def langchain_function_calling():
    chat = jsguruGenAIChatV2(
        temperature=0,
        metadata={
            "experience_id": EXPERIENCE_ID,
        },
        model_name="gpt-4-1106",
        callbacks=[ConsoleCallbackHandler()],
    )

    # Get the prompt to use - you can modify this!
    prompt = hub.pull("hwchase17/openai-functions-agent")
    print(multiply_special.description, get_weather.description)
    tools = [get_weather]

    agent = create_openai_tools_agent(chat, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    agent_executor.invoke({"input": "what's the current weather?"})