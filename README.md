# finmodel-ai

AI-powered financial modeling and analysis pipeline.

## Overview
Multi-agent system for processing financial documents (e.g. 10-K filings) and generating insights.

**Note:** Full agent functionality requires an API key for the underlying LLM (e.g. OpenAI). Set it via environment variables as used in the tools/agents modules.

## Features
- Agent-based architecture
- Document processing pipeline
- State management and tools for financial analysis

## Getting Started
```bash
uv sync
# Optional: create a .env file with your LLM key, for example:
# OPENAI_API_KEY=sk-...
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
- `OPENAI_API_KEY` (or the key expected by the configured LLM provider) is required for agent calls.
- Document paths and other settings can be passed programmatically or via the pipeline once implemented.

## Next Steps
- Implement the orchestration logic in `pipeline.py` to connect agents, states, and tools.
- Add tests for document extraction and agent responses.
- Extend tools for additional financial data sources if needed.
- Consider pinning dependencies more tightly in `pyproject.toml` for reproducible builds.
- Add type hints across modules for better maintainability.
- Document required environment variables more fully (sample `.env.example`).
- Add robust error handling for missing API keys or invalid documents.

Updated: 2026-11-10
