from app.database import engine
from app.models import user

def init_db():
    print("Creando tablas en la base de datos...")
    user.Base.metadata.create_all(bind=engine)
    #component.Base.metadata.create_all(bind=engine)
    print("¡Tablas creadas exitosamente!")

if __name__ == "__main__":
    init_db()