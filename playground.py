from phi.agent import Agent
from phi.model.groq import Groq
import phi.api
import dotenv
import phi
import os
from dotenv import load_dotenv

from phi.playground import Playground, serve_playground_app
#TO load environment variables from .env file
load_dotenv()

phi.api= os.getenv("PHI_API_KEY")

research_agent=Agent(
    name='research Agent for arxiv documents parsing',
    model=Groq(id="llama-3.1-70b-versatile"),
    instructions=["Cross refer most frequent topics and methodology","Provide links to sources with most prominent topics and look for lesser explored methodologythose can implement."],
    show_tools_calls=True,
    markdown=True
)

app=Playground(agents=[research_agent]).get_app()

if __name__=="__main__":
    serve_playground_app("playground:app")