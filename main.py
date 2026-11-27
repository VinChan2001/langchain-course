import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain_tavily.tavily_search import TavilySearchInput

load_dotenv()


llm = ChatOpenAI(model="gpt-4o-mini")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)

def main():
    result = agent.invoke({"messages": [HumanMessage(content="List 3 job posting for langchain engineers in the bay area on linkedin and their details")]})
    print(result)

if __name__ == "__main__":
    main()
