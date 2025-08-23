# Prueba tecnica Ing Datos - Kitsune

# Ejecución entorno virtual
Antes de instalar dependencias o ejecutar el proyecto, se debe revisar si existe el .venv en la raíz. Si no existe, se debera crear:

En Windows (cmd o PowerShell):

python -m venv .venv
.venv\Scripts\activate

En Git Bash:

python -m venv .venv
source .venv/Scripts/activate

En Linux/Mac:

python3 -m venv .venv
source .venv/bin/activate


Esto asegura que las dependencias se instalen de forma aislada para tu proyecto.

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

# P2

En la segunda parte del proyecto se implementa una API con FastAPI para consultar y filtrar los datos almacenados en la base de datos SQLite.

# Cómo ejecutar la API
1. Activar el entorno virtual (.venv) antes de instalar dependencias (ver instrucciones arriba).
2. Instala las dependencias necesarias para la API:
   pip install fastapi uvicorn
3. Ejecuta el servidor FastAPI desde la raíz del proyecto:
   uvicorn src.api_server:app --reload
# Endpoints
- Listar todos los registros: GET /datos
- Consultar por ID: GET /datos/{id}
- Filtrar por año y/o palabra clave: 
GET /datos/especificos/filtrar?fecha=2014&palabra=agua
/datos/especificos/filtrar?palabra=agua
/datos/especificos/filtrar?fecha=2014
# Consideraciones
- La API consulta directamente la base de datos SQLite generada en la p1.
- Se puede usar Postman o tu navegador para probar los endpoints.
- Si modificas la estructura de la base de datos, asegúrate de actualizar los filtros en el archivo api_server.py.
- El endpoint de filtro permite combinar búsqueda por año y por palabra clave en cualquier campo.







