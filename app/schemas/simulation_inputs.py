from pydantic import BaseModel, Field
from typing import Optional


class EmergencyFundInput(BaseModel):
    target: float = Field(
        ...,
        description="Target for the simulation, default is 'emergency_fund'"
    )
    monthly_contrib: float = Field(
        ...,
        description="Monthly contribution to the emergency fund"
    )
    current_savings: float = Field(
        ...,
        description="Current savings amount"
    )
