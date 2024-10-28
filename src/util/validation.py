from fastapi import HTTPException
from .envs import USERNAME
from ..model.association_request import AssociationRequest
from ..model.operational_request import OperationalRequest

def validate_association_request(request: AssociationRequest):
    check_value('username', request.username, USERNAME)
    validate_code(request.setup_code)
    
def validate_operational_request(request: OperationalRequest):
    check_value('username', request.username, USERNAME)
    check_required('userid', request.userid)
    check_required('password', request.password)

def validate_code(code: str):
    check_required('setup_code', code)
    if len(code) != 4:
        message="Field 'setup_code' must be exactly 4 length"
        raise_bad_response(message)
    if not code.isdigit():
        message="Field 'setup_code' must be composed by only digits"
        raise_bad_response(message)
    
def check_value(name: str, value: str, equal_value: str):
    check_required(name, value)
    if value == equal_value:
        return
    message = f"Field '{name}' not valid"
    raise_bad_response(message)

def check_required(name: str, value: str):
    if value:
        return
    message = f"Field '{name}' is required"
    raise_bad_response(message)

def raise_bad_response(message: str):
    raise HTTPException(status_code=400,detail=message)