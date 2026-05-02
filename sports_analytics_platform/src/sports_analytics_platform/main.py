from sports_analytics_platform.crew import SportsAnalyticsPlatform
from dotenv import load_dotenv
import agentops
import os

load_dotenv()

def run():
  
  agentops.init(os.getenv("AGENTOPS_API_KEY"))
  
  inputs = {
        "user_question": "Write a full report about everything that happened in the top 5 European leagues recently"
    }
    
  result = SportsAnalyticsPlatform().crew().kickoff(inputs=inputs)
  print(result)

  agentops.end_session("Success")

if __name__ == "__main__":
    run()