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
        pixmap = QPixmap('Letras_gestor_almacen_1.png')
        self.imagen_app.setPixmap(pixmap)
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
        
        ## BUSCAR CODIGO ##

        self.ctrl_buscar_codigo.editingFinished.connect(self.OnEnterPressedCodigo)
        #################################################

        ## TABLA DE RESULTADOS ##
        self.tabla_resultado.setColumnCount(6)
        self.tabla_resultado.setRowCount(50)
        self.tabla_resultado.setHorizontalHeaderLabels(['Codigo','Categoria','Modelo','Stock','Ultima Modificacion', 'Precio'])
        self.tabla_resultado.horizontalHeader().setSectionResizeMode(90)
        ####################################################
        
        ##BOTON MODIFICAR ##
        self.boton_modificar.clicked.connect(self.OnClickedModificar)
        #####################################################

        ## BOTON NUEVO ##
        self.boton_nuevo.clicked.connect(self.OnClickedNuevo)
        #####################################################


        ## VARIABLES AUXILIARES ##
        self.n_pulsado_nuevo = 0
        self.n_pulsado_modificar = 0
        self.primer_ciclo_categorias = False
        self.nueva_list_categorias_antigua = []

        ######################################################
    def enviar(self):
        envio = {
            "busc":self.busqueda_codigo
        }
        respuesta_envio = requests.post('http://localhost:8000/envios', data=json.dumps(envio))
        #print(f'Respuesta del requests -> {respuesta_envio.json()}')
        #print(f'Envio -> {envio}')
        self.busqueda_codigo = 'vacio_0000'
        sleep(1)
        list_recibir_busqueda = requests.post('http://localhost:8000/envios_recibir')
        data_list_recibir_busqueda=list_recibir_busqueda.json()
        #print(data_list_recibir_busqueda)
        if data_list_recibir_busqueda[0]['busc'] != 'vacio_0000':
            self.dict_recibir_busqueda = data_list_recibir_busqueda[1]
            self.ctrl_codigo.setText(self.dict_recibir_busqueda['codigo'])
            self.ctrl_categoria.setText(self.dict_recibir_busqueda['categoria'])
            self.ctrl_modelo.setText(self.dict_recibir_busqueda['modelo'])
            self.ctrl_stock.setText(str(self.dict_recibir_busqueda['stock']))
            self.ctrl_fecha.setText(self.dict_recibir_busqueda['fecha'])
            self.ctrl_precio.setText(self.dict_recibir_busqueda['precio'])
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
        for a in range (0,len(list_mostrar)):
            dict_mostrar = list_mostrar[a]

            item_codigo = dict_mostrar['codigo']
            item_categoria = dict_mostrar['categoria']
            item_modelo = dict_mostrar['modelo']
            item_stock = dict_mostrar['stock']
            item_fecha = dict_mostrar['fecha']
            item_precio = dict_mostrar['precio'] 

            codigo.append(item_codigo)            
            categoria.append(item_categoria)
            modelo.append(item_modelo)
            stock.append(item_stock)
            fecha.append(item_fecha)
            precio.append(item_precio)

        self.data_categoria = {
            'Codigo': codigo,
            'Categoria': categoria,
            'Modelo':modelo,
            'Stock':stock,
            'Fecha':fecha,
            'Precio':precio
        }
        #print(f'Los datos seleccionados son: {self.data_categoria}')
        self.tabla_resultado.clear()
        self.tabla_resultado.setHorizontalHeaderLabels(['Codigo','Categoria','Modelo','Stock','Ultima Modificacion', 'Precio'])
        for n, key in enumerate(self.data_categoria.keys()):
            for m, item in enumerate(self.data_categoria[key]):
                #newitem = QTableWidgetItem(item)
                #self.setItem(m, n, newitem)
                self.tabla_resultado.setItem(m,n,QTableWidgetItem(item))
        self.tabla_resultado.verticalHeader().setDefaultSectionSize(80)
        
    def fecha_actual(self):
        ahora = datetime.now()
        formato = "%Y-%m-%d_%H:%M:%S"
        fecha_hora_actual = ahora.strftime(formato)
        return fecha_hora_actual
        

    def OnClickedModificar(self):
        print('Se ha pulsado boton Modificar')
        self.n_pulsado_modificar += 1
        if self.n_pulsado_modificar == 1:

            self.busqueda_codigo = self.ctrl_buscar_codigo.text()
            print(f'Busqueda codigo -> {self.busqueda_codigo}\n')
            self.enviar()
            id_modificar = {
                "id_modificar": str(self.dict_recibir_busqueda['id'])
            }
            #print(id_modificar)
            requests.post('http://localhost:8000/modificar', data= json.dumps(id_modificar))
            print('Esperando modificacion...')
            
            self.ctrl_fecha.setText('Automatica')
        if self.n_pulsado_modificar == 2:
            fecha_now = self.fecha_actual()
            nuevo_item = {
                    'codigo':str(self.ctrl_codigo.text()),
                    'categoria':str(self.ctrl_categoria.text()),
                    'modelo': str(self.ctrl_modelo.text()),
                    'stock': str(self.ctrl_stock.text()),
                    'fecha': fecha_now,
                    'precio':str(self.ctrl_precio.text())
                }
            respuesta_nuevo_item = requests.post('http://localhost:8000/inventario', data=json.dumps(nuevo_item))
            self.n_pulsado_modificar = 0
            if str(respuesta_nuevo_item) == '<Response [200]>':
                    self.ctrl_codigo.setText('Modificar OK')
                    self.ctrl_categoria.setText(' ')
                    self.ctrl_modelo.setText(' ')
                    self.ctrl_stock.setText(' ')
                    self.ctrl_fecha.setText(' ')
                    self.ctrl_precio.setText('')
                    

    

    def OnClickedNuevo(self):        
        self.n_pulsado_nuevo += 1 
        if self.n_pulsado_nuevo == 1:
            
            self.ctrl_codigo.setText('-> Codigo nuevo...')
            self.ctrl_categoria.setText('-> Categoria nuevo...')
            self.ctrl_modelo.setText('-> Modelo nuevo...')
            self.ctrl_stock.setText('-> Stock nuevo...')
            self.ctrl_fecha.setText('Automatica')
            self.ctrl_precio.setText('-> Precio nuevo...')
            print('Esperando datos para el envio...')


        if self.n_pulsado_nuevo == 2:
            fecha_now = self.fecha_actual()
            nuevo_item = {
                'codigo':str(self.ctrl_codigo.text()),
                'categoria':str(self.ctrl_categoria.text()),
                'modelo': str(self.ctrl_modelo.text()),
                'stock': str(self.ctrl_stock.text()),
                'fecha': fecha_now,
                'precio':str(self.ctrl_precio.text())
            }
            respuesta_nuevo_item = requests.post('http://localhost:8000/inventario', data=json.dumps(nuevo_item))
            self.n_pulsado_nuevo = 0
            print('Nuevo item enviado a Inventario')
            
            if str(respuesta_nuevo_item) == '<Response [200]>':
                self.ctrl_codigo.setText('Insertado OK')
                self.ctrl_categoria.setText(' ')
                self.ctrl_modelo.setText(' ')
                self.ctrl_stock.setText(' ')
                self.ctrl_fecha.setText(' ')
                self.ctrl_precio.setText('')
            else:
                self.ctrl_categoria.setText('Fallo envio server')
                self.ctrl_codigo.setText(' ')
                self.ctrl_modelo.setText(' ')
                self.ctrl_stock.setText(' ')
                self.ctrl_fecha.setText(' ')
                self.ctrl_precio.setText(' ')
            
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = gui_gestor_almacen()
    GUI.show()
    sys.exit(app.exec_())
