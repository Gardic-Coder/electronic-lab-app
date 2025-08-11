# backend/app/routers/auth.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from passlib.context import CryptContext
from app.schemas.user import UserResponse, UserLogin, UserCreate
from fastapi.responses import JSONResponse
#from sqlalchemy import or_

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

    # Verificar credenciales
    if not user or not pwd_context.verify(credentials.password, user.hashed_password):
        return JSONResponse(status_code=200, content={"success": False})

    # Simular token (puedes reemplazar con JWT luego)
    fake_token = f"token-{user.id}"

    # Convertir instancia de User a UserResponse
    user_data = UserResponse(
        id=user.id,
        cedula=user.cedula,
        nombre=user.nombre,
        apellido=user.apellido,
        email=user.email,
        rol=user.rol,
        estado=user.estado,
        created_at=user.created_at,
        updated_at=user.updated_at
    )

    # Construir respuesta
    return {
        "success": True,
        "token": fake_token,
        "user": user_data
    }