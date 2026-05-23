from langchain.agents import create_agent
from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.tools.tools import web_search, scrape_url
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# LLM setup
llm = ChatOpenRouter(
    model="openai/gpt-4o-mini",
    temperature=0,
    api_key=os.getenv("OPENROUTER_API_KEY")
)


# =====================================================
# 1st Agent: Search Agent
# =====================================================

def build_search_agent():
    return create_agent(
        model=llm,
        tools=[web_search],
        system_prompt="""
        You are a helpful research assistant.
        Find recent, reliable and detailed information.
        """
    )


# =====================================================
# 2nd Agent: Reader Agent
# =====================================================

def build_reader_agent():
    return create_agent(
        model=llm,
        tools=[scrape_url],
        system_prompt="""
        You are a research assistant.

        Your job:
        1. Read search results
        2. Pick relevant URLs
        3. Scrape information using tools
        4. Return summarized content
        """
    )


# =====================================================
# 3rd Agent: Writer Chain
# =====================================================

writer_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert research writer. Write clear, structured and insightful reports."
        ),

        (
            "human",
            """
Write a detailed research report on the topic below.

Topic:
{topic}

Research gathered:
{research}

Structure the report as:

- Introduction
- Key Findings (minimum 3 well explained points)
- Conclusion
- Sources (list all URLs used)

Be detailed, factual and professional.
"""
        )
    ]
)

writer_chain = writer_prompt | llm | StrOutputParser()


# =====================================================
# 4th Agent: Critic Chain
# =====================================================

critic_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a sharp and constructive research critic."
        ),

        (
            "human",
            """
Review the research report below and evaluate it strictly.

Report:
{report}

Respond exactly in this format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
...
"""
        )
    ]
)

critic_chain = critic_prompt | llm | StrOutputParser()

