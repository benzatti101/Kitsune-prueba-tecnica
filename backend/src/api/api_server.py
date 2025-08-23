from fastapi import FastAPI, Query, Path
import sqlite3

app = FastAPI()

@app.get("/datos", description="Listar todos los registros de la tabla 'datos'")
def get_datos():
    # Lista todos los registros
    conn = sqlite3.connect("local_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM datos")  # Consulta todos los registros
    columns = [desc[0] for desc in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]  # Convierte cada fila en un diccionario
    conn.close()
    return results

@app.get("/datos/{id}", description="Consultar un registro específico por su ID")
def get_dato_by_id(id: int = Path(..., description="ID del registro a consultar")):
    # Consulta un registro por ID
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
    # Filtra registros por columna y palabra clave (insensible a mayúsculas)
    conn = sqlite3.connect("local_data.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM datos WHERE UPPER({columna}) = UPPER(?)"
    cursor.execute(query, (palabra,))
    columns = [desc[0] for desc in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    conn.close()
    return results