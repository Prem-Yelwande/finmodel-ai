# finmodel-ai

AI-powered financial modeling and analysis pipeline.

## Overview
Multi-agent system for processing financial documents (e.g. 10-K filings) and generating insights.

**Note:** Full agent functionality requires API keys for the underlying LLMs. The agents use Groq (for analysis) and Mistral (for document extraction). Set `GROQ_API_KEY` and `MISTRA_AI_API_KEY` via environment variables (see agents.py). Without valid keys the agents will fail at runtime.

## Features
- Agent-based architecture
- Document processing pipeline
- State management and tools for financial analysis

## Getting Started
Recommended: Python 3.11+

```bash
uv sync
# Optional: create a .env file with your LLM keys, for example:
# GROQ_API_KEY=gsk-...
# MISTRA_AI_API_KEY=...
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

## Environment Variables
- `GROQ_API_KEY` is required for the financial analysis agent.
- `MISTRA_AI_API_KEY` is required for the document extraction agent. (Note: the variable name uses "MISTRA" as defined in agents.py; it is the key for the Mistral API.)
- Document paths and other settings can be passed programmatically or via the pipeline once implemented.
- **Security:** Never commit API keys to the repository. Use a `.env` file (add it to `.gitignore`) and load via `python-dotenv` or similar. Example `.env` is not included to avoid accidental key exposure.

## Next Steps
- Implement the orchestration logic in `pipeline.py` to connect agents, states, and tools.
- Add tests for document extraction and agent responses.
- Extend tools for additional financial data sources if needed.
- Consider pinning dependencies more tightly in `pyproject.toml` for reproducible builds.
- Add type hints across modules for better maintainability.
- Document required environment variables more fully (sample `.env.example`).
- Add robust error handling for missing API keys or invalid documents.

Updated: 2026-11-26
