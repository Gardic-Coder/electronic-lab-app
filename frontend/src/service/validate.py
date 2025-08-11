# frontend/src/service/validate.py
import re

def is_not_empty(value: str) -> bool:
    return bool(value and value.strip())

def is_valid_email(email: str) -> bool:
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def is_strong_password(password: str) -> bool:
    # Al menos 8 caracteres, una mayúscula, una minúscula, un número
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
    return re.match(pattern, password) is not None

def validate_login(identifier: str, password: str) -> dict:
    errors = {}
    if not is_not_empty(identifier):
        errors["identifier"] = "Cedula o Correo obligatorio."
    if not is_not_empty(password):
        errors["password"] = "La contraseña es obligatoria."
    return errors

def validate_register(cedula: str, nombre: str, apellido: str, email: str, password: str, confirm_password: str) -> dict:
    errors = {}
    if not is_not_empty(cedula):
        errors["cedula"] = "La cédula es obligatoria."
    elif not cedula.isdigit() or len(cedula) < 7:
        errors["cedula"] = "La cédula debe ser un número de al menos 7 dígitos."
    if not is_not_empty(nombre):
        errors["nombre"] = "El nombre es obligatorio."
    if not is_not_empty(apellido):
        errors["apellido"] = "El apellido es obligatorio."
    if not is_valid_email(email):
        errors["email"] = "El correo no es válido."
    if not is_strong_password(password):
        errors["password"] = "La contraseña debe tener al menos 8 caracteres, una mayúscula, una minúscula y un número."
    if password != confirm_password:
        errors["password"] = "Las contraseñas no coinciden."
    return errors
