import requests
# Clase responsable de obtener datos desde el endpoint público
class DataExtractor:
    # URL del endpoint con límite de 20 registros
    ENDPOINT = "https://www.datos.gov.co/resource/7q36-mkp5.json?$limit=20"

    def fetch_data(self):
        # Realiza una petición GET al endpoint y retorna los datos en formato JSON
        # Lanza una excepción si la respuesta no es exitosa
        response = requests.get(self.ENDPOINT)
        response.raise_for_status()  # Verifica si la petición fue exitosa
        return response.json()  # Retorna los datos como lista de diccionarios
