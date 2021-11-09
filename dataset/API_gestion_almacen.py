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
    precio: str

class Paquete(BaseModel):                             
    busc: str 

class Modificado(BaseModel):
    id_modificar : str

class Categoria_borrar(BaseModel):
    categoria_delete : str


almacen = FastAPI() 

conexion = Conexion()

@almacen.post("/envios")
def post_envios(paquete : Paquete):
    conexion.eliminar_envios()
    dic_paquete= dict(
        busc=paquete.busc,
    )
    conexion.insertar_envios(dic_paquete)
    conexion.buscar_codigo_inventario()
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


@almacen.post("/inventario")
def post_inventario(Nuevo_item: Datos):
    dict_nuevo_item = dict(
        codigo = Nuevo_item.codigo,
        categoria = Nuevo_item.categoria,
        modelo = Nuevo_item.modelo,
        stock = Nuevo_item.stock,
        fecha = Nuevo_item.fecha,
        precio = Nuevo_item.precio

    )
    conexion.insertar_inventario(dict_nuevo_item)
    return 'Nuevo item insertado en Inventario'

@almacen.get("/inventario")
def get_inventario():
    return conexion.mostrar_inventario()

@almacen.delete("/inventario")
def delete_inventario():
    conexion.eliminar_inventario()
    return 'Inventario eliminado OK'

@almacen.get("/inventario_recibir")
def get_recibir_inventario():
    return conexion.mostrar_inventario()

@almacen.post("/modificar")
def delete_modificar(modificado: Modificado):
    dict_modificado = dict(
        id_modificar = modificado.id_modificar
    )
    conexion.borrar_modificado(dict_modificado)
    return 'Borrado de modificar OK'

@almacen.delete("/categoria_borrar")
def delete_categoria(borrar_categoria: Categoria_borrar):
    dict_borrar_categoria=dict(
        categoria_delete = borrar_categoria.categoria_delete
    )
    conexion.borrar_categoria(dict_borrar_categoria)
    return 'Borrada la categoria OK'

if __name__ == "__main__":  # si el nombre del script que se esta ejecutando es main realiza lo siguiente
    
    uvicorn.run(almacen, host="0.0.0.0", port=8000)