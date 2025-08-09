# Sistema de Gestión de Laboratorio Electrónico

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.88.0-green)
![Flet](https://img.shields.io/badge/Flet-0.14.2-orange)
![MySQL](https://img.shields.io/badge/MySQL-8.0-blue)

Sistema completo para la gestión de inventario, préstamos y usuarios en laboratorios de electrónica universitaria. Permite a encargados administrar componentes y préstamos, y a estudiantes solicitar materiales con seguimiento automatizado.

## Características Principales

- **Gestión de inventario avanzada** con categorización por tags
- **Sistema de préstamos** con aprobación en tiempo real
- **Seguimiento de devoluciones** con registro de estado de componentes
- **Penalizaciones automáticas** por retrasos o daños
- **Panel de efemérides técnicas** diarias
- **Sistema de auditoría** completo para todas las operaciones
- **Roles diferenciados**: estudiantes, encargados y administradores

## Tecnologías Utilizadas

| Área           | Tecnologías                               |
|----------------|-------------------------------------------|
| Frontend       | Flet (Python)                             |
| Backend        | FastAPI (Python)                          |
| Base de Datos  | MySQL                                     |
| Autenticación  | JWT (JSON Web Tokens)                     |
| Almacenamiento | Sistema de archivos local / S3 (opcional) |

## Estructura del Proyecto

```
electronic-lab-app/
├── backend/         # API FastAPI (Python)
│   ├── app/         
│       ├── models/  # Modelos de base de datos
│       ├── routers/ # Endpoints API
│       ├── services/# Lógica de negocio
│       └── utils/   # Utilidades comunes
│
├── frontend/        # UI Flet (Python)
│   ├── src/
│       ├── views/   # Pantallas de la aplicación
│       ├── components/ # Componentes UI
│       └── services/   # Conexión con backend
│
└── scripts/          # Scripts de inicialización DB
```

### Entidades Principales
- **Usuario**: Cédula, nombre, apellido, email, rol, estado
- **Componente**: Descripción, stock, ubicación, datasheet, imagen
- **Préstamo**: Usuario, estado, fechas, lista de componentes
- **Categoría**: Sistema de tags para clasificar componentes
- **Efeméride**: Notas diarias sobre hitos técnicos

## Instalación y Configuración

### Requisitos Previos
- Python 3.9+
- MySQL 8.0+

### Pasos de Instalación

1. Clonar repositorio:
```bash
git clone https://github.com/tu-usuario/electronic-lab-app.git
cd electronic-lab-app
```

2. Configurar entorno:
```bash
# Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac)
venv\Scripts\activate    # Windows

# Instalar dependencias
pip install -r backend/requirements.txt
pip install -r frontend/requirements.txt
```

3. Configurar base de datos:
- Crear archivo `.env` en la raíz del proyecto:
```ini
# 🔗 Conexión a la base de datos
DATABASE_URL=mysql://<USUARIO>:<CONTRASEÑA>@<HOST>:<PUERTO>/<NOMBRE_BASE_DATOS>

# 🔐 Clave secreta para firmar tokens JWT
SECRET_KEY=<CLAVE_SECRETA_SEGURA>

# ⚙️ Configuración general
DEBUG=True
ENV=development  # Cambiar a "production" en entorno de producción

# 🌐 Configuración del frontend
FRONTEND_PORT=8550

# 🕒 Tiempo de expiración de los tokens JWT (en minutos)
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

4. Inicializar base de datos:
```bash
mysql -u root -p < scripts/init_db.sql
```

5. Ejecutar aplicaciones:
```bash
# Iniciar backend (FastAPI)
cd backend
uvicorn app.main:app --reload

# Iniciar frontend (Flet)
cd ../frontend
flet run src/main.py
```

## Estado Actual del Proyecto

### ✅ Funcionalidades Completadas

### ⏳ En Progreso
- Autenticación de usuarios (login/registro)
- CRUD básico de componentes electrónicos
- Sistema de categorización por tags
- Solicitud de préstamos por estudiantes
- Aprobación/rechazo de préstamos por encargados

### 📅 Próximas Funcionalidades
- Registro básico de devoluciones
- Sistema de penalizaciones automáticas
- Integración con APIs de efemérides
- Panel de auditoría para administradores
- Notificaciones automáticas por email
- Gestión avanzada de imágenes y PDFs
- Reportes estadísticos de uso
- Integración con sistemas universitarios (LDAP)
- Sistema de reserva de componentes
- Dashboard con métricas clave
- Mobile app complementaria

## Capturas de Pantalla

*(Se agregarán cuando la interfaz esté más desarrollada)*

## Contribución

Las contribuciones son bienvenidas! Sigue estos pasos:

1. Haz fork del proyecto
2. Crea una rama (`git checkout -b feature/nueva-funcionalidad`)
3. Realiza tus cambios y commitea (`git commit -m 'Agregar nueva funcionalidad'`)
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).

---
