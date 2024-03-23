from pydantic import BaseModel


class Machine(BaseModel):
    machine_type: str
    machine_company: str
    machine_model: str
    machine_cost: int
    machine_color: str

