# Financial Researcher Agent System

A multi-agent AI system powered by CrewAI that conducts comprehensive financial research on companies and generates professional reports. This project demonstrates how multiple AI agents can work together to gather, analyze, and present financial information automatically.

## Project Overview

The system has two AI agents: a Researcher (gathers company data via web search) and a Reporting Analyst (creates professional reports). It automates research and report generation using Google Gemini 2.0 Flash.

## Key Features

- Two specialized agents with distinct roles and responsibilities
- Automated web-based research gathering
- Professional report generation in markdown format
- Sequential task processing (research first, then analysis)
- Output files saved to the output/ directory
- Real-time verbose logging of agent activities

## Project Structure

```
financial_researcher/
├── src/financial_researcher/
│   ├── __init__.py
│   ├── main.py                    - Entry point and execution logic
│   ├── crew.py                    - Crew structure with agents and tasks
│   ├── config/
│   │   ├── agents.yaml            - Agent configurations and roles
│   │   └── tasks.yaml             - Task definitions
│   └── tools/
│       ├── __init__.py
│       └── custom_tool.py         - Custom tool template
├── knowledge/
│   └── user_preference.txt        - User preferences
├── tests/                         - Test directory
├── output/                        - Generated reports directory
├── pyproject.toml                 - Project dependencies
├── AGENTS.md                      - CrewAI reference guide
├── README.md                      - This file
├── .env.example                   - Environment variables template
└── uv.lock                        - Locked dependencies
```

## Requirements

- Python 3.10 or higher (less than 3.14)
- UV package manager
- Google Gemini API key
- SerperDev API key for web search

## Installation

Step 1: Install UV package manager
```
pip install uv
```

Step 2: Install project dependencies
```
crewai install
```

Or use:
```
uv sync
```

Step 3: Create .env file with your API keys
```
GOOGLE_API_KEY=your_google_gemini_api_key
SERPER_API_KEY=your_serper_dev_api_key
```

See .env.example for all required variables.

## How to Run

Execute the financial research system:
```
crewai run
```

This command will:
1. Initialize the FinancialResearcher crew
2. Activate the researcher and reporting analyst agents
3. Execute tasks in order (research then report generation)
4. Generate a markdown report in output/report.md

By default, the system researches Tesla. To change the company, edit src/financial_researcher/main.py and modify the company name in the inputs section.
