"""Placeholder entry point for the finmodel-ai project.

Core agent logic, state models, and tools live in:
- agents.py
- states.py
- tools.py
- prompts.py

See README.md for the project overview and getting started instructions.
The main processing pipeline is still to be implemented in pipeline.py.

Usage:
    python main.py

Next steps:
    1. Review and refine prompts in prompts.py
    2. Implement end-to-end flow in pipeline.py
    3. Add unit tests for document extraction tools
    4. Set required LLM API keys via environment variables (see tools/agents)
"""


def main() -> None:
    """Print project overview and module locations."""
    print("finmodel-ai — AI-powered financial modeling & analysis pipeline")
    print("Placeholder entry point. Core logic lives in the agent modules.")
    print("  agents.py   — agent definitions and orchestration")
    print("  states.py   — shared state models")
    print("  tools.py    — document extraction tools (PDF, DOCX, CSV, Excel)")
    print("  prompts.py  — prompt templates")
    print("  pipeline.py — (coming soon) end-to-end analysis flow")
    print()
    print("Suggested next steps:")
    print("  - Finalize extraction tools and add error handling")
    print("  - Wire agents into a LangGraph or sequential pipeline")
    print("  - Add sample input documents and expected outputs for testing")
    print("  - Ensure LLM API keys are set in the environment before running agents")
    print("See README.md for setup, dependencies, and more details.")


if __name__ == "__main__":
    main()
