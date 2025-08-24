# Usar imagen base de Python
FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivo de dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código fuente del backend
COPY backend/ ./backend/

# Copiar base de datos SQLite
COPY local_data.db ./local_data.db

# Exponer puerto 8000
EXPOSE 8000

# Comando para ejecutar la API
CMD ["uvicorn", "backend.src.api.api_server:app", "--host", "0.0.0.0", "--port", "8000"]
