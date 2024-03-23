from fastapi import APIRouter
from database.machinservice import (get_all_machines_db, get_machine_by_id_db, get_all_machines_by_type_db,
                                    get_all_machines_by_company_db, get_machine_by_model_db, edit_info_db,
                                    delete_machine_db, add_machine_db)
from machine import Machine


machine_router = APIRouter(prefix='/machine', tags=['Methods for machines'])


@machine_router.get('/all-machine')
async def all_machine():
    result = get_all_machines_db()
    return result


@machine_router.get('/by-type')
async def get_by_type(machine_type: str):
    machine = get_all_machines_by_type_db(machine_type=machine_type)
    if machine:
        return machine
    else:
        return machine


@machine_router.get('/by-model')
async def get_by_type(machine_model: str):
    machine = get_machine_by_model_db(machine_model=machine_model)
    if machine:
        return machine
    else:
        return machine


@machine_router.get('/by-id')
async def get_by_type(id: int):
    machine = get_machine_by_id_db(id=id)
    if machine:
        return machine
    else:
        return machine


@machine_router.get('/by-company')
async def get_by_type(machine_company: str):
    machine = get_all_machines_by_company_db(machine_company=machine_company)
    if machine:
        return machine
    else:
        return machine


@machine_router.post('/add-machine')
async def add_machine(machine_type, machine_model, machine_company, machine_color, machine_cost):
    machine = add_machine_db(machine_type, machine_model, machine_company, machine_color, machine_cost)
    return machine


@machine_router.post('/edit-machin')
async def edit_machin(id: int, new_model: str, new_type: str, new_company: str, new_color: str, new_cost: str, choose: str):
    machine = edit_info_db(id=id, new_cost=new_cost, new_color=new_color, new_model=new_model, new_type=new_type,
                           new_company=new_company, choose=choose)
    return machine


@machine_router.delete('/delete-machine')
async def delete_machine(id: int):
    machine = delete_machine_db(id)
    return machine




















