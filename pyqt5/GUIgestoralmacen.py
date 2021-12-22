import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem,QHeaderView
from PyQt5.QtGui import QIcon, QPixmap
import requests
import json
from time import sleep
from datetime import datetime
from ObjectListView import ObjectListView, ColumnDefn

class gui_gestor_almacen(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI_Gestor_almacen.ui",self)
        ## LOGO ##
        pixmap = QPixmap('Letras_gestor_almacen_2.png')
        self.img_letras_logo.setPixmap(pixmap)
        ## FONDO ##
        pixmap = QPixmap('Fondo_gestor_almacen.png')
        self.img_fondo.setPixmap(pixmap)
        
        ##############################################
        ## RECOPILAR CATEGORIAS DEL INVENTARIO ##
        recibir_inventario = requests.get('http://localhost:8000/inventario_recibir')
        list_recibir_inventario = list(recibir_inventario.json())
        #print(list_recibir_inventario)
        list_dict_inventario = [dict(dict_inventario) for dict_inventario in list_recibir_inventario]
        #print(list_dict_inventario)
        self.list_categorias = []
        for i in range(1,len(list_dict_inventario)):    
            id_item = list_dict_inventario[i]
            id_item_anterior = list_dict_inventario[i-1]
            if len(self.list_categorias)>0:
                if id_item_anterior['categoria'] != id_item['categoria']:
                    n_list_categorias = 0
                    for l in range(0,len(self.list_categorias)):
                        if id_item['categoria'] != self.list_categorias[l]:
                            n_list_categorias += 1                          
                    if n_list_categorias == len(self.list_categorias):
                        self.list_categorias.append(id_item['categoria'])
            if len(self.list_categorias) == 0:
                    self.list_categorias.append(id_item['categoria'])    
        #print(f'La lista de categorias es: {self.list_categorias} ')
        self.list_categorias.sort()
        self.cbbox_categorias.addItems(self.list_categorias)
        self.cbbox_categorias.activated.connect(self.seleccion_categoria)
        #################################################        
        
        ## TOTAL INVERSEION ALMACEN
        self.suma_total_almacen = 0.00
        for t in range(1,len(list_dict_inventario)): 
            self.suma_total_almacen = round(float(list_dict_inventario[t]['precio']) + self.suma_total_almacen,3)
        self.ctrl_total_almacen.setText(str(self.suma_total_almacen) + ' €')

        #################################################
        
        ## BUSCAR CODIGO ##

        self.ctrl_buscar_codigo.editingFinished.connect(self.OnEnterPressedCodigo)
        #################################################

        ## BUSCAR MODELO ##

        self.ctrl_busqueda_modelo.editingFinished.connect(self.OnPressed_Busqueda_modelo)
        #################################################

        ## TABLA DE RESULTADOS ##
        self.tabla_resultado.setColumnCount(8)
        self.tabla_resultado.setRowCount(50)
        self.tabla_resultado.setHorizontalHeaderLabels(['Codigo','Categoria','Modelo','Stock','Ultima Modificacion', 'Precio','Precio min','Precio max'])
        self.tabla_resultado.horizontalHeader().setSectionResizeMode(80)
        ####################################################
        
        ##BOTON MODIFICAR ##
        self.boton_modificar.clicked.connect(self.OnClickedModificar)
        #####################################################

        ## BOTON NUEVO ##
        self.boton_nuevo.clicked.connect(self.OnClickedNuevo)
        #####################################################

        ## BOTON BORRAR ##
        self.boton_borrar.clicked.connect(self.OnClickedBorrar)
        #####################################################


        ## VARIABLES AUXILIARES ##
        self.n_pulsado_nuevo = 0
        self.n_pulsado_modificar = 0
        self.primer_ciclo_categorias = False
        self.nueva_list_categorias_antigua = []
        self.precio_min_calculado = float
        self.precio_max_calculado = float
        self.precio_medio = float
        

        ######################################################
    def enviar(self):
        envio = {
            "busc":self.busqueda_codigo
        }
        respuesta_envio = requests.post('http://localhost:8000/envios', data=json.dumps(envio))
        #print(f'Respuesta del requests -> {respuesta_envio.json()}')
        #print(f'Envio -> {envio}')
        #self.busqueda_codigo = 'vacio_0000'
        list_recibir_busqueda = requests.post('http://localhost:8000/envios_recibir')
        data_list_recibir_busqueda=list_recibir_busqueda.json()
        #print(data_list_recibir_busqueda)
        #if data_list_recibir_busqueda[0]['busc'] != 'vacio_0000':
        #print(data_list_recibir_busqueda)
        self.dict_recibir_busqueda = data_list_recibir_busqueda[1]
        self.ctrl_codigo.setText(self.dict_recibir_busqueda['codigo'])
        self.ctrl_categoria.setText(self.dict_recibir_busqueda['categoria'])
        self.ctrl_modelo.setText(self.dict_recibir_busqueda['modelo'])
        self.ctrl_stock.setText(str(self.dict_recibir_busqueda['stock']))
        self.ctrl_fecha.setText(self.dict_recibir_busqueda['fecha'])
        self.ctrl_precio.setText(str(self.dict_recibir_busqueda['precio']))
        self.ctrl_precio_min.setText(str(self.dict_recibir_busqueda['precio_min']))
        self.ctrl_precio_max.setText(str(self.dict_recibir_busqueda['precio_max']))
    def OnEnterPressedCodigo(self):
        self.busqueda_codigo = self.ctrl_buscar_codigo.text()
        print('Se ha introducido codigo para buscar',self.busqueda_codigo)
        self.enviar()

    def seleccion_categoria(self):
        self.categoria_seleccionada = self.cbbox_categorias.currentText()
        print(f'La categoria seleccionada es: {self.categoria_seleccionada}')
        recibir_inventario = requests.get('http://localhost:8000/inventario_recibir')
        json_recibir_inventario = recibir_inventario.json()
        list_json_inventario = [dict(id_item) for id_item in json_recibir_inventario]
        list_mostrar = []
        for i in range(0,len(list_json_inventario)):
            dict_list_json_inventario = list_json_inventario[i]
            if self.categoria_seleccionada == dict_list_json_inventario['categoria']:
                list_mostrar.append(dict_list_json_inventario)
        print(f'La lista recibida de la categoria {self.categoria_seleccionada} es:\n{list_mostrar}')
        codigo=[]
        categoria=[]
        modelo=[]
        stock=[]
        fecha=[]
        precio=[]
        precio_min = []
        precio_max = []
        for a in range (0,len(list_mostrar)):
            dict_mostrar = list_mostrar[a]

            item_codigo = dict_mostrar['codigo']
            item_categoria = dict_mostrar['categoria']
            item_modelo = dict_mostrar['modelo']
            item_stock = dict_mostrar['stock']
            item_fecha = dict_mostrar['fecha']
            item_precio = dict_mostrar['precio']
            item_precio_min = dict_mostrar['precio_min']
            item_precio_max =  dict_mostrar['precio_max']

            codigo.append(item_codigo)            
            categoria.append(item_categoria)
            modelo.append(item_modelo)
            stock.append(item_stock)
            fecha.append(item_fecha)
            precio.append(item_precio)
            precio_min.append(item_precio_min)
            precio_max.append(item_precio_max)

        self.data_categoria = {
            'Codigo': codigo,
            'Categoria': categoria,
            'Modelo':modelo,
            'Stock':stock,
            'Fecha':fecha,
            'Precio':precio,
            'Precio_min': precio_min,
            'Precio_max':precio_max
        }
        #print(f'Los datos seleccionados son: {self.data_categoria}')
        self.tabla_resultado.clear()
        self.tabla_resultado.setHorizontalHeaderLabels(['Codigo','Categoria','Modelo','Stock','Ultima Modificacion','Precio','Precio min','Precio max'])
        for n, key in enumerate(self.data_categoria.keys()):
            for m, item in enumerate(self.data_categoria[key]):
                self.tabla_resultado.setItem(m,n,QTableWidgetItem(item))
        self.tabla_resultado.verticalHeader().setDefaultSectionSize(80)
        
        self.suma_total_categoria = 0.00
        for t in range(0,len(list_mostrar)): 
            self.suma_total_categoria = round(float(list_mostrar[t]['precio']) + self.suma_total_categoria,3)
        self.ctrl_total_categoria.setText(str(self.suma_total_categoria) + ' €')
        self.ctrl_total_busqueda.clear()
    def fecha_actual(self):
        ahora = datetime.now()
        formato = "%Y-%m-%d_%H:%M:%S"
        fecha_hora_actual = ahora.strftime(formato)
        return fecha_hora_actual
        
    def actualizar_precios_medio(self):
        recibir_historial = requests.get('http://localhost:8000/historial_precios_recibir')
        json_recibir_historial = recibir_historial.json()
        list_json_historial = [dict(id_item) for id_item in json_recibir_historial]
        list_historial = []
        for i in range(0,len(list_json_historial)):
            dict_list_json_historial = list_json_historial[i]
            if self.busqueda_codigo == dict_list_json_historial['codigo']:
                list_historial.append(dict_list_json_historial)
        print(f'La lista de items del codigo {self.busqueda_codigo} es {list_historial}')
        list_precios=[]
        for h in range(0,len(list_historial)):
            list_precios.append(list_historial[h]['precio'])
        print(f'La lista de precios del codigo {self.busqueda_codigo} es {list_precios}')
        self.precio_min_calculado = float(min(list_precios) if len(list_precios)>0 else list_historial[0]['precio'])
        self.precio_max_calculado = float(max(list_precios) if len(list_precios)>0 else list_historial[0]['precio'])
        
        suma=0
        for s in range(0,len(list_precios)):
            suma = list_precios[s] + suma
        self.precio_medio = round(float(suma/len(list_precios)),3)
        print(f'Para el codigo {self.busqueda_codigo} tenemos los precios {list_precios}\nsiendo el min: {self.precio_min_calculado},\nel max: {self.precio_max_calculado}\ny el precio medio: {self.precio_medio}')       

    def OnClickedModificar(self):
        self.ctrl_mensaje.clear()
        self.ctrl_mensaje.setText('Espere para modificar...')
        print('Se ha pulsado boton Modificar')
        self.n_pulsado_modificar += 1
        if self.n_pulsado_modificar == 1:

            self.busqueda_codigo = self.ctrl_buscar_codigo.text()
            #print(f'Busqueda codigo -> {self.busqueda_codigo}\n')
            self.enviar()
            id_borrar = {
                "id_borrar_item": str(self.dict_recibir_busqueda['id']),
                "codigo_borrar_item": 'jkahsdfgjhñ'
            }
            #print(id_modificar)
            requests.post('http://localhost:8000/borrar_item', data= json.dumps(id_borrar))
            print('Esperando modificacion...')
            
            self.ctrl_fecha.setText('Auto')
            self.ctrl_precio_min.setText('Auto')
            self.ctrl_precio_max.setText('Auto')
            self.ctrl_mensaje.clear()
            self.ctrl_mensaje.setText('Ahora puede modificar...')
        if self.n_pulsado_modificar == 2:
            self.ctrl_mensaje.clear()
            self.ctrl_mensaje.setText('Procesando modificacion...')
            fecha_now = self.fecha_actual()
            item_amodificar = {
                'codigo':str(self.ctrl_codigo.text()),
                'categoria':str(self.ctrl_categoria.text()),
                'modelo': str(self.ctrl_modelo.text()),
                'stock': int(self.ctrl_stock.text()),
                'fecha': fecha_now,
                'precio':round(float(self.ctrl_precio.text()),3),
                'precio_min': 0.00,
                'precio_max': 0.00
                }
            
            respuesta_historial = requests.post('http://localhost:8000/historial_precios', data=json.dumps(item_amodificar))
            print(f'La respuesta del envio a historial de precios es: {respuesta_historial}')
            self.actualizar_precios_medio()
            nuevo_item_actualizado = {
                'codigo':str(self.ctrl_codigo.text()),
                'categoria':str(self.ctrl_categoria.text()),
                'modelo': str(self.ctrl_modelo.text()),
                'stock': int(self.ctrl_stock.text()),
                'fecha': fecha_now,
                'precio': round(float(self.precio_medio),3),
                'precio_min': round(float(self.precio_min_calculado),3),
                'precio_max': round(float(self.precio_max_calculado),3)
                }
            
            respuesta_inventario = requests.post('http://localhost:8000/inventario', data=json.dumps(nuevo_item_actualizado))
            self.n_pulsado_modificar = 0
            if (str(respuesta_historial) == '<Response [200]>') and (str(respuesta_inventario) == '<Response [200]>'):
                self.ctrl_mensaje.setText('Modificar OK')
                self.ctrl_codigo.clear()
                self.ctrl_categoria.clear()
                self.ctrl_modelo.clear()
                self.ctrl_stock.clear()
                self.ctrl_fecha.clear()
                self.ctrl_precio.clear()
                self.ctrl_precio_min.clear()
                self.ctrl_precio_max.clear()
            elif (str(respuesta_historial) != '<Response [200]>') and (str(respuesta_inventario) == '<Response [200]>'):
                self.ctrl_mensaje.setText('Fallo server: insertado historial error')
                self.ctrl_codigo.clear()
                self.ctrl_categoria.clear()
                self.ctrl_modelo.clear()
                self.ctrl_stock.clear()
                self.ctrl_fecha.clear()
                self.ctrl_precio.clear()
                self.ctrl_precio_min.clear()
                self.ctrl_precio_max.clear()
            elif (str(respuesta_historial) == '<Response [200]>') and (str(respuesta_inventario) != '<Response [200]>'):
                self.ctrl_mensaje.setText('Fallo server: insertado inventario error')
                self.ctrl_codigo.clear()
                self.ctrl_categoria.clear()
                self.ctrl_modelo.clear()
                self.ctrl_stock.clear()
                self.ctrl_fecha.clear()
                self.ctrl_precio.clear()
                self.ctrl_precio_min.clear()
                self.ctrl_precio_max.clear()  
        recibir_inventario = requests.get('http://localhost:8000/inventario_recibir')
        list_recibir_inventario = list(recibir_inventario.json())
        list_dict_inventario = [dict(dict_inventario) for dict_inventario in list_recibir_inventario]
        self.suma_total_almacen = 0.00
        for t in range(1,len(list_dict_inventario)): 
            self.suma_total_almacen = round(float(list_dict_inventario[t]['precio']) + self.suma_total_almacen,3)
        self.ctrl_total_almacen.setText(str(self.suma_total_almacen) + ' €')
    def OnClickedNuevo(self):        
        self.ctrl_mensaje.clear()
        self.n_pulsado_nuevo += 1 
        if self.n_pulsado_nuevo == 1:
            
            self.ctrl_codigo.setText('-> Codigo...')
            self.ctrl_categoria.setText('-> Categoria...')
            self.ctrl_modelo.setText('-> Modelo...')
            self.ctrl_stock.setText('-> Stock...')
            self.ctrl_fecha.setText('Auto')
            self.ctrl_precio.setText('-> Precio...')
            self.ctrl_precio_min.setText('Auto')
            self.ctrl_precio_max.setText('Auto')
            print('Esperando datos para el envio...')
            self.ctrl_mensaje.setText('Ahora puede rellenar el nuevo item...')

        if self.n_pulsado_nuevo == 2:
            fecha_now = self.fecha_actual()
            nuevo_item = {
                'codigo':str(self.ctrl_codigo.text()),
                'categoria':str(self.ctrl_categoria.text()),
                'modelo': str(self.ctrl_modelo.text()),
                'stock': int(self.ctrl_stock.text()),
                'fecha': fecha_now,
                'precio': round(float(self.ctrl_precio.text()),3),
                'precio_min': round(float(self.ctrl_precio.text()),3),
                'precio_max': round(float(self.ctrl_precio.text()),3)

            }
            respuesta_nuevo_item = requests.post('http://localhost:8000/inventario', data=json.dumps(nuevo_item))
            respuesta_historial = requests.post('http://localhost:8000/historial_precios', data=json.dumps(nuevo_item))
            self.n_pulsado_nuevo = 0
            print('Nuevo item enviado a Inventario')
            
            if (str(respuesta_nuevo_item) == '<Response [200]>') and (str(respuesta_historial) == '<Response [200]>'):
                self.ctrl_mensaje.setText('Insertado nuevo OK')
                self.ctrl_codigo.clear()
                self.ctrl_categoria.clear()
                self.ctrl_modelo.clear()
                self.ctrl_stock.clear()
                self.ctrl_fecha.clear()
                self.ctrl_precio.clear()
                self.ctrl_precio_min.clear()
                self.ctrl_precio_max.clear()
            else:
                self.ctrl_mensaje.setText('Fallo server')
                self.ctrl_codigo.clear()
                self.ctrl_categoria.clear()
                self.ctrl_modelo.clear()
                self.ctrl_stock.clear()
                self.ctrl_fecha.clear()
                self.ctrl_precio.clear()
                self.ctrl_precio_min.clear()
                self.ctrl_precio_max.clear()
            
            recibir_inventario = requests.get('http://localhost:8000/inventario_recibir')
            list_recibir_inventario = list(recibir_inventario.json())
            list_dict_inventario = [dict(dict_inventario) for dict_inventario in list_recibir_inventario]
            nueva_list_categorias = []
            for i in range(1,len(list_dict_inventario)):    
                id_item = list_dict_inventario[i]
                id_item_anterior = list_dict_inventario[i-1]
                if len(nueva_list_categorias)>0:
                    if id_item_anterior['categoria'] != id_item['categoria']:
                        n_nueva_list_categorias = 0
                        for l in range(0,len(nueva_list_categorias)):
                            if id_item['categoria'] != nueva_list_categorias[l]:
                                n_nueva_list_categorias += 1                          
                        if n_nueva_list_categorias == len(nueva_list_categorias):
                            nueva_list_categorias.append(id_item['categoria'])                              
                if len(nueva_list_categorias) == 0:
                        nueva_list_categorias.append(id_item['categoria'])    
            list_categorias = []
            if self.primer_ciclo_categorias == True:
                if len(self.nueva_list_categorias_antigua) != len(nueva_list_categorias):
                    nueva_categoria = nueva_list_categorias[len(nueva_list_categorias)-1]
                    list_categorias.append(nueva_categoria)
                    print(f'La nueva lista de categorias es: {nueva_list_categorias} ')
                    print(f'La nueva categoria es: {nueva_categoria}')
            
            if self.primer_ciclo_categorias == False:
                if len(self.list_categorias) != len(nueva_list_categorias):
                    nueva_categoria = nueva_list_categorias[len(nueva_list_categorias)-1]
                    list_categorias.append(nueva_categoria)
                    self.primer_ciclo_categorias = True
                    print(f'La nueva lista de categorias es: {nueva_list_categorias} ')
                    print(f'La nueva categoria es: {nueva_categoria}')
            self.list_categorias.sort()
            self.cbbox_categorias.addItems(list_categorias)
            self.nueva_list_categorias_antigua = nueva_list_categorias
            self.suma_total_almacen = 0.00
            for t in range(1,len(list_dict_inventario)): 
                self.suma_total_almacen = round(float(list_dict_inventario[t]['precio']) + self.suma_total_almacen,3)
            self.ctrl_total_almacen.setText(str(self.suma_total_almacen) + ' €')

    def OnPressed_Busqueda_modelo(self):
        busqueda_modelos = self.ctrl_busqueda_modelo.text()
        minus_busqueda_modelos = busqueda_modelos.lower()
        recibir_inventario = requests.get('http://localhost:8000/inventario_recibir')
        json_recibir_inventario = recibir_inventario.json()
        list_json_inventario = [dict(id_item) for id_item in json_recibir_inventario]
        list_modelos = []
        
        for i in range(0,len(list_json_inventario)):
            dict_list_json_inventario = list_json_inventario[i]
            list_dividido = []
            list_dividido = dict_list_json_inventario['modelo'].lower().split()
            #print(f'Lista dividida de modelo: {minus_busqueda_modelos} es {list_dividido}')
            for d in range(0,len(list_dividido)):
                if minus_busqueda_modelos == list_dividido[d]:
                    list_modelos.append(dict_list_json_inventario)
        print(f'La lista recibida de modelos "{minus_busqueda_modelos}" es:\n{list_modelos}')
        codigo=[]
        categoria=[]
        modelo=[]
        stock=[]
        fecha=[]
        precio=[]
        precio_min = []
        precio_max = []
        for a in range (0,len(list_modelos)):
            dict_mostrar = list_modelos[a]

            item_codigo = dict_mostrar['codigo']
            item_categoria = dict_mostrar['categoria']
            item_modelo = dict_mostrar['modelo']
            item_stock = dict_mostrar['stock']
            item_fecha = dict_mostrar['fecha']
            item_precio = dict_mostrar['precio']
            item_precio_min = dict_mostrar['precio_min']
            item_precio_max =  dict_mostrar['precio_max']

            codigo.append(item_codigo)            
            categoria.append(item_categoria)
            modelo.append(item_modelo)
            stock.append(item_stock)
            fecha.append(item_fecha)
            precio.append(item_precio)
            precio_min.append(item_precio_min)
            precio_max.append(item_precio_max)

        self.data_categoria = {
            'Codigo': codigo,
            'Categoria': categoria,
            'Modelo':modelo,
            'Stock':stock,
            'Fecha':fecha,
            'Precio':precio,
            'Precio_min': precio_min,
            'Precio_max':precio_max
        }
        #print(f'Los datos seleccionados son: {self.data_categoria}')
        self.tabla_resultado.clear()
        self.tabla_resultado.setHorizontalHeaderLabels(['Codigo','Categoria','Modelo','Stock','Ultima Modificacion', 'Precio','Precio min','Precio max'])
        for n, key in enumerate(self.data_categoria.keys()):
            for m, item in enumerate(self.data_categoria[key]):
                #newitem = QTableWidgetItem(item)
                #self.setItem(m, n, newitem)
                self.tabla_resultado.setItem(m,n,QTableWidgetItem(item))
        self.tabla_resultado.verticalHeader().setDefaultSectionSize(80)
        self.suma_total_busqueda = 0.00
        for t in range(0,len(list_modelos)): 
            self.suma_total_busqueda= round(float(list_modelos[t]['precio']) + self.suma_total_busqueda,3)
        self.ctrl_total_busqueda.setText(str(self.suma_total_busqueda) + ' €')
        self.ctrl_total_categoria.clear()

    def OnClickedBorrar(self):
        self.busqueda_codigo = self.ctrl_buscar_codigo.text()
        #print(f'Busqueda codigo -> {self.busqueda_codigo}\n')
        self.enviar()
        id_borrar = {
            "id_borrar_item": str(self.dict_recibir_busqueda['id']),
            "codigo_borrar_item": self.busqueda_codigo
            }
        requests.post('http://localhost:8000/borrar_item', data= json.dumps(id_borrar))
        self.ctrl_mensaje.clear()
        self.ctrl_mensaje.setText(f'Codigo {self.busqueda_codigo} eliminado OK')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = gui_gestor_almacen()
    GUI.show()
    sys.exit(app.exec_())
