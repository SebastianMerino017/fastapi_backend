from fastapi import FastAPI

app = FastAPI(title="Query Parameters")

fake_items_db = [
    {"item_name": "Monitor"},
    {"item_name": "Teclado"},
    {"item_name": "Mouse"}
]

# 1. Paginacion con valores por defecto
@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# 2. Combinacion de Path Param, Query Opcional y Booleano
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int,
    item_id: str,
    q: str | None = None,
    short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "Descripcion extendida del item"})
    return item

# 3. Parametro de Query Requerido (sin valor por defecto)
@app.get("/items1/{item_id}")
async def read_item_required(item_id: str, needy: str):
    return {"item_id": item_id, "needy": needy}
