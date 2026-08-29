from fastapi import FastAPI

app = FastAPI(title="Introduccion a FastAPI")

@app.get("/")
async def root():
    """Devuelve mensaje de bienvenida."""
    return {"message": "Hola Mundo"}

@app.get("/ping")
async def ping():
    """Comprueba la disponibilidad del servidor."""
    return {"status": "ok"}
