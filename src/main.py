A especificação menciona a geração de uma API em Node.js, mas como a tarefa pede um código Python usando FastAPI e Pydantic, presumo que isso seja um erro. Portanto, eu vou criar um código Python para uma API com dois endpoints.


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float

items = {}

@app.post("/items/")
async def create_item(item: Item):
    """Create a new item"""
    if item.name in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item.name] = item
    return item

@app.get("/items/{item_name}")
async def read_item(item_name: str):
    """Get a specific item by name"""
    if item_name not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_name]

Este código cria uma API FastAPI com dois endpoints: um para criar um novo item (POST em /items/) e um para ler um item específico (GET em /items/{item_name}). Os itens são validados usando o modelo Pydantic 'Item', e são armazenados em um dicionário em memória. O código inclui tratamento de erros para situações em que um item já existe ou não pode ser encontrado.