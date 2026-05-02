import requests
import os
from crewai.tools import tool
from dotenv import load_dotenv

load_dotenv()

FOOTBALL_API_KEY = os.getenv("FOOTBALL_API_KEY")
BASE_URL = "https://api.football-data.org/v4"

HEADERS = {
    "X-Auth-Token": FOOTBALL_API_KEY
}


@tool("Search Competition Standings")
def get_standings(competition_code: str) -> dict:
    """
    Get the current standings for a football competition.
    competition_code examples: PL, PD, SA, BL1, FL1, CL
    """
    url = f"{BASE_URL}/competitions/{competition_code}/standings"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        table = data["standings"][0]["table"]
        simplified = []
        for t in table[:10]:
            simplified.append({
                "position": t["position"],
                "team": t["team"]["name"],
                "points": t["points"],
                "played": t["playedGames"],
                "won": t["won"],
                "draw": t["draw"],
                "lost": t["lost"],
                "gf": t["goalsFor"],
                "ga": t["goalsAgainst"]
            })
        return {"competition": competition_code, "standings": simplified}
    return {"error": f"Failed: {response.status_code}"}

@tool("Search Team Info")
def get_team_info(team_id: int) -> dict:
    """
    Get detailed information about a football team by its ID.
    """
    url = f"{BASE_URL}/teams/{team_id}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    return {"error": f"Failed to fetch team info: {response.status_code}"}


@tool("Search Team Matches")
def get_team_matches(team_id: int) -> dict:
    """
    Get recent and upcoming matches for a specific team by its ID.
    """
    url = f"{BASE_URL}/teams/{team_id}/matches?status=FINISHED&limit=10"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    return {"error": f"Failed to fetch team matches: {response.status_code}"}


@tool("Search Match Details")
def get_match_details(match_id: int) -> dict:
    """
    Get detailed information about a specific match by its ID.
    """
    url = f"{BASE_URL}/matches/{match_id}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    return {"error": f"Failed to fetch match details: {response.status_code}"}


@tool("Search Top Scorers")
def get_top_scorers(competition_code: str) -> dict:
    """
    Get the top scorers for a football competition.
    competition_code examples: PL, PD, SA, BL1, FL1, CL
    """
    url = f"{BASE_URL}/competitions/{competition_code}/scorers?limit=5"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        scorers = []
        for s in data.get("scorers", []):
            scorers.append({
                "name": s["player"]["name"],
                "team": s["team"]["name"],
                "goals": s["goals"],
                "assists": s["assists"],
                "penalties": s["penalties"],
                "played": s["playedMatches"]
            })
        return {"competition": competition_code, "scorers": scorers}
    return {"error": f"Failed: {response.status_code}"}


@tool("Search Competition Matches")
def get_competition_matches(competition_code: str) -> dict:
    """
    Get recent matches for a specific competition.
    competition_code examples: PL, PD, SA, BL1, FL1, CL
    """
    url = f"{BASE_URL}/competitions/{competition_code}/matches?status=FINISHED&limit=10"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    return {"error": f"Failed to fetch competition matches: {response.status_code}"}


@tool("Search Teams in Competition")
def get_teams_in_competition(competition_code: str) -> dict:
    """
    Get all teams participating in a specific competition.
    competition_code examples: PL, PD, SA, BL1, FL1, CL
    """
    url = f"{BASE_URL}/competitions/{competition_code}/teams"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    return {"error": f"Failed to fetch teams: {response.status_code}"}