# backend/app/routers/auth.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from passlib.context import CryptContext
from app.schemas.user import UserResponse, UserLogin, UserCreate
from sqlalchemy import or_

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register")
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    # Verificar si el usuario ya existe
    existing_user = db.query(User).filter(
        (User.email == user_data.email) | 
        (User.cedula == user_data.cedula)
    ).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email o cédula ya registrados")
    
    # Hashear la contraseña
    hashed_password = pwd_context.hash(user_data.password)

    # Crear el nuevo usuario
    new_user = User(
        cedula=user_data.cedula,
        nombre=user_data.nombre,
        apellido=user_data.apellido,
        email=user_data.email,
        hashed_password=hashed_password,
        rol=user_data.rol,
        estado=user_data.estado
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "Registro exitoso"}

@router.post("/login")
def login_user(credentials: UserLogin, db: Session = Depends(get_db)):
    # Buscar por email o cedula
    user = db.query(User).filter(
        (User.email == credentials.identifier) | 
        (User.cedula == credentials.identifier)
    ).first()

    if not user or not pwd_context.verify(credentials.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    return {"message": "Login exitoso", "user_id": user.id}