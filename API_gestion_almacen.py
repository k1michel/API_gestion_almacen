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
    stock: str
    fecha: str

class Paquete(BaseModel):                             
    busc: str 

almacen = FastAPI() 

conexion = Conexion()

@almacen.post("/envios")
def post_envios(paquete : Paquete):
    conexion.eliminar_envios()
    dic_paquete= dict(
        busc=paquete.busc,
    )
    conexion.insertar_envios(dic_paquete)
    conexion.buscar_codigo()
    return 'Paquete recibido en Envios OK'
@almacen.post("/envios_recibir")
def post_recibir_envios():
    return conexion.mostrar_envios()

@almacen.get("/envios")
def get_envios():
    list_envio = conexion.mostrar_envios()
    return list_envio

@almacen.delete("/envios")
def delete_envios():
    conexion.eliminar_envios()
    return 'Eliminado completo Envios OK'

@almacen.get("/electricidad")  
def get_electricidad():
    return conexion.mostrar_electricidad()

@almacen.get("/neumatica")  
def get_neumatica():
    return conexion.mostrar_neumatica()

@almacen.post("/electricidad")
def post_electricidad():
    conexion.insertar_electricidad()
    return 'Insertados en Electricidad OK'

@almacen.get("/electricidad_mostrar")
def post_electricidad_mostrar():
    return conexion.mostrar_electricidad()

@almacen.post("/neumatica")
def post_neumatica():
    conexion.insertar_neumatica()
    return 'Insertados en Neumatica OK'

@almacen.get("/neumatica_mostrar")
def post_electricidad_mostrar():
    return conexion.mostrar_neumatica()

@almacen.delete("/electricidad")
def delete_electricidad():
    conexion.eliminar_electricidad()
    return 'Eliminado completo Electricidad OK'

@almacen.delete("/neumatica")
def delete_neumatica():
    conexion.eliminar_neumatica()
    return 'Eliminado completo Neumatica OK'




if __name__ == "__main__":  # si el nombre del script que se esta ejecutando es main realiza lo siguiente
    
    uvicorn.run(almacen, host="0.0.0.0", port=8000)