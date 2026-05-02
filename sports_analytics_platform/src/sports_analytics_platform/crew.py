from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from dotenv import load_dotenv
import os

from .tools.custom_tool import (
    get_standings,
    get_team_info,
    get_team_matches,
    get_match_details,
    get_top_scorers,
    get_competition_matches,
    get_teams_in_competition
)

load_dotenv()



@CrewBase
class SportsAnalyticsPlatform:

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"


    @agent
    def Orchestrator(self) -> Agent:
        return Agent(
            config=self.agents_config["Orchestrator"],
            verbose=True
        )

    @agent
    def data_collector(self) -> Agent:
        return Agent(
            config=self.agents_config["data_collector"],
            verbose=True,
            tools=[
                get_standings,
                get_team_info,
                get_team_matches,
                get_match_details,
                get_top_scorers,
                get_competition_matches,
                get_teams_in_competition
            ]
        )

    @agent
    def player_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["player_analyst"],
            verbose=True
        )

    @agent
    def team_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["team_analyst"],
            verbose=True
        )

    @agent
    def match_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["match_analyst"],
            verbose=True
        )

    @agent
    def report_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["report_writer"],
            verbose=True
        )

    # ========== TASKS ==========

    @task
    def understand_request(self) -> Task:
        return Task(
            config=self.tasks_config["understand_request"],
        )

    @task
    def collect_data(self) -> Task:
        return Task(
            config=self.tasks_config["collect_data"],
        )

    @task
    def analyze_player(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_player"],
        )

    @task
    def analyze_team(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_team"],
        )

    @task
    def analyze_match(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_match"],
        )

    @task
    def write_report(self) -> Task:
        return Task(
            config=self.tasks_config["write_report"],
        )


    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )