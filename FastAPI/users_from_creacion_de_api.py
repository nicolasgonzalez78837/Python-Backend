### Users API ###
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Inicia el server: python -m uvicorn users:app --reload

class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int

users_list = [User(name = "Brais", surname = "Moure", url = "https://moure.dev", age = 35),
User(name = "Moure", surname = "Dev", url = "https://moure.dev", age = 35),
User(name ="Haakon", surname = "Daglberg", url = "https://haakon.com", age = 33)]

@app.get("/usersjson")
async def usersjson():  # Creamos un JSON a mano
    return [{"name": "Brais", "surname": "Moure", "url": "https://moure.dev", "age": 35},
            {"name": "Moure", "surname": "Dev", "url": "https://mouredev.com", "age": 35},
            {"name": "Haakon", "surname": "Dahlberg", "url": "https://haakon.com", "age": 33}]

@app.get("/users")
async def users():
    return (users_list)
