from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo


web_search_agent= Agent(
    name="Web search Agent",
    role='Search Web for information',
    model=Groq(id="llama-3.1-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources and links"],
    show_tools_calls=True,
    markdown=True
)


#Finance agent

finance_agent= Agent(
    name='Finance guidance agent',
    model='llama-3.1-70b-versatile',
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    instructions= ['Use Tables to showcase data'],
    show_tools_calls=True,
    markdown=True
)

#Multi Ai Agent

multi_ai= Agent(
    team= [web_search_agent,finance_agent],
    instructions=['Always include source and links','Use tables to showcase data'],
    show_tools_calls=True,
    markdown=True
)

multi_ai.print_response('Summarize analyst recommendations and share latest news for NVDA',steam=True)