from fastapi import FastAPI

from database import Pollos #eNVIAMOS LOS DATOS A FASAPI Y LOS RECIBIMOS DEL HOST QUE LE DEMOS
#aL HOTS LE DAMOS UNA URL DE RENDER Y PAGES PARA HTML:


app = FastAPI()

@app.get('/pollos')
def get_pollos():
    return Pollos


