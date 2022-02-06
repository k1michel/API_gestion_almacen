import dataset

class Conexion:
    fichero_sqlite: str = 'base_datos.db' 
    inventario = None
    envios = None
    historial_precios = None

    def __init__(self):

        self.db = dataset.connect(
            f'sqlite:///{Conexion.fichero_sqlite}?check_same_thread=False')  # sirve para que varios procesos simultaneos se puedan ejecutar sin que salte warning
        # creamos instancia q mediante dataset la conectamos con nuestro fichero de la base de datos
        self.envios = self.db['envios']
        self.inventario = self.db['inventario']
        self.historial_precios = self.db['historial_precios']
        self.pedido_marchando = self.db['pedido_marchando']
        self.pedidos = self.db['pedidos']
        self.clientes = self.db['clientes']
        self.provedores = self.db['provedores']

    ### PEDIDO MARCHANDO ###

    def insertar_pedido_marchando(self,dict_pedido_marchando):
        return self.pedido_marchando.insert(dict_pedido_marchando)

    def mostrar_pedido_marchando(self):
        return [dict(pedido_marchando) for pedido_marchando in self.pedido_marchando.all()]
    
    def eliminar_pedido_marchando(self):
        self.pedido_marchando.delete()
        return

    ### PEDIDOS ###

    def insertar_pedidos(self,dict_pedidos):
        return self.pedidos.insert(dict_pedidos)

    def mostrar_pedidos(self):
        return [dict(pedidos) for pedidos in self.pedidos.all()]
    
    def eliminar_pedidos(self):
        self.pedidos.delete()
        return

    ### CLIENTES ###

    def insertar_clientes(self,dict_clientes):
        return self.clientes.insert(dict_clientes)

    def mostrar_clientes(self):
        return [dict(clientes) for clientes in self.clientes.all()]
    
    def eliminar_clientes(self):
        self.clientes.delete()
        return

    ### PROVEDORES ###

    def insertar_provedores(self,dict_provedores):
        return self.provedores.insert(dict_provedores)

    def mostrar_provedores(self):
        return [dict(provedores) for provedores in self.provedores.all()]
    
    def eliminar_provedores(self):
        self.provedores.delete()
        return

    ### HISTORIAL PRECIOS ### 

    def insertar_historial(self,dict_nuevo_historial):
        return self.historial_precios.insert(dict_nuevo_historial)
    
    def mostrar_historial(self):
        return [dict(historial) for historial in self.historial_precios.all()]

    def eliminar_historial(self):
        self.historial_precios.delete()
        return

    ### ENVIOS ###

    def insertar_envios(self,dic_paquete):
        return self.envios.insert(dic_paquete)
    
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

    ### INVENTARIO ###

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
            
    def borrado_item(self,dict_borrado):
        id_borrar_item = dict_borrado['id_borrar_item']
        codigo_borrar_item = dict_borrado['codigo_borrar_item']
        self.inventario.delete(id=id_borrar_item)
        self.historial_precios.delete(codigo=codigo_borrar_item)
        return
    
    def borrar_categoria(self, dict_borrar_categoria):
        categoria_eliminar = dict_borrar_categoria['categoria_delete']
        self.inventario.delete(categoria=categoria_eliminar)
        return
    
 
    

        
     