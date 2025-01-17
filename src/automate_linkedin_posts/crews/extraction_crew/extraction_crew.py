from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SpiderTool

@CrewBase
class ExtractionCrew:
    """Crew specialized in extracting real estate listing data"""
    
    agents_config = "config/agents.yaml"  
    tasks_config = "config/tasks.yaml"

    @agent
    def content_extractor(self) -> Agent:
        return Agent(
            config=self.agents_config["content_extractor"],
            tools=[SpiderTool()]
        )

    @task
    def extract_content(self) -> Task:
        return Task(
            config=self.tasks_config["extract_content"]
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.content_extractor()],
            tasks=[self.extract_content()],
            process=Process.sequential,
            verbose=True
        )