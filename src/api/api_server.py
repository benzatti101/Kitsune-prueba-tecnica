from fastapi import FastAPI, Query
import sqlite3

app = FastAPI()

@app.get("/datos")
def get_datos():
    # Endpoint para listar todos los registros de la tabla 'datos'
    conn = sqlite3.connect("local_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM datos")  # Consulta todos los registros
    columns = [desc[0] for desc in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]  # Convierte cada fila en un diccionario
    conn.close()
    return results

@app.get("/datos/{id}")
def get_dato_by_id(id: int):
    # Endpoint para consultar un registro específico por su ID
    conn = sqlite3.connect("local_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM datos WHERE id = ?", (id,))  # Busca el registro por ID
    columns = [desc[0] for desc in cursor.description]
    row = cursor.fetchone()
    conn.close()
    if row:
        return dict(zip(columns, row))  # Devuelve el registro como diccionario
    return {"error": "No encontrado"}  # Si no existe, devuelve un error

@app.get("/datos/especificos/filtrar")
def filtrar_especificos(fecha: str = Query(None), palabra: str = Query(None)):
    # Endpoint para filtrar registros por fecha y/o palabra clave en cualquier columna
    conn = sqlite3.connect("local_data.db")
    cursor = conn.cursor()
    # Construye la consulta base para agregar filtros dinámicos
    query = "SELECT * FROM datos WHERE 1=1"  # 1=1 siempre es verdadero, facilita agregar condiciones
    params = []
    if fecha:
        # Agrega filtro por fecha si se recibe el parámetro
        query += " AND a_o_inscripci_n LIKE ?"
        params.append(f"%{fecha}%")
    if palabra:
        # Agrega filtro por palabra clave en todas las columnas (excepto id)
        query += " AND ("
        cursor.execute("PRAGMA table_info(datos)")  # Obtiene los nombres de las columnas
        columns = [row[1] for row in cursor.fetchall() if row[1] != 'id']
        like_clauses = [f"{col} LIKE ?" for col in columns]
        query += " OR ".join(like_clauses) + ")"
        params += [f"%{palabra}%"] * len(columns)
    # Ejecuta la consulta con los filtros aplicados
    cursor.execute(query, params)
    columns = [desc[0] for desc in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    conn.close()
    return results
