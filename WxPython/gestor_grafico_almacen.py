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
        
        ## VENTANA ##       
        self.SetSize(1080,1080)
        self.SetTitle('GESTOR ALMACEN')  
        self.SetBackgroundColour((232, 249, 210))
        
        #Variables
        self.n_pulsado_nuevo = 0
        self.ip_server = 'http://0.0.0.0:8000/'
        self.primer_ciclo_categorias = False
        self.nueva_list_categorias_antigua = []

        self.sizer = wx.GridBagSizer(17,5)
        

        ## Titulo
        self.fuente_titulo = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        self.titulo= wx.StaticText(self.pnl, label= 'GESTOR ALMACEN')
        self.titulo.SetFont(self.fuente_titulo)
        self.titulo.SetForegroundColour(wx.Colour(0,0,0))
        self.sizer.Add(self.titulo, pos=(0, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTER)
        
        ### Boton Cerrar ###
        '''
        self.closeButton = wx.Button(self.pnl, label='Cerrar')   
        self.closeButton.Bind(wx.EVT_BUTTON, self.OnClickedCerrar)
        self.closeButton.SetForegroundColour(wx.Colour(255,255,255))   
        self.closeButton.SetBackgroundColour(wx.Colour(0,0,0)) 
        self.sizer.Add(self.closeButton, pos=(1, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTER)
        '''

        ## Listado 
        self.txt_listado= wx.StaticText(self.pnl, label= 'Listado')
        self.txt_listado.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_listado, pos=(12, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTER)

        self.ctrl_buscar= wx.TextCtrl(self.pnl, size= (120,30),style = wx.TE_PROCESS_ENTER)
        self.ctrl_buscar.Bind(wx.EVT_TEXT_ENTER,self.OnEnterPressedBuscar)
        self.ctrl_buscar.SetValue('Buscar...')
        self.sizer.Add(self.ctrl_buscar, pos=(2, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTER)
        
        ## LINEA
        self.linea1 = wx.StaticLine(self, size=(500,2))
        self.sizer.Add(self.linea1, pos=(3, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTER)
        
        ## LISTA DESPLEGABLE CATEGORIAS

        recibir_inventario = requests.get('http://0.0.0.0:8000/inventario_recibir')
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
        
        
                
        self.categoria =  self.list_categorias
        self.cbbox_categoria = wx.ComboBox(self,-1,choices= self.categoria,size=(120,30))
        self.Bind(wx.EVT_COMBOBOX, self.OnSelect)
        self.sizer.Add(self.cbbox_categoria, pos=(13, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTER)

        
        self.resultado = ObjectListView(self.pnl, wx.ID_ANY, style=wx.LC_REPORT|wx.SUNKEN_BORDER,size=(600,200))
        self.resultado.SetColumns([
                ColumnDefn("Codigo", "center", 50,"codigo"),
                ColumnDefn("Categoria", "center", 100,"categoria"),
                ColumnDefn("Modelo", "center", 250,"modelo"),
                ColumnDefn("Stock", "center", 50,"stock"),
                ColumnDefn("Fecha", "center", 100,"fecha"),
                ColumnDefn("Precio", "center", 50,"precio")

            ])
        self.sizer.Add(self.resultado, pos=(15, 1), flag=wx.ALIGN_CENTRE)
        
        ## Referenciado
        self.txt_referenciado= wx.StaticText(self.pnl, label= 'Referenciado')
        self.txt_referenciado.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_referenciado, pos=(4, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTER)

        self.ctrl_buscar_codigo= wx.TextCtrl(self.pnl, size= (120,30),style= wx.TE_PROCESS_ENTER)
        self.ctrl_buscar_codigo.Bind(wx.EVT_TEXT_ENTER,self.OnEnterPressedCodigo)
        self.ctrl_buscar_codigo.SetValue('Codigo...') 
        self.sizer.Add(self.ctrl_buscar_codigo, pos=(5, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTER)

        self.txt_codigo= wx.StaticText(self.pnl, label= 'Codigo')
        self.txt_codigo.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_codigo, pos=(6, 0),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)
        
        self.ctrl_codigo= wx.TextCtrl(self.pnl, size= (120,60),style = wx.TE_MULTILINE)
        self.sizer.Add(self.ctrl_codigo, pos=(7, 0),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)

        self.txt_categoria= wx.StaticText(self.pnl, label= 'Categoria')
        self.txt_categoria.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_categoria, pos=(6, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)
        
        self.ctrl_categoria= wx.TextCtrl(self.pnl, size= (120,60),style = wx.TE_MULTILINE)
        self.sizer.Add(self.ctrl_categoria, pos=(7, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)

        self.txt_modelo= wx.StaticText(self.pnl, label= 'Modelo')
        self.txt_modelo.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_modelo, pos=(6, 2),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)

        self.ctrl_modelo= wx.TextCtrl(self.pnl, size= (120,60),style = wx.TE_MULTILINE)
        self.sizer.Add(self.ctrl_modelo, pos=(7, 2),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)

        self.txt_stock= wx.StaticText(self.pnl, label= 'Stock')
        self.txt_stock.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_stock, pos=(8, 0),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)

        self.ctrl_stock= wx.TextCtrl(self.pnl, size= (120,60),style = wx.TE_MULTILINE)
        self.sizer.Add(self.ctrl_stock, pos=(9, 0),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)

        self.txt_fecha= wx.StaticText(self.pnl, label= 'Ultima modificacion')
        self.txt_fecha.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_fecha, pos=(8, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)

        self.ctrl_fecha= wx.TextCtrl(self.pnl, size= (120,60),style = wx.TE_MULTILINE)
        self.sizer.Add(self.ctrl_fecha, pos=(9, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)
        
        self.txt_precio = wx.StaticText(self.pnl, label= 'Precio')
        self.txt_precio.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_precio, pos=(8, 2),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)

        self.ctrl_precio= wx.TextCtrl(self.pnl, size= (120,60),style = wx.TE_MULTILINE)
        self.sizer.Add(self.ctrl_precio, pos=(9, 2),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)

        #Modificar y refrescar
        self.modificarButton = wx.Button(self.pnl, label='Modificar', size= (90,30))   
        self.modificarButton.Bind(wx.EVT_BUTTON, self.OnClickedModificar) 
        self.modificarButton.SetBackgroundColour(wx.Colour(0,0,0))
        self.modificarButton.SetForegroundColour(wx.Colour(255,255,255))
        self.sizer.Add(self.modificarButton, pos=(10, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)

        self.nuevoButton = wx.Button(self.pnl, label='NUEVO', size= (90,30))   
        self.nuevoButton.Bind(wx.EVT_BUTTON, self.OnClickedNuevo) 
        self.nuevoButton.SetBackgroundColour(wx.Colour(0,0,0))
        self.nuevoButton.SetForegroundColour(wx.Colour(255,255,255))
        self.sizer.Add(self.nuevoButton, pos=(11, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)

        #LogoS
        self.imagen1 = wx.Image('Logo_almacen_2.png', wx.BITMAP_TYPE_PNG).Rescale(100, 100).ConvertToBitmap() 
        
        
        self.logo1= wx.StaticBitmap(self.pnl, -1, self.imagen1)
        self.sizer.Add(self.logo1, pos=(0, 0),span=wx.DefaultSpan, flag=wx.ALIGN_CENTER)

        
        self.logo2= wx.StaticBitmap(self.pnl, -1, self.imagen1)
        self.sizer.Add(self.logo2, pos=(0, 2),span=wx.DefaultSpan, flag=wx.ALIGN_CENTER)

        self.txt_copyright= wx.StaticText(self.pnl, label= 'Copyright 2021 | All Rights Reserved | Software by Michel Alvarez')
        self.txt_fecha.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_copyright, pos=(16, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTER)

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
            self.ctrl_precio.SetValue(dict_recibir_busqueda['precio'])
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
            self.ctrl_precio.SetValue('-> Precio nuevo...')
            print('Esperando datos para el envio...')


        if self.n_pulsado_nuevo == 2:
            nuevo_item = {
                'codigo':str(self.ctrl_codigo.GetValue()),
                'categoria':str(self.ctrl_categoria.GetValue()),
                'modelo': str(self.ctrl_modelo.GetValue()),
                'stock': str(self.ctrl_stock.GetValue()),
                'fecha': str(self.ctrl_fecha.GetValue()),
                'precio':str(self.ctrl_precio.GetValue())
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
                self.ctrl_precio.SetValue('')
            else:
                self.ctrl_categoria.SetValue('Fallo envio server')
                self.ctrl_codigo.SetValue(' ')
                self.ctrl_modelo.SetValue(' ')
                self.ctrl_stock.SetValue(' ')
                self.ctrl_fecha.SetValue(' ')
                self.ctrl_precio.SetValue(' ')
            
            recibir_inventario = requests.get('http://0.0.0.0:8000/inventario_recibir')
            list_recibir_inventario = list(recibir_inventario.json())
            print(list_recibir_inventario)
            list_dict_inventario = [dict(dict_inventario) for dict_inventario in list_recibir_inventario]
            print(list_dict_inventario)
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
            
            if self.primer_ciclo_categorias == True:
                if len(self.nueva_list_categorias_antigua) != len(nueva_list_categorias):
                    nueva_categoria = nueva_list_categorias[len(nueva_list_categorias)-1]
                    self.cbbox_categoria.Append(nueva_categoria)
                    print(f'La nueva lista de categorias es: {nueva_list_categorias} ')
                    print(f'La nueva categoria es: {nueva_categoria}')
            
            if self.primer_ciclo_categorias == False:
                if len(self.list_categorias) != len(nueva_list_categorias):
                    nueva_categoria = nueva_list_categorias[len(nueva_list_categorias)-1]
                    self.cbbox_categoria.Append(nueva_categoria)
                    self.primer_ciclo_categorias = True
                    print(f'La nueva lista de categorias es: {nueva_list_categorias} ')
                    print(f'La nueva categoria es: {nueva_categoria}')
            
            self.nueva_list_categorias_antigua = nueva_list_categorias
            
            
                     
            
            




def main():

    app = wx.App()
    ex = interfaz(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()