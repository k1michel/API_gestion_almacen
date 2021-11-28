import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import requests
import json
from time import sleep
from datetime import datetime
from ObjectListView import ObjectListView, ColumnDefn

class gui_gestor_almacen(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI_Gestor_almacen.ui",self)
        self.ctrl_buscar_codigo.editingFinished.connect(self.OnEnterPressedCodigo)

    def enviar(self):
        envio = {
            "busc":self.busqueda_codigo
        }
        respuesta_envio = requests.post('http://localhost:8000/envios', data=json.dumps(envio))
        #print(f'Respuesta del requests -> {respuesta_envio.json()}')
        print(f'Envio -> {envio}')
        self.busqueda_codigo = 'vacio_0000'
        sleep(1)
        list_recibir_busqueda = requests.post('http://localhost:8000/envios_recibir')
        print(list_recibir_busqueda)
        data_list_recibir_busqueda=list_recibir_busqueda.json()
        print(data_list_recibir_busqueda)
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = gui_gestor_almacen()
    GUI.show()
    sys.exit(app.exec_())
