from sports_analytics_platform.crew import SportsAnalyticsPlatform


def run():
    inputs = {
        "user_question": "Write a full report about everything that happened in the top 5 European leagues recently"
    }
    
    result = SportsAnalyticsPlatform().crew().kickoff(inputs=inputs)
    print(result)


if __name__ == "__main__":
    run()