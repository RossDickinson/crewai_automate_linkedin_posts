from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class ContentCrew:
    """Content crew for creating LinkedIn posts"""
    
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def linkedin_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["linkedin_writer"],
            verbose=True
        )

    @task
    def write_post(self) -> Task:
        return Task(
            config=self.tasks_config["write_post"]
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.linkedin_writer()],
            tasks=[self.write_post()],
            process=Process.sequential,
            verbose=True
        )