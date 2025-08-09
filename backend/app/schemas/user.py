from pydantic import BaseModel, EmailStr
from typing import Optional, Literal
from datetime import datetime

class UserBase(BaseModel):
    id: Optional[int]
    cedula: str
    nombre: str
    apellido: str
    email: EmailStr
    password: str
    rol: Literal['estudiante', 'encargado', 'admin'] = 'estudiante'
    estado: Literal['activo', 'penalizado'] = 'activo'
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

class UserLogin(BaseModel):
    identifier: str # Puede ser email o cédula
    password: str