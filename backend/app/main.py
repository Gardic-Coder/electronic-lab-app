from fastapi import FastAPI

app = FastAPI()

# Ejemplo de endpoint
@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}