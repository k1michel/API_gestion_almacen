from typing import Optional   
from fastapi import FastAPI
from pydantic import BaseModel  
from datetime import datetime
from threading import Thread
from time import sleep
import uvicorn
from gestor_datos_almacen import Conexion


class Datos(BaseModel):         
    codigo: str                     
    categoria: str  
    modelo: str
    stock: int
    fecha: str

class Paquete(BaseModel):         
    cat: str                     
    busc: str 

almacen = FastAPI() 

conexion = Conexion()

@almacen.post("/envios")
def post_envios(paquete : Paquete):
    conexion = Conexion()
    dic_paquete= dict(
        cat=paquete.cat,
        busc=paquete.busc,
    )
    conexion.insertar_envios(dic_paquete)
    return 'Paquete recibido en Envios OK'

@almacen.get("/envios")
def get_envios():
    conexion = Conexion()
    return conexion.mostrar_envios()

@almacen.delete("/envios")
def delete_envios():
    conexion = Conexion()
    conexion.eliminar_envios()
    return 'Eliminado completo Envios OK'

@almacen.get("/electricidad")  
def get_electricidad():
    conexion = Conexion()
    return conexion.mostrar_electricidad()

@almacen.get("/neumatica")  
def get_neumatica():
    conexion = Conexion()
    return conexion.mostrar_neumatica()

@almacen.post("/electricidad")
def post_electricidad():
    conexion = Conexion()
    conexion.insertar_electricidad()
    return 'Insertados en Electricidad OK'

@almacen.post("/neumatica")
def post_neumatica():
    conexion = Conexion()
    conexion.insertar_neumatica()
    return 'Insertados en Neumatica OK'

@almacen.delete("/electricidad")
def delete_electricidad():
    conexion = Conexion()
    conexion.eliminar_electricidad()
    return 'Eliminado completo Electricidad OK'

@almacen.delete("/neumatica")
def delete_neumatica():
    conexion = Conexion()
    conexion.eliminar_neumatica()
    return 'Eliminado completo Neumatica OK'




if __name__ == "__main__":  # si el nombre del script que se esta ejecutando es main realiza lo siguiente
    
    uvicorn.run(almacen, host="0.0.0.0", port=8000)