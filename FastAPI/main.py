### Hola Mundo ###

# Documentación oficial: https://fastapi.tiangolo.com/es/

# Instala FastAPI: pip install "fastapi[all]"
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return 'Hola'

#Correr el servidor con una terminal integrada a el modulo
# PS C:\Users\User\Downloads\Nueva carpeta (2)\FastAPI> python -m uvicorn main:app --reload

# Url local: http://127.0.0.1:8000

@app.get("/")
async def root():
    return "Hola FastAPI!"

# Url local: http://127.0.0.1:8000/url

@app.get("/url")
async def url():
    return { "url": "https://fastapi.tiangolo.com/" }

# Inicia el server: uvicorn main:app --reload
# Detener el server: CTRL+C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc
