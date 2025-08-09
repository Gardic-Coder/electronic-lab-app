from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.database import get_db
from app.routers import auth
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"message": "Sistema de Gestión de Laboratorio Electrónico"}