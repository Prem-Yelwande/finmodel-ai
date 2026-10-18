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

Updated: 2026-10-18
