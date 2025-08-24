# Prueba tecnica Ing Datos - Kitsune

# Estructura del proyecto
- Backend/ETL: Extracción, tranformación y cargue.
- Backend/API: Endpoints consulta de datos.
- Frontend: Interfaz.

# Flujo de datos
1. Obtención: Usamos el endpoint público para traer los primeros 20 registros en formato JSON.
2. Transformación: El modelo limpia los datos, excluye campos basura y prepara los valores para la base de datos.
3. Almacenamiento: Los datos se guardan en una base de datos SQLite local y se manejan los nombres de las columnas sin caracteres especiales en la base de datos, ya que el API publico lo maneja con "_" caracteres especiales y espacios.

# Cómo probar el proyecto P1
Se debe verificar en primera instancia que el proyecto se encuentre clonado desde su repositorio de github compartido para sus respectivas pruebas, y una vez clonado tener el entorno activo para sus respectivas instalaciónes.
0. Ejecución entorno virtual
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
1. Instalar las dependencias:
pip install requests
2. Ejecuta el script principal para poblar la base de datos:
python -m backend.src.main 
(Se uso este comando por la estructura como se manejo el proyecto, ya que al aplicar los principios SOLID de buenas practicas se manejo por carpetas, se realiza el comando por los import de los modulos, se puede cambiar dependiendo de los import de cada modulo)
Nota comando: Al tener estructurado el proyecto por modulos se debera ejecutar el comando para que identifique las diferentes import realizado sobre los modulos del proyecto para que asi se pueda ejecutar el Main.
3. Si se desea consulta la base de datos generada, se debera instalar la extension de SQLite en VS code
4. Dar clic derecho sobre el archivo "local_data.db" y selecciona "Open Database".
5. Luego se debe dar click "New Query" y se debera ejecutar "Run Query" el siguiente SQL:
 SELECT * FROM datos;
6. Verificar extracción/transformación/cargue de datos extraidos de la API Publica. 

# P2: API
En la segunda parte del proyecto se implementa una API con FastAPI para consultar y filtrar los datos almacenados en la base de datos SQLite.

# Cómo ejecutar la API
0. Si se realizara con Docker se debera saltar los pasos a continuación y pasar al P4 y seguir los pasos de ejecución.
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
Ej: http://localhost:8000/datos/especificos/filtrar?columna=pa_s_residencia&palabra=CHILE
# Consideraciones
- La API consulta directamente la base de datos SQLite generada en la p1.
- Se puede usar Postman o el navegador para probar los endpoints.
- Si se modifica la estructura de la base de datos, no tendra problema ya que el API es mantenible a posibles cambios, el unico detalle es si se cambia el nombre de la BD se debera realiza rel respectivo ajuste en api_server.py


# P3: FrontEnd

# Instalación y configuración del frontend para usar Vue y Vite

1. Instalar Node.js y npm desde https://nodejs.org/ (requisito para usar Vue).
2. Instalar CLI vue dentro de este comando se selecciona el package manager yarn o en su preferencia npm en este caso fue con yarn:
npm install -g @vue/cli
Vue 3
Yarn
3. Iniciar el servidor front
yarn serve

# P4: Docker Compose  (Bonus)

# 🐳 Ejecución con Docker

### Prerequisitos
- Docker instalado y configurado.
- Base de datos generada: python -m backend.src.main - P1.

### Comandos

1. Construir y levantar API:
docker-compose up --build
2. Ejecutar en segundo plano:
docker-compose up -d
3. Ver logs:
docker-compose logs -f api
4. Detener:
docker-compose down

# Servicios
- API: http://localhost:8000/datos (Ejecución por docker)
- Docs: http://localhost:8000/docs
- Frontend: yarn serve (se ejecuta por separado)
- APP: http://localhost:8080/

---

# 🤖 Uso de Inteligencia Artificial

## Herramientas IA Utilizadas

En el desarrollo de este proyecto se emplearon herramientas de inteligencia artificial **a través de GitHub Copilot** para optimizar la estructura, lógica y aplicación de buenas prácticas:

### **Claude Sonnet 3.5  - Frontend y Arquitectura
- **Uso principal**: Desarrollo del frontend Vue.js y estructuración del proyecto
- **Eficiencia aplicada**:
  - Configuración óptima de Vue CLI con mejores prácticas
  - Estructuración de componentes siguiendo principios de composición
  - Optimización de la arquitectura de carpetas y módulos
  - Implementación de patrones de diseño para mantenibilidad

### **GPT-4o  - Backend y DevOps
- **Uso principal**: Desarrollo del backend FastAPI y configuración Docker
- **Eficiencia aplicada**:
  - Implementación de principios SOLID en la estructura del backend
  - Separación de responsabilidades entre ETL, API y modelos de datos
  - Configuración profesional de Docker y Docker Compose
  - Optimización de consultas SQLite y manejo de errores
  - Documentación técnica y buenas prácticas de desarrollo

## Impacto en el Proyecto

### **Estructura y Organización**
- Aplicación de **principios SOLID** para código mantenible
- Separación clara de **responsabilidades** (ETL, API, DB, Frontend)
- **Modularización** apropiada del código Python
- Configuración de **entornos virtuales** y dependencias

### **Buenas Prácticas Implementadas**
- **Clean Code**: Nombres descriptivos, funciones pequeñas y enfocadas
- **Error Handling**: Manejo apropiado de excepciones y validaciones
- **Documentation**: Comentarios claros y README comprensivo
- **DevOps**: Dockerización para portabilidad y facilidad de despliegue
- **API Design**: Endpoints RESTful con documentación automática

### **Eficiencia en Desarrollo**
- **Aceleración**: Reducción significativa en tiempo de desarrollo
- **Calidad**: Implementación de patrones probados desde el inicio
- **Escalabilidad**: Estructura preparada para crecimiento futuro
- **Mantenibilidad**: Código limpio y bien documentado

La IA fue utilizada a través de GitHub Copilot como herramienta de consultoría técnica y aceleración de desarrollo, manteniendo siempre el control sobre las decisiones arquitectónicas y la comprensión completa del código implementado.







