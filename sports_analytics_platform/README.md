# Sports Analytics Platform

A production-grade Multi-Agent AI System built with CrewAI, designed to analyze everything happening in world football using natural language questions in Arabic or English.

---

## Agents

| Agent | Role |
|---|---|
| Orchestrator | Understands natural language questions and delegates to the right agents |
| Data Collector | Fetches real-time football data from Football-Data.org API |
| Player Analyst | Analyzes player performance, statistics, and form |
| Team Analyst | Analyzes team standings, results, and tactical patterns |
| Match Analyst | Analyzes match events, key moments, and insights |
| Report Writer | Compiles all analysis into a professional structured report |

---

## Key Features

- Supports any natural language football question in Arabic or English
- Covers Premier League, La Liga, Serie A, Bundesliga, Ligue 1 and Champions League
- Real-time data via Football-Data.org API
- Outputs automatically saved as Markdown, JSON, and PDF reports
- Powered by Gemini and Groq LLMs via CrewAI
- Sequential multi-agent pipeline with full context passing between agents

---

## Installation

Ensure you have Python >=3.10 <3.14 installed. This project uses UV for dependency management.

```bash
pip install uv && crewai install && crewai run
```

---

## Configuration

Add your API keys to the .env file:

```env
GEMINI_API_KEY=your_gemini_api_key
FOOTBALL_API_KEY=your_football_data_api_key
MODEL=gemini/gemini-2.0-flash-001
```

Customize your setup:
- src/sports_analytics_platform/config/agents.yaml - Define agent roles and goals
- src/sports_analytics_platform/config/tasks.yaml - Define tasks and output files
- src/sports_analytics_platform/crew.py - Add logic, tools, and configurations
- src/sports_analytics_platform/main.py - Set your football question as input

---

## Running the Project

```bash
crewai run
```

The crew will automatically:
1. Understand your football question
2. Fetch real-time data from the API
3. Run analysis across players, teams, and matches
4. Generate a full professional report saved in outputs/reports/

---

## Output Structure

```
outputs/reports/
├── 01_understand_request.md   - Parsed question and identified entities
├── 02_collect_data.md         - Raw data fetched from Football API
├── 03_analyze_player.md       - Player performance analysis
├── 04_analyze_team.md         - Team performance analysis
├── 05_analyze_match.md        - Match analysis and insights
└── 06_final_report.md         - Complete professional analytics report
```

---

## Project Structure

```
sports_analytics_platform/
├── src/
│   └── sports_analytics_platform/
│       ├── config/
│       │   ├── agents.yaml        - Agents definitions
│       │   └── tasks.yaml         - Tasks definitions
│       ├── tools/
│       │   ├── custom_tool.py     - Football API tools
│       │   └── report_saver.py    - PDF, Markdown, JSON saver
│       ├── crew.py                - Crew setup and orchestration
│       └── main.py                - Entry point
├── outputs/
│   └── reports/                   - Generated reports
├── .env                           - API Keys
└── pyproject.toml                 - Dependencies
```

---

## Resources

- CrewAI Documentation: https://docs.crewai.com
- Football-Data.org API: https://www.football-data.org
- Google AI Studio: https://aistudio.google.com
- Groq Console: https://console.groq.com