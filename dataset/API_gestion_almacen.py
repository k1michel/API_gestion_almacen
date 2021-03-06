from typing import Optional   
from fastapi import FastAPI
from pydantic import BaseModel  
from datetime import datetime
from threading import Thread
from time import sleep
import uvicorn
from gestor_datos_almacen import Conexion
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

class Datos(BaseModel):         
    codigo: str                     
    categoria: str  
    modelo: str
    stock: int
    fecha: str
    precio: float
    precio_min: float
    precio_max: float

class Paquete(BaseModel):                             
    busc: str 

class Borrado(BaseModel):
    id_borrar_item : str
    codigo_borrar_item: str

class Categoria_borrar(BaseModel):
    categoria_delete : str

class Clientes_provedores (BaseModel):
    cip: str
    empresa: str
    ubicacion: str
    telefono: str
    email: str
    proyecto: str
    contacto: str

class Pedido(BaseModel):
    codigo: str
    categoria: str
    modelo: str
    unidades: int
    precio: float
    fecha: str

almacen = FastAPI() 
almacen.mount("/static_files", StaticFiles(directory="static_files"), name="static_files")
conexion = Conexion()

### ENVIOS ###

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

### INVENTARIO ###

@almacen.post("/inventario")
def post_inventario(Nuevo_item: Datos):
    dict_nuevo_item = dict(
        codigo = Nuevo_item.codigo,
        categoria = Nuevo_item.categoria,
        modelo = Nuevo_item.modelo,
        stock = Nuevo_item.stock,
        fecha = Nuevo_item.fecha,
        precio = Nuevo_item.precio,
        precio_min = Nuevo_item.precio_min,
        precio_max = Nuevo_item.precio_max

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

@almacen.post("/borrar_item")
def delete_borrar_item(borrado: Borrado):
    dict_borrado = dict(
        id_borrar_item = borrado.id_borrar_item,
        codigo_borrar_item = borrado.codigo_borrar_item
    )
    conexion.borrado_item(dict_borrado)
    return 'Borrado de item OK'

@almacen.delete("/categoria_borrar")
def delete_categoria(borrar_categoria: Categoria_borrar):
    dict_borrar_categoria=dict(
        categoria_delete = borrar_categoria.categoria_delete
    )
    conexion.borrar_categoria(dict_borrar_categoria)
    return 'Borrada la categoria OK'

### HISTORIAL PRECIOS ###

@almacen.post("/historial_precios")
def post_historial(Nuevo_historial: Datos):
    dict_nuevo_historial = dict(
        codigo = Nuevo_historial.codigo,
        categoria = Nuevo_historial.categoria,
        modelo = Nuevo_historial.modelo,
        stock = Nuevo_historial.stock,
        fecha = Nuevo_historial.fecha,
        precio = Nuevo_historial.precio,
        precio_min = Nuevo_historial.precio_min,
        precio_max = Nuevo_historial.precio_max
    )
    conexion.insertar_historial(dict_nuevo_historial)
    return 'Nuevo item insertado en Historial de Precios'

@almacen.get("/historial_precios")
def get_historial():
    return conexion.mostrar_historial()

@almacen.delete("/historial_precios")
def delete_historial():
    conexion.eliminar_historial()
    return 'Historial de precios eliminado OK'

@almacen.get("/historial_precios_recibir")
def get_recibir_historial():
    return conexion.mostrar_historial()

### HOME API ###

def generate_html_response():
    html_content = """
    <html>
        <head>
            <title>
                Gestor Almacen
            </title>
        </head>
        <body>
            <header>
                <div align="center">
                    <img src="./static_files/Letras_gestor_almacen_2.png" width="400" height="100" alt="portada">
                    <h1>BIENVENIDOS AL SERVIDOR</h1>
                    <h3>Todo esta correcto por aqui...<h3>
                </div>
            </header>
            <p style="text-align:center">
                Servidor local con instancias de bases de datos para la gestion con sus clientes
            </p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@almacen.get("/", response_class=HTMLResponse)
async def home():
    return generate_html_response()

### RUN API ###

if __name__ == "__main__":  # si el nombre del script que se esta ejecutando es main realiza lo siguiente
    
    uvicorn.run(almacen, host="0.0.0.0", port=8000)