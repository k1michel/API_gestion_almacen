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
        print(list_recibir_inventario)
        list_dict_inventario = [dict(dict_inventario) for dict_inventario in list_recibir_inventario]
        print(list_dict_inventario)
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
        print(f'La lista de categorias es: {self.list_categorias} ')
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
        print(f'Los datos seleccionados son: {self.data_categoria}')
        self.tabla_resultado.clear()
        self.tabla_resultado.setHorizontalHeaderLabels(['Codigo','Categoria','Modelo','Stock','Ultima Modificacion', 'Precio'])
        for n, key in enumerate(self.data_categoria.keys()):
            for m, item in enumerate(self.data_categoria[key]):
                #newitem = QTableWidgetItem(item)
                #self.setItem(m, n, newitem)
                self.tabla_resultado.setItem(m,n,QTableWidgetItem(item))
        self.tabla_resultado.verticalHeader().setDefaultSectionSize(80)
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = gui_gestor_almacen()
    GUI.show()
    sys.exit(app.exec_())
