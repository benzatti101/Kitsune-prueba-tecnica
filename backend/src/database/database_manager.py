import sqlite3
from backend.src.models.data_model import DataModel

class DatabaseManager:
    def __init__(self, db_name="local_data.db"):
        self.db_name = db_name
        self.conn = None

    def connect(self):
        # Establece la conexión con la base de datos SQLite
        self.conn = sqlite3.connect(self.db_name)

    def create_table(self, columns):
        # Crea la tabla 'datos' con columnas dinámicas según los títulos del JSON
        cursor = self.conn.cursor()
        columns_def = ', '.join([f'{col} TEXT' for col in columns])  # Define cada columna como texto
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS datos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                {columns_def}
            )
        ''')  # Crea la tabla si no existe
        self.conn.commit()  # Guarda los cambios

    def insert_data(self, model: DataModel):
        # Inserta un registro en la tabla 'datos' usando los datos procesados por el modelo
        cursor = self.conn.cursor()
        keys = list(model.data.keys())  # Obtiene los nombres de las columnas
        values = [str(model.data.get(k, '')) for k in keys]  # Obtiene los valores a insertar
        columns_str = ', '.join(keys)
        placeholders = ', '.join(['?' for _ in keys])  # Prepara los placeholders para la consulta
        cursor.execute(f'''
            INSERT INTO datos ({columns_str})
            VALUES ({placeholders})
        ''', values)  # Inserta los datos en la tabla
        self.conn.commit()  # Guarda los cambios

    def clear_table(self):
        # Elimina todos los registros de la tabla 'datos' sin borrar la estructura
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM datos')  # Borra todas las filas
        self.conn.commit()  # Guarda los cambios en la base de datos
