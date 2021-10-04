from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError
from datetime import date, datetime
Base = declarative_base()

class Producto(Base):
    __tablename__ = 'productos'

    codigo = Column(Integer, primary_key=True)
    grupo = Column(String)
    id_categoria = Column(Integer, ForeignKey('categoria.id'))
    modelo = Column(String, unique=True)
    stock = Column(Integer)
    ultima_modificacion = Column(DateTime)

    def to_dict(self):
        return dict(
            codigo = self.codigo,
            id_categoria = self.id_categoria,
            grupo = self.grupo,
            modelo = self.modelo,
            stock = self.stock,
            ultima_modificacion = self.ultima_modificacion.strftime('%Y/%m/%d %H:%M'),
            )
        
class Categoria(Base):
    __tablename__ = 'categoria'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True)
    productos = relationship('Producto')
    
    def to_dict(self):
        return dict(id=self.id, nombre=self.nombre, productos=[producto.to_dict() for producto in self.productos])

def get_engine():
    return create_engine(f'sqlite:///{Conexion.fichero_sqlite}?check_same_thread=False')  # sirve para que varios procesos simultaneos se puedan ejecutar sin que salte warning
    
class Conexion:
    fichero_sqlite: str = 'base_datos.db' 
    electricidad = None
    neumatica = None
    envios = None

    def __init__(self):
        self.engine = get_engine()
        Base.metadata.create_all(self.engine)  # Creamos la estructura de tablas en la base de datos

        self.session = sessionmaker(bind=self.engine)()
        
        #self.insertar_categorias()
        #self.insertar_productos()
        
        '''
        print([producto.to_dict() for producto in self.get_productos_de_categoria('electricidad')])
        print([categoria.to_dict() for categoria in self.get_categorias()])
        # self.delete_productos()
        print('-'*100)
        self.update_producto('ev doble camara', Producto(grupo='ev', modelo='ev doble camara', stock=15))
        print([categoria.to_dict() for categoria in self.get_categorias()])
        '''

    def insertar_categorias(self):
        electricidad = Categoria(nombre='electricidad')
        neumatica = Categoria(nombre='neumatica')
        
        self.session.add(electricidad)
        self.session.add(neumatica)
        try:
            self.session.commit()  # guardar los cambios
        except (IntegrityError) as e:
            self.session.rollback()
            print('ya estaban las categorias creadas')
    
    def add_producto_a_categoria(self, producto, nombre_categoria):
        categoria = (
            self.session.query(Categoria)
            .filter(Categoria.nombre == nombre_categoria)
            .one_or_none()
        )
        categoria.productos.append(producto)
        try:
            self.session.commit()  # guardar los cambios
        except (IntegrityError) as e:
            self.session.rollback()
            print('ya existe el producto', producto.modelo)

    def update_producto(self, modelo, modificacion_producto):
        self.get_producto(modelo).update(
            dict(
                grupo = modificacion_producto.grupo,
                modelo = modificacion_producto.modelo,
                stock = modificacion_producto.stock,
                ultima_modificacion = datetime.now()
            )
        )
        self.session.commit()

    def delete_producto(self, modelo):
        producto = self.get_producto(modelo)
        producto.delete()
        self.session.commit()

    def delete_productos(self):
        self.session.query(Producto).delete()
        self.session.commit()
        
    def delete_categoria(self, nombre): # Por hacer
        categoria = self.get_categoria(nombre)
        categoria.delete()
        self.session.commit()
        

    def delete_categorias(self):
        self.session.query(Categoria).delete()
        self.session.commit()

    def get_categorias(self):
        return self.session.query(Categoria).all()
    
    def get_categoria(self, nombre):
        return self.session.query(Categoria).filter(Categoria.nombre == nombre)

    def get_productos(self):
        return self.session.query(Producto).all()
    
    def get_producto(self, modelo):
        return self.session.query(Producto).filter(Producto.modelo == modelo)
    

    def get_productos_de_categoria(self, nombre_categoria):
        categoria = (
            self.session.query(Categoria)
            .filter(Categoria.nombre == nombre_categoria)
            .one_or_none()
        )
        return categoria.productos

    def insertar_productos_manual(self):
        self.add_producto_a_categoria(
            producto = Producto(grupo='cable', modelo='Azul 2.5mm', stock=2, ultima_modificacion=datetime.now()),
            nombre_categoria = 'electricidad'
        )
        self.add_producto_a_categoria(
            producto = Producto(grupo='dispositivo', modelo='fuente alimentacion mofasica 3A', stock=6, ultima_modificacion=datetime.now()),
            nombre_categoria = 'electricidad'
        )
        self.add_producto_a_categoria(
            producto = Producto(grupo='termico', modelo='termico bipolar 16A', stock=10, ultima_modificacion=datetime.now()),
            nombre_categoria = 'electricidad'
        )
        self.add_producto_a_categoria(
            producto = Producto(grupo='plc', modelo='plc siemens 1214c DC/DC/DC', stock=2, ultima_modificacion=datetime.now()),
            nombre_categoria = 'electricidad'
        )
        # Neumatica
        self.add_producto_a_categoria(
            producto = Producto(grupo='ev', modelo='ev doble camara', stock=20, ultima_modificacion=datetime.now()),
            nombre_categoria = 'neumatica'
        )
        self.add_producto_a_categoria(
            producto = Producto(grupo='racor', modelo='rosca 1/4 toma 8 diametro', stock=12, ultima_modificacion=datetime.now()),
            nombre_categoria = 'neumatica'
        )
        self.add_producto_a_categoria(
            producto = Producto(grupo='conexion', modelo='recto 6 diametro', stock=25, ultima_modificacion=datetime.now()),
            nombre_categoria = 'neumatica'
        )
        self.add_producto_a_categoria(
            producto = Producto(grupo='bloque ev', modelo='6 modulos profinet in y out power in', stock=5, ultima_modificacion=datetime.now()),
            nombre_categoria = 'neumatica'
        )
    def mostrar_categorias(self):
        return [categoria.to_dict() for categoria in self.get_categorias()]
    
    def mostrar_productos(self):
        return [producto.to_dict() for producto in self.get_productos()]