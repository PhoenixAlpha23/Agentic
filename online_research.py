from phi.agent import Agent
from phi.tools.arxiv_toolkit import ArxivToolkit
from phi.model.groq import Groq
from phi.tools.googlesearch import GoogleSearch

import phi
import phi.api
import dotenv
import os
from dotenv import load_dotenv

#TO load environment variables from .env file
load_dotenv()

phi.api= os.getenv("OPENAI_API_KEY")
#Arxiv Agent
research_agent=Agent(
    name='research Agent for arxiv documents',
    model=Groq(id="llama-3.1-70b-versatile"),
    instructions=["Cross refer most frequent topics and methodology","Provide links to sources with most prominent topics and look for lesser explored methodologythose can implement."],
    show_tools_calls=True,
    markdown=True
)

web_agent= Agent(
    name='Web search Agent',
    tools=[GoogleSearch()],
    model=Groq(id="llama-3.1-70b-versatile"),
    instructions=[
        "Search for research papers on google scholar, semantic scholar, ieeexplore and paperswithcode.com",
        "Pick topics with least common approaches/methodologies among them, with great potential",
        "Pick methodologes with have potential to improve results or have a innovative approach",
        "reccommend topics for research with methodology"
    ],
    debug_mode= True,
    show_tool_calls=True,
    markdown=True
)



multi_agent= Agent(
    team= [research_agent,web_agent],
    instructions= ["Analyse and give sources for each method you mention","Analyse the methodolgy and give sources for it, and the recent trends in the relevatn domain and include some prospective topics as well"]
)
#agent = Agent(tools=[ArxivToolkit()], show_tool_calls=True)
#research_agent.print_response("Search arxiv for 'Optical Character Recognition','Big data' and 'LLMs", markdown=True)

web_agent.print_response("Search for research topics in OCR and LLM combination papers",markdown=True)