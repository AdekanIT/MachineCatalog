from database import get_db
from database.models import Machine


def get_all_machines_db():
    db = next(get_db())
    machines = db.query(Machine).all()
    return machines


def get_all_machines_by_type_db(machine_type):
    db = next(get_db())
    machine = db.query(Machine).filter_by(machine_type=machine_type).all()
    if machine:
        return machine
    else:
        return f'{machine} not found'


def get_all_machines_by_company_db(machine_company):
    db = next(get_db())
    machine = db.query(Machine).filter_by(machine_company=machine_company).all()
    if machine:
        return machine
    else:
        return f'{machine} not found'


def get_machine_by_model_db(machine_model):
    db = next(get_db())
    machine = db.query(Machine).filter_by(machine_model=machine_model).first()
    if machine:
        return machine
    else:
        return f'{machine} not found'


def get_machine_by_id_db(id):
    db = next(get_db())
    machine = db.query(Machine).filter_by(id=id).first()
    if machine:
        return machine
    else:
        return f'Machine by {id} ID not found'


def edit_info_db(id, new_model, new_type, new_company, new_color, new_cost, choose):
    db = next(get_db())
    machine = db.query(Machine).filter_by(id=id).first()
    if choose == 'model':
        machine.machine_model = new_model
        db.commit()
        return 'Machine changed'
    elif choose == 'type':
        machine.machine_type = new_type
        db.commit()
        return 'Machine changed'
    elif choose == 'company':
        machine.machine_company = new_company
        db.commit()
        return 'Machine changed'
    elif choose == 'color':
        machine.machine_color = new_color
        db.commit()
        return 'Machine changed'
    elif choose == 'cost':
        machine.machine_cost = new_cost
        db.commit()
        return 'Machine changed'
    else:
        return f'Machine by {id} ID not found'


def add_machine_db(machine_type, machine_model, machine_company, machine_color, machine_cost):
    db = next(get_db())
    machine = Machine(machine_type=machine_type, machine_model=machine_model, machine_company=machine_company,
                      machine_color=machine_color, machine_cost=machine_cost)
    db.add(machine)
    db.commit()
    return machine


def delete_machine_db(id):
    db = next(get_db())
    machine = db.query(Machine).filter_by(id=id).first()
    if machine:
        db.delete(machine)
        db.commit()
        return 'Machine deleted'
    else:
        return f'Machine by {id} ID not found'






















