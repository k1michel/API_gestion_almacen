import dataset

class Conexion:
    fichero_sqlite: str = 'base_datos.db' 
    electricidad = None
    neumatica = None
    envios = None


    def __init__(self):

        self.db = dataset.connect(
            f'sqlite:///{Conexion.fichero_sqlite}?check_same_thread=False')  # sirve para que varios procesos simultaneos se puedan ejecutar sin que salte warning
        # creamos instancia q mediante dataset la conectamos con nuestro fichero de la base de datos
        self.envios = self.db['envios']
        self.inventario = self.db['inventario']
    
    def insertar_envios(self,dic_paquete):
        return self.envios.insert(dic_paquete)
    
    def mostrar_inventario(self):
        return [dict(inventario) for inventario in self.inventario.all()]

    def eliminar_inventario(self):
        self.inventario.delete()
        return
    
    def insertar_inventario(self,dict_nuevo_item):
         return self.inventario.insert(dict_nuevo_item)  

    def buscar_codigo_inventario(self):
        existe_codigo = False
        for i in self.envios.all():
            print(i['busc'])
            for busqueda_codigo in self.inventario.all(): 
                print(busqueda_codigo['codigo'])
                if busqueda_codigo['codigo']==i['busc']:
                    encontrado = busqueda_codigo
                    existe_codigo = True
        if existe_codigo == False:
                encontrado = 'No existe'
                print('No existe')
        else:
            self.envios.insert(dict(encontrado))         
            
    def borrar_modificado(self,dict_modificado):
        id_borrar_modificado = dict_modificado['id_modificar']
        self.inventario.delete(id=id_borrar_modificado)
        return
    
    def borrar_categoria(self, dict_borrar_categoria):
        categoria_eliminar = dict_borrar_categoria['categoria_delete']
        self.inventario.delete(categoria=categoria_eliminar)
        return
    
    def mostrar_envios(self):
        return [dict(envios) for envios in self.envios.all()]


    def eliminar_envios(self):
        self.envios.delete()
        return 
    
    def buscar_codigo(self):
        existe_codigo = False
        for i in self.envios.all():
            print(i['busc'])
            for busqueda_codigo in self.electricidad.all(): 
                print(busqueda_codigo['codigo'])
                if busqueda_codigo['codigo']==i['busc']:
                    encontrado = busqueda_codigo
                    existe_codigo = True
            if existe_codigo == False:
                for busqueda_codigo in self.neumatica.all(): 
                    print(busqueda_codigo['codigo'])
                    if busqueda_codigo['codigo']==i['busc']:
                        encontrado = busqueda_codigo
                        existe_codigo = True
        if existe_codigo == True:
            self.envios.insert(dict(encontrado))         
        else:
            print('No existe')
        
     