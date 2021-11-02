import wx
import requests
import json
from time import sleep
from ObjectListView import ObjectListView, ColumnDefn


class interfaz(wx.Frame):
    categoria_sel : str = 'vacio_0000'
    busqueda_codigo : str = 'vacio_0000'
    

    def __init__(self, *args, **kw):
        super(interfaz, self).__init__(*args, **kw)
    
        
        self.InitUI()
        self.Centre()

    def InitUI(self):

        self.pnl = wx.Panel(self)
        self.n_pulsado_nuevo = 0
        self.ip_server = 'http://0.0.0.0:8000/'
        
        ## VENTANA ##       
        self.SetSize(1080,1080)
        self.SetTitle('GESTION ALMACEN by Michel Alvarez')  
        self.SetBackgroundColour((237, 237, 227))
        

        self.sizer = wx.GridBagSizer(16,5)
        

        ## Titulo
        self.fuente_titulo = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        self.titulo= wx.StaticText(self.pnl, label= 'GESTION ALMACEN')
        self.titulo.SetFont(self.fuente_titulo)
        self.titulo.SetForegroundColour(wx.Colour(0,0,0))
        self.sizer.Add(self.titulo, pos=(0, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTER)
        ### Boton Cerrar ###
        self.closeButton = wx.Button(self.pnl, label='Cerrar')   
        self.closeButton.Bind(wx.EVT_BUTTON, self.OnClickedCerrar)
        self.closeButton.SetForegroundColour(wx.Colour(255,255,255))   
        self.closeButton.SetBackgroundColour(wx.Colour(0,0,0)) 
        self.sizer.Add(self.closeButton, pos=(1, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTER)

        ## Base de datos completa
        #self.ctrl_basedatos = wx.TextCtrl(self.pnl,size=(400,1000),style = wx.TE_MULTILINE)
        #self.sizer.Add(self.ctrl_basedatos, pos=(2, 4), flag=wx.ALIGN_CENTRE)

        ## Listado 
        self.txt_listado= wx.StaticText(self.pnl, label= 'Listado')
        self.txt_listado.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_listado, pos=(11, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTER)

        self.ctrl_buscar= wx.TextCtrl(self.pnl, size= (120,30),style = wx.TE_PROCESS_ENTER)
        self.ctrl_buscar.Bind(wx.EVT_TEXT_ENTER,self.OnEnterPressedBuscar)
        self.ctrl_buscar.SetValue('Buscar...')
        self.sizer.Add(self.ctrl_buscar, pos=(2, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTER)
        
        recibir_inventario = requests.get('http://0.0.0.0:8000/inventario_recibir')
        list_recibir_inventario = list(recibir_inventario.json())
        print(list_recibir_inventario)
        list_categorias = []
        list_dict_inventario = [dict(dict_inventario) for dict_inventario in list_recibir_inventario]
        print(list_dict_inventario)
        igual_categoria = False
        for i in range(0,len(list_dict_inventario)):    
            if i != 0:
                id_list = list_dict_inventario[i]
                nom_categoria = id_list['categoria']
                print(nom_categoria)
                dict_item_inventario = list_dict_inventario[i-1]
                if nom_categoria != dict_item_inventario['categoria']:
                    for l in range(0,len(list_categorias)):
                        if nom_categoria == list_categorias[l]:
                            igual_categoria = True
                            print(igual_categoria)
                    if igual_categoria == False:
                        list_categorias.append(nom_categoria)                       
        print(f'La lista de categorias es: {list_categorias}')
        print(len(list_dict_inventario))
                
        self.categoria =  list_categorias
        self.cbbox_categoria = wx.ComboBox(self,-1,choices= self.categoria,size=(120,30))
        self.Bind(wx.EVT_COMBOBOX, self.OnSelect)
        self.sizer.Add(self.cbbox_categoria, pos=(12, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTER)

        #self.resultado = wx.ListCtrl(self.pnl,-1, style = wx.LC_REPORT)
        self.resultado = ObjectListView(self.pnl, wx.ID_ANY, style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.resultado.SetColumns([
                ColumnDefn("Codigo", "left", 90,"codigo"),
                ColumnDefn("Categoria", "center", 100,"categoria"),
                ColumnDefn("Modelo", "left", 200,"modelo"),
                ColumnDefn("Stock", "center", 90,"stock"),
                ColumnDefn("Fecha", "center", 100,"fecha")
            ])
        self.sizer.Add(self.resultado, pos=(14, 1), flag=wx.ALIGN_CENTRE)
        ## Referenciado
        self.txt_referenciado= wx.StaticText(self.pnl, label= 'Referenciado')
        self.txt_referenciado.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_referenciado, pos=(3, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTER)

        self.ctrl_buscar_codigo= wx.TextCtrl(self.pnl, size= (120,30),style= wx.TE_PROCESS_ENTER)
        self.ctrl_buscar_codigo.Bind(wx.EVT_TEXT_ENTER,self.OnEnterPressedCodigo)
        self.ctrl_buscar_codigo.SetValue('Codigo...') 
        self.sizer.Add(self.ctrl_buscar_codigo, pos=(4, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTER)

        self.txt_codigo= wx.StaticText(self.pnl, label= 'Codigo')
        self.txt_codigo.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_codigo, pos=(5, 0),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)
        
        self.ctrl_codigo= wx.TextCtrl(self.pnl, size= (120,60),style = wx.TE_MULTILINE)
        self.sizer.Add(self.ctrl_codigo, pos=(6, 0),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)

        self.txt_categoria= wx.StaticText(self.pnl, label= 'Categoria')
        self.txt_categoria.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_categoria, pos=(5, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)
        
        self.ctrl_categoria= wx.TextCtrl(self.pnl, size= (120,60),style = wx.TE_MULTILINE)
        self.sizer.Add(self.ctrl_categoria, pos=(6, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)

        self.txt_modelo= wx.StaticText(self.pnl, label= 'Modelo')
        self.txt_modelo.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_modelo, pos=(5, 2),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)

        self.ctrl_modelo= wx.TextCtrl(self.pnl, size= (120,60),style = wx.TE_MULTILINE)
        self.sizer.Add(self.ctrl_modelo, pos=(6, 2),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)

        self.txt_stock= wx.StaticText(self.pnl, label= 'Stock')
        self.txt_stock.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_stock, pos=(7, 0),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)

        self.ctrl_stock= wx.TextCtrl(self.pnl, size= (120,60),style = wx.TE_MULTILINE)
        self.sizer.Add(self.ctrl_stock, pos=(8, 0),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)

        self.txt_fecha= wx.StaticText(self.pnl, label= 'Ultima modificacion')
        self.txt_fecha.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_fecha, pos=(7, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)

        self.ctrl_fecha= wx.TextCtrl(self.pnl, size= (120,60),style = wx.TE_MULTILINE)
        self.sizer.Add(self.ctrl_fecha, pos=(8, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)
        #Modificar y refrescar
        self.modificarButton = wx.Button(self.pnl, label='Modificar', size= (90,30))   
        self.modificarButton.Bind(wx.EVT_BUTTON, self.OnClickedModificar) 
        self.modificarButton.SetBackgroundColour(wx.Colour(0,0,0))
        self.modificarButton.SetForegroundColour(wx.Colour(255,255,255))
        self.sizer.Add(self.modificarButton, pos=(9, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)

        self.nuevoButton = wx.Button(self.pnl, label='NUEVO', size= (90,30))   
        self.nuevoButton.Bind(wx.EVT_BUTTON, self.OnClickedNuevo) 
        self.nuevoButton.SetBackgroundColour(wx.Colour(0,0,0))
        self.nuevoButton.SetForegroundColour(wx.Colour(255,255,255))
        self.sizer.Add(self.nuevoButton, pos=(10, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)

        #Logo
        self.imagen1 = wx.Image('logo1.png', wx.BITMAP_TYPE_PNG).Rescale(150, 150).ConvertToBitmap() 
        #self.logo1= wx.StaticBitmap(self.pnl, -1, self.imagen1)
        #self.sizer.Add(self.logo1, pos=(0, 0),span=wx.DefaultSpan, flag=wx.ALIGN_CENTER)

        
        #self.logo2= wx.StaticBitmap(self.pnl, -1, self.imagen1)
        #self.sizer.Add(self.logo2, pos=(0, 2),span=wx.DefaultSpan, flag=wx.ALIGN_CENTER)

        ## Imagen
        self.imagen_grande= wx.StaticBitmap(self.pnl,-1, self.imagen1)
        self.sizer.Add(self.imagen_grande, pos=(15, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTER)

        #self.sizer.AddGrowableCol(4)
        
        
        
        

        self.SetSizerAndFit(self.sizer)
        
        
                                   
    

    def OnClose(self,e):                                
        self.Close(True)
    def OnClickedCerrar(self,e):                             
        print("El boton de CERRAR ha sido presionado")     
        self.OnClose(True)
    
    def OnSelect(self,event):
        self.categoria_sel = self.cbbox_categoria.GetValue()
        recibir_inventario = requests.get('http://0.0.0.0:8000/inventario_recibir')
        json_recibir_inventario = recibir_inventario.json()
        list_json_inventario = [dict(id_item) for id_item in json_recibir_inventario]
        list_mostrar = []
        for i in range(0,len(list_json_inventario)):
            dict_list_json_inventario = list_json_inventario[i]
            if self.categoria_sel == dict_list_json_inventario['categoria']:
                list_mostrar.append(dict_list_json_inventario)
        self.resultado.SetObjects(list_mostrar)
        '''
        if self.categoria_sel == 'Electricidad':
            muestra_electricidad = requests.get('http://0.0.0.0:8000/electricidad_mostrar')
            list_muestra_electricidad = muestra_electricidad.json()
            print(list_muestra_electricidad)
            list_separada_electricidad = [i for i in list_muestra_electricidad[1:]]
            self.resultado.SetObjects(list_separada_electricidad)
        if self.categoria_sel == 'Neumatica':
            muestra_neumatica = requests.get('http://0.0.0.0:8000/neumatica_mostrar')
            list_muestra_neumatica = muestra_neumatica.json()
            print(list_muestra_neumatica)
            list_separada_neumatica = [i for i in list_muestra_neumatica[1:]]
            self.resultado.SetObjects(list_separada_neumatica)
        '''
    def OnEnterPressedBuscar(self,event):
        self.busqueda = self.ctrl_buscar.GetValue() 
        print(f'Se ha buscado {self.busqueda}')

    def enviar(self,e):
        envio = {
            "busc":self.busqueda_codigo
        }
        respuesta_envio = requests.post('http://0.0.0.0:8000/envios', data=json.dumps(envio))
        #print(f'Respuesta del requests -> {respuesta_envio.json()}')
        print(f'Envio -> {envio}')
        self.busqueda_codigo = 'vacio_0000'
        sleep(1)
        list_recibir_busqueda = requests.post('http://0.0.0.0:8000/envios_recibir')
        print(list_recibir_busqueda)
        data_list_recibir_busqueda=list_recibir_busqueda.json()
        print(data_list_recibir_busqueda)
        if data_list_recibir_busqueda[0]['busc'] != 'vacio_0000':
            dict_recibir_busqueda = data_list_recibir_busqueda[1]
            self.ctrl_codigo.SetValue(dict_recibir_busqueda['codigo'])
            self.ctrl_categoria.SetValue(dict_recibir_busqueda['categoria'])
            self.ctrl_modelo.SetValue(dict_recibir_busqueda['modelo'])
            self.ctrl_stock.SetValue(str(dict_recibir_busqueda['stock']))
            self.ctrl_fecha.SetValue(dict_recibir_busqueda['fecha'])
    def OnEnterPressedCodigo(self,event):
        print('Se ha introducido codigo para buscar')
        self.busqueda_codigo = self.ctrl_buscar_codigo.GetValue()
        print(f'Busqueda codigo -> {self.busqueda_codigo}\n')
        self.enviar(True)
        
        

    def OnClickedModificar(self,event):
        print('Se ha pulsado boton Modificar')

    

    def OnClickedNuevo(self,event):        
        self.n_pulsado_nuevo += 1 
        if self.n_pulsado_nuevo == 1:
            
            self.ctrl_codigo.SetValue('-> Codigo nuevo...')
            self.ctrl_categoria.SetValue('-> Categoria nuevo...')
            self.ctrl_modelo.SetValue('-> Modelo nuevo...')
            self.ctrl_stock.SetValue('-> Stock nuevo...')
            self.ctrl_fecha.SetValue('-> Fecha nuevo...')
            print('Esperando datos para el envio...')


        if self.n_pulsado_nuevo == 2:
            nuevo_item = {
                'codigo':str(self.ctrl_codigo.GetValue()),
                'categoria':str(self.ctrl_categoria.GetValue()),
                'modelo': str(self.ctrl_modelo.GetValue()),
                'stock': str(self.ctrl_stock.GetValue()),
                'fecha': str(self.ctrl_fecha.GetValue())
            }
            respuesta_nuevo_item = requests.post('http://0.0.0.0:8000/inventario', data=json.dumps(nuevo_item))
            self.n_pulsado_nuevo = 0
            print('Nuevo item enviado a Inventario')
            print(respuesta_nuevo_item)
            if str(respuesta_nuevo_item) == '<Response [200]>':
                self.ctrl_codigo.SetValue('Insertado OK')
                self.ctrl_categoria.SetValue(' ')
                self.ctrl_modelo.SetValue(' ')
                self.ctrl_stock.SetValue(' ')
                self.ctrl_fecha.SetValue(' ')
            else:
                self.ctrl_categoria.SetValue('Fallo envio server')
                self.ctrl_codigo.SetValue(' ')
                self.ctrl_modelo.SetValue(' ')
                self.ctrl_stock.SetValue(' ')
                self.ctrl_fecha.SetValue(' ')
            '''
            recibir_inventario = requests.get('http://0.0.0.0:8000/inventario_recibir')
            list_recibir_inventario = list(recibir_inventario.json())
            list_categorias = []
            list_dict_inventario = [dict(dict_inventario) for dict_inventario in list_recibir_inventario]
            igual_categoria = False
            for i in range(0,len(list_dict_inventario)):    
                if i != 0:
                    id_list = list_dict_inventario[i]
                    nom_categoria = id_list['categoria']
                    dict_item_inventario = list_dict_inventario[i-1]
                    if nom_categoria != dict_item_inventario['categoria']:
                        for l in range(0,len(list_categorias)):
                            if nom_categoria == list_categorias[l]:
                                igual_categoria = True  
                        if igual_categoria == False:
                            list_categorias.append(nom_categoria)                       
            print(f'La lista de categorias es: {list_categorias}')
                    
            self.categoria =  list_categorias
            self.cbbox_categoria = wx.ComboBox(self,-1,choices= self.categoria,size=(120,30))
            '''




def main():

    app = wx.App()
    ex = interfaz(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()