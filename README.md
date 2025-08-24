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
- Backend/ETL: Extracción, tranformación y cargue.
- Backend/API: Endpoints consulta de datos.
- Frontend: Interfaz.

# Flujo de datos
1. Obtención: Usamos el endpoint público para traer los primeros 20 registros en formato JSON.
2. Transformación: El modelo limpia los datos, excluye campos basura y prepara los valores para la base de datos.
3. Almacenamiento: Los datos se guardan en una base de datos SQLite local y se manejan los nombres de las columnas sin caracteres especiales en la base de datos, ya que el API publico lo maneja con "_" caracteres especiales y espacios.

# Cómo probar el proyecto P1
1. Instala las dependencias:
pip install requests
2. Ejecuta el script principal para poblar la base de datos:
python -m backend.src.main (Se uso este comando por la estructura como se manejo el proyecto, ya que al aplicar los principios SOLID de buenas practicas se manejo por carpetas, se realiza el comando por los import de los modulos, se puede cambiar dependiendo de los import de cada modulo y sobre en que parte de la carpeta se este ejecutando)
Nota comando: Al tener estructurado el proyecto por modulos se debera ejecutar el comando para que identifique las diferentes import realizado sobre los modulos del proyecto para que asi se pueda ejecutar el Main.
3. Si se desea consulta la basse de datos generada, se debera instalar la extension de SQLite en VS code y 
4. Haz clic derecho sobre el archivo "local_data.db" y selecciona "Open Database".
5. Luego se debe dar click "New Query" y se debera ejecutar "Run Query" el siguiente SQL:
 SELECT * FROM datos;

# P2: API
En la segunda parte del proyecto se implementa una API con FastAPI para consultar y filtrar los datos almacenados en la base de datos SQLite.

# Cómo ejecutar la API
1. Activar el entorno virtual (.venv) antes de instalar dependencias (ver instrucciones arriba).
2. Instala las dependencias necesarias para la API:
   pip install fastapi uvicorn
3. Ejecuta el servidor FastAPI desde la raíz del proyecto:
   uvicorn backend.src.api.api_server:app --reload
# Endpoints
- Listar todos los registros: GET /datos
- Consultar por ID: GET /datos/{id}
- Filtrar por año y/o palabra clave:
GET 
/datos/especificos/filtrar
Ej: http://127.0.0.1:8000/datos/especificos/filtrar?columna=pa_s_residencia&palabra=CHILE
# Consideraciones
- La API consulta directamente la base de datos SQLite generada en la p1.
- Se puede usar Postman o tu navegador para probar los endpoints.
- Si modificas la estructura de la base de datos, asegúrate de actualizar los filtros en el archivo api_server.py.
- El endpoint de filtro permite combinar búsqueda por año y por palabra clave en cualquier campo.

# P3: FrontEnd

# Instalación y configuración del frontend para usar Vue y Vite

1. Instalar Node.js y npm desde https://nodejs.org/ (requisito para usar Vue).
2. Instalar CLI vue dentro de este comando se selecciona el package manager yarn o en su preferencia npm en este caso fue con yarn:
npm install -g @vue/cli
Vue 3
Yarn
3. Iniciar el servidor de desarrollo:
yarn serve
Esto genera la estructura del proyecto Vue en la carpeta frontend y deja todo listo para desarrollar la interfaz.

## Siguiente paso
- Crear los componentes para mostrar los registros en una tabla, buscar por palabra clave y ver detalles de un registro.





