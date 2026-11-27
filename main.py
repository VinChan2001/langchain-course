import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient


load_dotenv()

tavily_client = TavilyClient()

@tool
def search(query: str) -> str:
    """
    Tool that searches over the internet 

    Args:
        query: The query to search for 

    Returns:
        The search results
    """
    print(f"Searching for: {query}")
    result = tavily_client.search(query=query)
    return result


llm = ChatOpenAI(model="gpt-4o-mini")
tools = [search]
agent = create_agent(model=llm, tools=tools)

def main():
    result = agent.invoke({"messages": [HumanMessage(content="List 3 job posting for langchain engineers in the bay area on linkedin and their details")]})
    print(result)

if __name__ == "__main__":
    main()
