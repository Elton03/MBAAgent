from crewai import Agent
from tools import DuckDuckGoSearchTool

def create_mba_advisor():
    return Agent(
        role="MBA School Advisor",
        goal="Help students with any question about MBA programs",
        backstory="Expert in MBA rankings, specializations, costs, and outcomes.",
        tools=[DuckDuckGoSearchTool()],
        verbose=True
    )
