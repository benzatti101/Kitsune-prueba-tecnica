from backend.src.api.data_retriever import DataRetriever
from backend.src.database.database_manager import DatabaseManager
from backend.src.models.data_model import DataModel


def main():
    # Obtener datos del endpoint
    retriever = DataRetriever()
    data = retriever.fetch_data()

    # Inicializar y conectar la base de datos
    db_manager = DatabaseManager()
    db_manager.connect()

    # Crear la tabla solo una vez usando los títulos del primer elemento
    if data:
        columns = list(data[0].keys())
        db_manager.create_table(columns)
        db_manager.clear_table()  # Limpiar la tabla antes de insertar

    # Procesar e insertar los datos
    for item in data:
        model = DataModel(item)
        db_manager.insert_data(model)

    print("Datos insertados correctamente en la base de datos.")

if __name__ == "__main__":
    main()
