import requests


class PollosApi:

    def __init__(self):
        self.__base_url = 'http://localhost:8000'

    def get_pollos(self):
        respuesta = requests.get(
            url=f'{self.__base_url}/pollos'
        )
        return respuesta.json()
    
    def crear_pollo(self,pollo):
        respuesta = requests.post(
            url=f'{self.__base_url}/pollos'
        )
        return respuesta.json()
    
    
    