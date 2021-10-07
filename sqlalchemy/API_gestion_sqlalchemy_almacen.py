from typing import Optional   
from fastapi import FastAPI
from pydantic import BaseModel  
from datetime import datetime
from threading import Thread
from time import sleep
import uvicorn
from gestor_datos_sqlalchemy_almacen import Conexion, Producto, Categoria

class Datos(BaseModel):         
    codigo: str                     
    id_categoria: str  
    grupo = str
    modelo: str
    stock: str
    ultima_modificacion: str

class Paquete(BaseModel):                             
    busc: str 

almacen = FastAPI() 

conexion = Conexion()
sql_productos = Producto()
sql_categorias = Categoria ()
conexion.insertar_categorias()
'''
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
'''


## MOSTRAR UNICA CATEGORIA
@almacen.get("/categorias/categoria")  
def get_categoria(nombre):
    return conexion.get_categoria(nombre=nombre)

## MOSTRAR TODAS LAS CATEGORIAS
@almacen.get("/categorias")  
def get_categorias():
    return conexion.mostrar_categorias()

##ELIMINAR TODOS LOS PRODUCTOS
@almacen.delete("/productos")
def delete_todas_productos():
    conexion.delete_productos()
    return 'ELIMINADOS TODOS LAS PRODUCTOS OK'

## MOSTRAR UNICO PRODUCTO
@almacen.get("/producto")
def get_producto(modelo, nombre_categoria):
    return conexion.get_producto(modelo, nombre_categoria)

##MOSTRAR TODOS LOS PRODUCTOS
@almacen.get("/productos")
def get_productos():
    return conexion.mostrar_productos()

@almacen.post("/productos")
def post_productos():
    conexion.insertar_productos_manual()



if __name__ == "__main__":  # si el nombre del script que se esta ejecutando es main realiza lo siguiente
    
    uvicorn.run(almacen, host="0.0.0.0", port=8000)