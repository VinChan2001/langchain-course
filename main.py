import os



from typing import List
from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from tavily import TavilyClient


class Sources(BaseModel):
    """Schema for a source used by the agent"""

    # this is a attributes
    url: str = Field(
        description="the URL of the source"
    )  # field allows us to add meta data to our attribute -- description in this case


class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""

    answer: str = Field(description="The agent's answer to the query")
    sources: List[Sources] = Field(
        default_factory=list,
        description="The list of sources used to generate the answer",
    )


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
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)


def main():
    result = agent.invoke(
        {
            "messages": [
                HumanMessage(
                    content="List 3 job posting for langchain engineers in the bay area on linkedin and their details"
                )
            ]
        }
    )
    print(result)


if __name__ == "__main__":
    main()
