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

## Project Layout
- `agents.py` — agent definitions and orchestration
- `states.py` — shared state models
- `tools.py` — tools used by the agents
- `prompts.py` — prompt templates

Core logic currently lives in the agent/state/tool modules above. `main.py` is a placeholder entry point.

Updated: 2026-10-11
