from pydantic import BaseModel
from typing import List, Dict

class SimulationInput(BaseModel):
    """
    Input data for the financial simulation
    """
    income: float
    rate: float
    goal: float
    months: int

class MathExplanationSection(BaseModel):
    """
    Explanation section for the mathematical logic used in the simulation
    """
    heading: str
    items: List[str]

class SimulationOutput(BaseModel):
    """
    Output data for the financial simulation
    """
    data: List[float]
    summary: str
    math_explanation: Dict[str, List[MathExplanationSection]]
