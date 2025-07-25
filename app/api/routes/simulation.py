from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db_session
from app.schemas.simulation import SimulationInput, SimulationOutput
from app.services.simulation_logic import run_simulation

router = APIRouter()

@router.post("/simulate/{scenario}", response_model=SimulationOutput)
def simulate_scenario(
    scenario: str,
    input_data: SimulationInput,
    db: Session = Depends(get_db_session)
):
    """
    POST Endpoint to run a financial simulation based on the provided scenario and input data
    """
    try:
        result = run_simulation(scenario, input_data.dict())
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
