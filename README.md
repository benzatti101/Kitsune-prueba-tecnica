Prueba tecnica Ing Datos - Kitsune

# Estructura del proyecto
- src/api/data_retriever.py: Se encarga de obtener datos de un endpoint publico (https://www.datos.gov.co/resource/7q36-mkp5.json?$limit=20)
- src/models/data_model.py*: Transformar y limpiar los datos antes de guardarlos.
- src/database/database_manager.py: Inserción/Borrado/Creación SQLite local.
- src/main.py: Script principal de extracción, transformación y listado de los datos.

# Flujo de datos
1. Obtención: Usamos el endpoint público para traer los primeros 20 registros en formato JSON.
2. Transformación: El modelo limpia los datos, excluye campos basura y prepara los valores para la base de datos.
3. Almacenamiento: Los datos se guardan en una base de datos SQLite local y se manejan los nombres de las columnas sin caracteres especiales en la base de datos, y incluyendo los espacios que se reemplazaron por "_".

# Cómo probar el proyecto P1
1. Instala las dependencias:
pip install requests
2. Ejecuta el script principal para poblar la base de datos:
python -m src.main (Se uso este comando por la estructura como se manejo el proyecto, ya que al aplicar los principios SOLID de buenas practicas se manejo por carpetas)
Nota comando: Al tener estructurado el proyecto por modulos se debera ejecutar el comando para que identifique las diferentes import realizado sobre los modulos del proyecto para que asi se pueda ejecutar el Main.
3. Si se desea consulta la basse de datos generada, se debera instalar la extension de SQLite en VS code y 
4. Haz clic derecho sobre el archivo "local_data.db" y selecciona "Open Database".
5. Luego se debe dar click "New Query" y se debera ejecutar "Run Query" el siguiente SQL:
 SELECT * FROM datos;
  






