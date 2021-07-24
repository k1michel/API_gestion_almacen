from typing import Optional    #libreria que usa FastApi
from fastapi import FastAPI
from pydantic import BaseModel  #modelo estrictamente tipado para heredar su clase
from datetime import datetime
from threading import Thread
from time import sleep
import uvicorn
from gestor_datos_almacen import Conexion


class Datos(BaseModel):         #crear clase para realizar el post de volatil con estructura basemodel
    codigo: str                     #basemodel tiene init
    categoria: str  
    modelo: str
    stock: int
  

almacen = FastAPI() #creamos aplicacion FASTAPI

conexion = Conexion()

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
    return conexion.insertar_electricidad()

@almacen.post("/neumatica")
def post_neumatica():
    conexion = Conexion()
    return conexion.insertar_neumatica()



if __name__ == "__main__":  # si el nombre del script que se esta ejecutando es main realiza lo siguiente
    
    uvicorn.run(almacen, host="0.0.0.0", port=8080)