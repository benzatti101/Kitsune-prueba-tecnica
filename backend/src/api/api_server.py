from fastapi import FastAPI, Query, Path
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()

# Configurar CORS para permitir peticiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://127.0.0.1:8080"],  # Permitir el puerto del frontend de Vue
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/datos", description="Listar todos los registros de la tabla 'datos'")
def get_datos():
    # Lista todos los registros tal como están en la BD
    conn = sqlite3.connect("local_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM datos")  # Consulta todos los registros
    columns = [desc[0] for desc in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]  # Convierte cada fila en un diccionario
    conn.close()
    return results

@app.get("/datos/{id}", description="Consultar un registro específico por su ID")
def get_dato_by_id(id: int = Path(..., description="ID del registro a consultar")):
    # Consulta un registro por ID tal como está en la BD
    conn = sqlite3.connect("local_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM datos WHERE id = ?", (id,))  # Busca el registro por ID
    columns = [desc[0] for desc in cursor.description]
    row = cursor.fetchone()
    conn.close()
    if row:
        return dict(zip(columns, row))  # Devuelve el registro como diccionario
    return {"error": "No encontrado"}  # Si no existe, devuelve un error

@app.get("/datos/especificos/filtrar", description="Filtrar registros por columna y palabra clave exacta, insensible a mayúsculas/minúsculas")
def filtrar_especificos(
    columna: str = Query(..., description="Nombre de la columna a filtrar"),
    palabra: str = Query(..., description="Palabra clave exacta")
):
    # Filtra registros por columna y palabra clave tal como están en la BD
    conn = sqlite3.connect("local_data.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM datos WHERE UPPER({columna}) = UPPER(?)"
    cursor.execute(query, (palabra,))
    columns = [desc[0] for desc in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    conn.close()
    return results