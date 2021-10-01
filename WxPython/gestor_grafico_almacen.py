import wx
import requests
import json
from time import sleep


class interfaz(wx.Frame):
    categoria_sel : str = 'vacio'
    busqueda_codigo : str = 'vacio'
    
    def __init__(self, *args, **kw):
        super(interfaz, self).__init__(*args, **kw)
    
        
        self.InitUI()
        self.Centre()

    def InitUI(self):

        self.pnl = wx.Panel(self)
        
        self.ip_server = 'http://0.0.0.0:8000/'
        
        ## VENTANA ##       
        self.SetSize(1080,720)
        self.SetTitle('GESTION ALMACEN by Michel Alvarez')  
        self.SetBackgroundColour((0, 176, 246))
        

        self.sizer = wx.GridBagSizer(16,3)
        

        ## Titulo
        self.fuente_titulo = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        self.titulo= wx.StaticText(self.pnl, label= 'GESTION ALMACEN')
        self.titulo.SetFont(self.fuente_titulo)
        self.titulo.SetForegroundColour(wx.Colour(255,255,255))
        self.sizer.Add(self.titulo, pos=(0, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTER)
        ### Boton Cerrar ###
        self.closeButton = wx.Button(self.pnl, label='Cerrar')   
        self.closeButton.Bind(wx.EVT_BUTTON, self.OnClickedCerrar)
        self.closeButton.SetForegroundColour(wx.Colour(255,255,255))   
        self.closeButton.SetBackgroundColour(wx.Colour(0,0,0)) 
        self.sizer.Add(self.closeButton, pos=(1, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTER)

        ## Listado 
        self.txt_listado= wx.StaticText(self.pnl, label= 'Listado')
        self.txt_listado.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_listado, pos=(11, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTER)

        self.ctrl_buscar= wx.TextCtrl(self.pnl, size= (120,30),style = wx.TE_PROCESS_ENTER)
        self.ctrl_buscar.Bind(wx.EVT_TEXT_ENTER,self.OnEnterPressedBuscar)
        self.ctrl_buscar.SetValue('Buscar...')
        self.sizer.Add(self.ctrl_buscar, pos=(13, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTER)
        
        self.categoria =  u"electricidad|neumatica".split("|")
        self.cbbox_categoria = wx.ComboBox(self,-1,choices= self.categoria,size=(120,30))
        self.Bind(wx.EVT_COMBOBOX, self.OnSelect)
        self.sizer.Add(self.cbbox_categoria, pos=(12, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTER)

        self.ctrl_resultado = wx.TextCtrl(self.pnl,size=(200,1000),style = wx.TE_MULTILINE)
        self.sizer.Add(self.ctrl_resultado, pos=(14, 1), flag=wx.ALIGN_CENTRE)
        

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
        
        self.ctrl_codigo= wx.TextCtrl(self.pnl, size= (120,30),style = wx.TE_MULTILINE)
        self.sizer.Add(self.ctrl_codigo, pos=(6, 0),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)

        self.txt_categoria= wx.StaticText(self.pnl, label= 'Categoria')
        self.txt_categoria.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_categoria, pos=(5, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)
        
        self.ctrl_categoria= wx.TextCtrl(self.pnl, size= (120,30),style = wx.TE_MULTILINE)
        self.sizer.Add(self.ctrl_categoria, pos=(6, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)

        self.txt_modelo= wx.StaticText(self.pnl, label= 'Modelo')
        self.txt_modelo.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_modelo, pos=(5, 2),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)

        self.ctrl_modelo= wx.TextCtrl(self.pnl, size= (120,30),style = wx.TE_MULTILINE)
        self.sizer.Add(self.ctrl_modelo, pos=(6, 2),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)

        self.txt_stock= wx.StaticText(self.pnl, label= 'Stock')
        self.txt_stock.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_stock, pos=(7, 0),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)

        self.ctrl_stock= wx.TextCtrl(self.pnl, size= (120,30),style = wx.TE_MULTILINE)
        self.sizer.Add(self.ctrl_stock, pos=(8, 0),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)

        self.txt_fecha= wx.StaticText(self.pnl, label= 'Ultima modificacion')
        self.txt_fecha.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_fecha, pos=(7, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)

        self.ctrl_fecha= wx.TextCtrl(self.pnl, size= (120,30),style = wx.TE_MULTILINE)
        self.sizer.Add(self.ctrl_fecha, pos=(8, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)
        #Modificar y refrescar
        self.modificarButton = wx.Button(self.pnl, label='Modificar', size= (90,30))   
        self.modificarButton.Bind(wx.EVT_BUTTON, self.OnClickedModificar) 
        self.modificarButton.SetBackgroundColour(wx.Colour(0,0,0))
        self.modificarButton.SetForegroundColour(wx.Colour(255,255,255))
        self.sizer.Add(self.modificarButton, pos=(9, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)

        self.refrescarButton = wx.Button(self.pnl, label='Refrescar', size= (90,30))   
        self.refrescarButton.Bind(wx.EVT_BUTTON, self.OnClickedRefrescar) 
        self.refrescarButton.SetBackgroundColour(wx.Colour(0,0,0))
        self.refrescarButton.SetForegroundColour(wx.Colour(255,255,255))
        self.sizer.Add(self.refrescarButton, pos=(10, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTRE)

        #Logo
        self.txt_logo1= wx.StaticText(self.pnl, label= 'Logo1')
        self.txt_logo1.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_logo1, pos=(0, 0),span=wx.DefaultSpan, flag=wx.ALIGN_CENTER)

        self.txt_logo2= wx.StaticText(self.pnl, label= 'Logo2')
        self.txt_logo2.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_logo2, pos=(0, 2),span=wx.DefaultSpan, flag=wx.ALIGN_CENTER)

        ## Imagen
        self.txt_imagen= wx.StaticText(self.pnl, label= 'Imagen')
        self.txt_imagen.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_imagen, pos=(15, 1),span=wx.DefaultSpan, flag=wx.ALIGN_CENTER)

        #self.sizer.AddGrowableCol(1)
        
        
        

        self.SetSizerAndFit(self.sizer)
        
        
        
        


                                     
        
    def OnClose(self,e):                                
        self.Close(True)
    def OnClickedCerrar(self,e):                             
        print("El boton de CERRAR ha sido presionado")     
        print(self.envio)
        self.OnClose(True)
    
    def OnSelect(self,event):
        self.categoria_sel = self.cbbox_categoria.GetValue()
        self.enviar(True)        

    def OnEnterPressedBuscar(self,event):
        self.busqueda = self.ctrl_buscar.GetValue() 
        print(f'Se ha buscado {self.busqueda}')

    def enviar(self,e):
        envio = {
            "cat": self.categoria_sel,
            "busc":self.busqueda_codigo
        }
        respuesta_envio = requests.post('http://0.0.0.0:8000/envios', data=json.dumps(envio))
        print(f'Respuesta del requests -> {respuesta_envio.json()}')
        print(f'Envio -> {envio}')
        self.categoria_sel = 'vacio'
        self.busqueda_codigo = 'vacio'
        sleep(1)
        list_recibir_busqueda = requests.get('http://0.0.0.0:8000/envios')
        print(list_recibir_busqueda)
        dict_recibir_busqueda = list_recibir_busqueda[1]
        self.ctrl_codigo.SetValue(dict_recibir_busqueda['codigo'])
        self.ctrl_categoria.SetValue(dict_recibir_busqueda['categoria'])
        self.ctrl_modelo.SetValue(dict_recibir_busqueda['modelo'])
        self.ctrl_stock.SetValue(dict_recibir_busqueda['stock'])
    def OnEnterPressedCodigo(self,event):
        print('Se ha introducido codigo para buscar')
        self.busqueda_codigo = self.ctrl_buscar_codigo.GetValue()
        print(f'Busqueda codigo -> {self.busqueda_codigo}\n')
        self.enviar(True)
        
        

    def OnClickedModificar(self,event):
        print('Se ha pulsado boton Modificar')

    def OnClickedRefrescar(self,event):
        print('Se ha pulsado boton Refrescar')




def main():

    app = wx.App()
    ex = interfaz(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()