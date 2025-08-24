import json


class DataTransformer:
    def __init__(self, data: dict):
        # Inicializa el diccionario interno para almacenar los datos procesados
        self.data = {}
        for key, value in data.items():
            # Si el valor es un dict, combina los valores no vacíos y excluye el campo 'human_address'
            if isinstance(value, dict):
                non_empty = [str(val) for k, val in value.items() if val and k != 'human_address']
                if non_empty:
                    self.data[key] = f"({', '.join(non_empty)})"
            else:
                # Si el valor es simple, lo guarda tal cual
                self.data[key] = value

    def get(self, key, default=None):
        # Devuelve el valor asociado a la clave, o el valor por defecto si no existe
        return self.data.get(key, default)
