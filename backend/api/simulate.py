from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from deception_engine.simulator import generate_fake_response
from utils.session_logger import log_session 

router = APIRouter()

class SimulateRequest(BaseModel):
    input: str

@router.post("/simulate")
def simulate_command(req: SimulateRequest):
    try:
        reply = generate_fake_response(req.input)
        log_session(req.input, reply)  
        return {"response": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
