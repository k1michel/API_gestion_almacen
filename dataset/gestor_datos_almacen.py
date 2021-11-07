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
        self.electricidad = self.db['electricidad']  
        self.neumatica = self.db['neumatica'] 
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
            

    def insertar_electricidad(self):

        self.electricidad.insert(
            dict(
                codigo = 'A0000',
                categoria = 'error integrity error de la propia sqlite',
                modelo = ' ',
                stock = ' ',
                fecha = ' '
            ))
        self.electricidad.insert(    
            dict(
                codigo = 'A0001',
                categoria = 'cable',
                modelo = 'Azul 2.5 mm',
                stock = '2',
                fecha = '2020'
            ))

        self.electricidad.insert(
            dict(
                codigo = 'A0002',
                categoria = 'dispositivo',
                modelo = 'fuente alimentacion mofasica 3A',
                stock = '5',
                fecha = '2020'
            )) 

        self.electricidad.insert(
            dict(
                codigo = 'A0003',
                categoria = 'termico',
                modelo = 'termico bipolar 16A',
                stock = '10',
                fecha = '2020'
            ))
        self.electricidad.insert(
            dict(
                codigo = 'A0004',
                categoria = 'plc',
                modelo = 'plc siemens 1214c DC/DC/DC',
                stock = '5',
                fecha = '2020'
            ))   

    def insertar_neumatica(self):
        
        self.neumatica.insert(
            dict(
                codigo = 'B0000',
                categoria = 'error integrity error de la propia sqlite',
                modelo = ' ',
                stock = ' ',
                fecha = ' '
            ))

        self.neumatica.insert(
            dict(
                codigo = 'B0001',
                categoria = 'ev',
                modelo = 'ev doble camara',
                stock = '20',
                fecha = '2020'
            ))

        self.neumatica.insert(
            dict(
                codigo = 'B0002',
                categoria = 'racor',
                modelo = 'rosca 3/4 d8',
                stock = '15',
                fecha = '2020'
            ))

        self.neumatica.insert(
            dict(
                codigo = 'B0003',
                categoria = 'toma',
                modelo = 'recto d8-union',
                stock = '21',
                fecha = '2020'
            ))


    def mostrar_electricidad(self):
        return [dict(electricidad) for electricidad in self.electricidad.all()]

    def mostrar_neumatica(self):
        return [dict(neumatica) for neumatica in self.neumatica.all()]
    
    def mostrar_envios(self):
        return [dict(envios) for envios in self.envios.all()]
    
    def eliminar_electricidad(self):
        self.electricidad.delete()
        return 
    
    def eliminar_neumatica(self):
        self.neumatica.delete()
        return 

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
        
     