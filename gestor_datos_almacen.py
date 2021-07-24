import dataset

class Conexion:
    fichero_sqlite: str = 'base_datos.db' 
    electricidad = None
    neumatica = None



    def __init__(self):

        self.db = dataset.connect(
            f'sqlite:///{Conexion.fichero_sqlite}?check_same_thread=False')  # sirve para que varios procesos simultaneos se puedan ejecutar sin que salte warning
        # creamos instancia q mediante dataset la conectamos con nuestro fichero de la base de datos
        self.electricidad = self.db['electricidad']  # variable que alberga dentro de la instancia de la bd la lista
        self.neumatica = self.db['neumatica'] 
         
    def insertar_electricidad(self):

        self.electricidad.insert(
            dict(
                codigo = 'A0001',
                categoria = 'cable',
                modelo = 'Azul 2.5 mm',
                stock = 2
            ))

        self.electricidad.insert(
            dict(
                codigo = 'A0002',
                categoria = 'dispositivo',
                modelo = 'fuente alimentacion mofasica 3A',
                stock = 5
            ))

        self.electricidad.insert(
            dict(
                codigo = 'A0003',
                categoria = 'termico',
                modelo = 'termico bipolar 16A',
                stock = 10
            ))

        self.neumatica.insert(
            dict(
                codigo = 'B0001',
                categoria = 'ev',
                modelo = 'ev doble camara',
                stock = 20
            ))

        self.neumatica.insert(
            dict(
                codigo = 'B0002',
                categoria = 'racor',
                modelo = 'rosca 3/4 d8',
                stock = 15
            ))

        self.neumatica.insert(
            dict(
                codigo = 'B0003',
                categoria = 'toma',
                modelo = 'recto d8-union',
                stock = 21
            ))
