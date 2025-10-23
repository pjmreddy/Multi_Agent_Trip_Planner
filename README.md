# Multi Agent Trip Planner

A Python project for planning trips using multiple agents and workflows. This repository is organized into modular packages for agents, configuration, prompts, and tools.

## Features
- Modular agentic workflow
- Configurable via YAML
- Prompt library for flexible agent communication
- Extensible tools package

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/pjmreddy14/Multi_Agent_Trip_Planner.git
cd Multi_Agent_Trip_Planner
```

### 2. Set up Python environment
This project uses [uv](https://github.com/astral-sh/uv) for fast Python environment management.

Install uv (if not already installed):
```bash
pip install uv
```

Initialize the environment:
```bash
uv init Multi_Agent_Trip_Planner
```

List available Python versions:
```bash
uv python list
```

Install a specific Python version (replace <version>):
```bash
uv pip install python <version>
```

Activate the environment:
```bash
uv
```

Alternatively, you can use the provided `env/` virtual environment:
```bash
source env/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the main script
```bash
python main.py
```

## Project Structure
```
agent/            # Agentic workflow logic
config/           # Configuration files (YAML)
prompt_library/   # Prompt templates and utilities
tools/            # Helper tools
main.py           # Entry point
requirements.txt  # Python dependencies
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
MIT
