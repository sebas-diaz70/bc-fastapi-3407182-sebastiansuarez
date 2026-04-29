from fastapi import FastAPI, HTTPException
from typing import Optional

# TODO 1: Crear aplicación FastAPI
app = FastAPI(
    title="API Academia de Artes Marciales",
    version="1.0.0",
    description="API para la gestión de estudiantes, instructores, clases y cinturones"
)

# ===============================
# TODO 2: Endpoint raíz
# ===============================
@app.get("/")
async def root():
    return {
        "name": "API Academia de Artes Marciales",
        "version": "1.0.0",
        "domain": "academia-artes-marciales"
    }

# ===============================
# TODO 3: Bienvenida personalizada
# ===============================
@app.get("/{actor}/{name}")
async def welcome(actor: str, name: str, language: Optional[str] = "es"):
    
    actor = actor.lower()

    if language == "en":
        message = f"Welcome {name}! You are accessing the {actor} system."
    elif language == "fr":
        message = f"Bienvenue {name}! Vous accédez au système de {actor}."
    else:
        message = f"¡Bienvenido {name}! Estás accediendo al sistema de {actor} de la academia."

    return {
        "actor": actor,
        "message": message
    }

# ===============================
# TODO 4: Información de entidad
# ===============================
@app.get("/{entity}/{identifier}/info")
async def entity_info(entity: str, identifier: str, detail_level: Optional[str] = "basic"):
    
    entity = entity.lower()

    # Datos simulados
    database = {
        "estudiantes": {
            "id": identifier,
            "nombre": "Juan Pérez",
            "cinturon": "Amarillo",
            "edad": 18
        },
        "instructores": {
            "id": identifier,
            "nombre": "Sensei Carlos",
            "rango": "Cinturón Negro",
            "experiencia": "10 años"
        },
        "clases": {
            "id": identifier,
            "nombre": "Karate Básico",
            "horario": "Lunes y Miércoles 6pm",
            "capacidad": 20
        },
        "cinturones": {
            "id": identifier,
            "nivel": "Amarillo",
            "descripcion": "Nivel básico de aprendizaje"
        }
    }

    if entity not in database:
        raise HTTPException(status_code=404, detail="Entidad no encontrada")

    result = database[entity]

    if detail_level == "full":
        result.update({
            "academia": "Academia de Artes Marciales",
            "estado": "activo",
            "notas": "Información completa del sistema"
        })

    return result

# ===============================
# TODO 5: Servicio según horario
# ===============================
@app.get("/servicio/horario")
async def schedule(hour: int):
    
    if hour < 0 or hour > 23:
        raise HTTPException(status_code=400, detail="La hora debe estar entre 0 y 23")

    if 6 <= hour <= 11:
        return {
            "mensaje": "Turno mañana: Clases activas",
            "disponible": ["karate", "taekwondo"]
        }
    elif 12 <= hour <= 17:
        return {
            "mensaje": "Turno tarde: Clases activas",
            "disponible": ["judo", "kung fu"]
        }
    else:
        return {
            "mensaje": "Turno noche: Clases activas",
            "disponible": ["mma", "defensa personal"]
        }

# ===============================
# TODO 6: Health check
# ===============================
@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "domain": "academia-artes-marciales"
    }