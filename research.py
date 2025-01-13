from phi.agent import Agent
from phi.tools.arxiv_toolkit import ArxivToolkit
from phi.model.groq import Groq

research_agent=Agent(
    name='research Agent for arxiv documents',
    model=Groq(id="llama-3.1-70b-versatile"),
    instructions=["Cross refer most frequent topics and methodology","Provide links to sources with most prominent topics and look for lesser explored methodologythose can implement."],
    show_tools_calls=True,
    markdown=True
)

#agent = Agent(tools=[ArxivToolkit()], show_tool_calls=True)
research_agent.print_response("Search arxiv for 'Optical Character Recognition' and 'LLMs", markdown=True)