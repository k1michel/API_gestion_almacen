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
  

almacen = FastAPI() 

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