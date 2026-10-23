# finmodel-ai

AI-powered financial modeling and analysis pipeline.

## Overview
Multi-agent system for processing financial documents (e.g. 10-K filings) and generating insights.

## Features
- Agent-based architecture
- Document processing pipeline
- State management and tools for financial analysis

## Getting Started
```bash
uv sync
python main.py
```

Note: `main.py` is currently a placeholder entry point. Core logic lives in the modules listed below. Check individual modules for the actual agent implementations before running.

## Project Layout
- `agents.py` — agent definitions and orchestration
- `states.py` — shared state models
- `tools.py` — tools used by the agents (file extractors for PDF, DOCX, CSV, Excel)
- `prompts.py` — prompt templates
- `pipeline.py` — placeholder for the main processing pipeline (currently empty; implement the orchestration here)

Core logic currently lives in the agent/state/tool modules above. The empty `pipeline.py` is reserved for the end-to-end flow that wires agents, states, and tools together.

## Dependencies
Managed with [uv](https://docs.astral.sh/uv/). See `pyproject.toml` for the full list. Run `uv sync` to install everything in a virtual environment.

## Next Steps
- Implement the orchestration logic in `pipeline.py` to connect agents, states, and tools.
- Add tests for document extraction and agent responses.
- Extend tools for additional financial data sources if needed.
- Consider pinning dependencies more tightly in `pyproject.toml` for reproducible builds.
- Add type hints across modules for better maintainability.

Updated: 2026-10-23
