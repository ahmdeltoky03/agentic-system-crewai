# Coder Agent System

A multi-agent AI system powered by CrewAI that generates professional Python code to solve specific problems. This project demonstrates how AI agents can intelligently analyze requirements and produce clean, well-organized, production-ready code automatically.

## Project Overview

The system has a specialized Coder Agent that analyzes problem statements and generates comprehensive Python solutions. It automates code generation and explanation using OpenAI's GPT models.

## Key Features

- Specialized coder agent with deep programming expertise
- Automatic Python code generation for complex problems
- Well-organized and documented code output
- Detailed explanations and implementation logic
- Output files saved to the output/ directory
- Real-time verbose logging of agent activities

## Project Structure

```
coder/
├── src/coder/
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
├── output/                        - Generated code directory
├── pyproject.toml                 - Project dependencies
├── AGENTS.md                      - CrewAI reference guide
├── README.md                      - This file
├── .env.example                   - Environment variables template
└── uv.lock                        - Locked dependencies
```

## Requirements

- Python 3.10 or higher (less than 3.14)
- UV package manager
- OpenAI API key

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
OPENAI_API_KEY=your_openai_api_key
```

See .env.example for all required variables.

## How to Run

Execute the coder system:
```
crewai run
```

This command will:
1. Initialize the Coder crew
2. Activate the coder agent
3. Execute the coding task based on the problem input
4. Generate Python code and explanation in output/code_and_output.md

By default, the system generates code to explain recursion in programming. To change the problem, edit `src/coder/main.py` and modify the problem statement in the inputs section.

## Customization

To customize the coder agent system:

- Modify `src/coder/config/agents.yaml` to change agent role, goal, and backstory
- Modify `src/coder/config/tasks.yaml` to define the coding task parameters
- Modify `src/coder/crew.py` to add custom tools and logic
- Modify `src/coder/main.py` to provide different problem inputs
