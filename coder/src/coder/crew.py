from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent


@CrewBase
class Coder():
    """Coder crew"""

    agent_config = "config/agents.yaml"
    task_config = "config/tasks.yaml"

    @agent
    def coder(self) -> Agent:
        return Agent(
            config=self.agents_config['coder'],
            verbose=True,
            allow_code_execution=True,
            code_execution_mode="safe",
            max_code_execution_time=10,
            max_iteration_time=30,
        )
        
    @task
    def coding_task(self) -> Task:
        return Task(
            config=self.tasks_config['coding_task'],
            output_file='output/code_and_output.md'
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the Coder crew"""

        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            # process=Process.sequential,
            verbose=True,
        )
