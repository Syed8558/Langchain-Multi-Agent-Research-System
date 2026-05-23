from langchain.agents import create_agent
from langchain_openrouter import OpenRouterChatModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.tools.tools import web_search ,scrape_url
from dotenv import load_dotenv


load_dotenv()

llm=OpenRouterChatModel(
    model="gpt-4o-mini",temperature=0,openrouter_api_key=os.getenv("OPENROUTER_API_KEY")
)

#1st Agent: Search Agent
def build_search_agent():
    return create_agent(
        model=llm,
        tools=[web_search],
        prompt=ChatPromptTemplate.from_messages([
            ("system", "You are a helpful research assistant."),
            
            ("human", "{input}"),
        ]),
        output_parser=StrOutputParser(),
        verbose=True


    )
#2nd Agent: Read Agent
def read_agent():
    return create_agent(
        model=llm,
        tools=[scrape_url],
        prompt=ChatPromptTemplate.from_messages([
            ("system", "You are a helpful research assistant."),
            
            ("human", "{input}"),
        ]),
        output_parser=StrOutputParser(),
        verbose=True


    )

