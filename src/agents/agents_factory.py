from crewai import Agent
from src.tools.file_tools import read_local_file
from src.config import get_llm

class AgentsFactory:
    def __init__(self):
        self.llm = get_llm()

    def create_data_analyst(self) -> Agent:
        return Agent(
            role="Data Analyst",
            goal="Extract and analyze precise information from provided text or files. All your thoughts and final output must be in French.",
            backstory="You are an expert in data extraction and analysis. You can process raw text or read local files to find key information. You must communicate exclusively in French.",
            tools=[read_local_file],
            llm=self.llm,
            verbose=True,
            allow_delegation=False
        )

    def create_strategic_planner(self) -> Agent:
        return Agent(
            role="Strategic Planner",
            goal="Take extracted information and structure a macro-level strategic plan. All your thoughts and final output must be in French.",
            backstory="You are a senior strategist capable of turning raw data into actionable plans. You excel at organization and strategic thinking. You must communicate exclusively in French.",
            tools=[],
            llm=self.llm,
            verbose=True,
            allow_delegation=False
        )
