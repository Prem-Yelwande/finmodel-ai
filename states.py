from typing import Any
from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class FinancialData(BaseModel):
    model_config = ConfigDict(extra="allow")

    company_name: str | None = None
    reporting_period: str | None = None
    currency: str | None = None
    unit: str | None = None

    financial_statements: dict[str, Any] = Field(default_factory=dict)
    financial_metrics: dict[str, Any] = Field(default_factory=dict)
    segments: dict[str, Any] = Field(default_factory=dict)
    notes: list[str] = Field(default_factory=list)
    source_references: list[dict[str, Any]] = Field(default_factory=list)


