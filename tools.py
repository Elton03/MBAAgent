from pydantic import BaseModel, Field
from crewai.tools import BaseTool
from langchain_community.tools import DuckDuckGoSearchRun

class DuckSearchInput(BaseModel):
    query: str = Field(..., description="Search query for DuckDuckGo")

class DuckDuckGoSearchTool(BaseTool):
    name: str = "DuckDuckGo Web Search"
    description: str = "Searches the web using DuckDuckGo"
    args_schema: type[BaseModel] = DuckSearchInput

    def _run(self, query: str) -> str:
        return DuckDuckGoSearchRun().run(query)
