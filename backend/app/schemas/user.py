# backend/app/schemas/user.py
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Literal
from datetime import datetime

# Esquema para CREACIÓN de usuario (input)
class UserCreate(BaseModel):
    cedula: str = Field(..., min_length=11, max_length=12)
    nombre: str = Field(..., min_length=2, max_length=50)
    apellido: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    password: str
    #Campos opcionales
    rol: Literal['estudiante', 'encargado', 'admin'] = 'estudiante'
    estado: Literal['activo', 'penalizado'] = 'activo'

# Esquema para LOGIN
class UserLogin(BaseModel):
    identifier: str # Puede ser email o cédula
    password: str

# Esquema para RESPUESTA (output)
class UserResponse(BaseModel):
    id: int
    cedula: str
    nombre: str
    apellido: str
    email: EmailStr
    rol: str
    estado: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True