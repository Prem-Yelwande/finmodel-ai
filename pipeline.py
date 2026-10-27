"""Main processing pipeline for the financial modeling system.

This module is intended to orchestrate the agents, states, and tools
to process financial documents end-to-end.

TODO: Implement the full pipeline that chains document extraction,
agent analysis, and insight generation.
"""

from typing import Dict, Any


def run_pipeline(document_path: str) -> Dict[str, Any]:
    """Run the full analysis pipeline on a document.

    Args:
        document_path: Path to the financial document (PDF, DOCX, etc.).

    Returns:
        Dictionary containing the analysis results.

    Raises:
        NotImplementedError: Until the pipeline is fully implemented.
    """
    # Future implementation should wire together tools.py extractors,
    # states.py models, and agents.py orchestration.
    raise NotImplementedError(
        "Pipeline implementation pending. "
        "See agents.py, states.py, and tools.py for the building blocks."
    )
