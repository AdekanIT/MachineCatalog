from sqlalchemy import Column, String, Integer
from database import Base


class Machine(Base):
    __tablename__ = 'machine'
    id = Column(Integer, autoincrement=True, primary_key=True)
    machine_type = Column(String)
    machine_company = Column(String)
    machine_model = Column(String)
    machine_cost = Column(Integer)
    machine_color = Column(String)