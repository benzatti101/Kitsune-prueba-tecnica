from backend.src.etl.extract import DataExtractor
from backend.src.etl.load import DataLoader
from backend.src.etl.transform import DataTransformer


def main():
    # Obtener datos del endpoint
    retriever = DataExtractor()
    data = retriever.fetch_data()

    # Inicializar y conectar la base de datos
    db_manager = DataLoader()
    db_manager.connect()

    # Crear la tabla solo una vez usando los nombres originales del JSON
    if data:
        columns = list(data[0].keys())
        db_manager.create_table(columns)
        db_manager.clear_table()  # Limpiar la tabla antes de insertar

    # Procesar e insertar los datos
    for item in data:
        model = DataTransformer(item)
        db_manager.insert_data(model)

    print("Datos insertados correctamente en la base de datos.")

if __name__ == "__main__":
    main()
