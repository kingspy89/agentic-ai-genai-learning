import os
from dotenv import load_dotenv
load_dotenv()

from langchain.tools import tool
from typing import Dict, Any
from tavily import TavilyClient
from langgraph.checkpoint.memory import InMemorySaver   
from langchain.agents import create_agent
from langchain.messages import HumanMessage

tavily_client = TavilyClient()

@tool
def web_search(query: str) -> Dict[str, Any]:

    """Search the web for information"""

    return tavily_client.search(query)

# creating agent

agent = create_agent(
    model="groq:qwen/qwen3-32b",
      tools=[web_search],
    system_prompt = """

You are a personal chef. The user will give you a list of ingredients they have left over in their house.

Using the web search tool, search the web for recipes that can be made with the ingredients they have.

Return recipe suggestions and eventually the recipe instructions to the user, if requested.

"""
)

if __name__ == "__main__":
    question = HumanMessage(content="i have panner and other vegs like palak  what can i make from it ?")
    config = {"configurable": {"thread_id": "1"}}

    response = agent.invoke(
        {"messages": [question]},
        config,  
    )

    print(response['messages'][-1].content.split('</think>')[-1].strip())

    question = HumanMessage(content="i dont have tomato !!")

    response = agent.invoke(
        {"messages": [question]},
        config,  
    )

    print(response['messages'][-1].content)




