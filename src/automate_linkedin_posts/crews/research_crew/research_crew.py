from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

@CrewBase
class ResearchCrew:
    """Research crew for gathering topic information"""
    
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def trend_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["trend_analyst"],
            tools=[SerperDevTool()],
        )

    @agent
    def data_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["data_researcher"],
            tools=[SerperDevTool()],
        )

    @agent 
    def competitor_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["competitor_analyst"],
            tools=[SerperDevTool()],
        )

    @task
    def analyze_trends(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_trends"]
        )

    @task
    def gather_data(self) -> Task:
        return Task(
            config=self.tasks_config["gather_data"]
        )

    @task
    def analyze_competitor_content(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_competitor_content"]
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[
                self.trend_analyst(),
                self.data_researcher(),
                self.competitor_analyst()
            ],
            tasks=[
                self.analyze_trends(),
                self.gather_data(),
                self.analyze_competitor_content()
            ],
            process=Process.sequential,
            verbose=True
        )