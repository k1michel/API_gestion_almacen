import wx


class interfaz(wx.Frame):

    #def __init__(self, *args, **kw):
        #super(interfaz, self).__init__(*args, **kw)
    def __init__(self, parent, title):
        super(interfaz, self).__init__(parent, title=title)
        
        self.InitUI()
        self.Centre()

    def InitUI(self):

        self.pnl = wx.Panel(self)
        self.categoria_sel = str
        self.busqueda_enter = str
        ## VENTANA ##
        self.SetSize((1080, 720))       
        #self.SetTitle('Gestion Almacen')  
        self.SetBackgroundColour((0, 176, 246))
        

        self.sizer = wx.GridBagSizer(12, 5)
        
 

        
        ## Cuadro titulo
        #self.cuadro_titulo= wx.StaticBox(self.pnl, label="", pos=(200,2),size=(400,85), style= wx.ALIGN_CENTRE_HORIZONTAL)
        #self.cuadro_titulo.SetBackgroundColour(wx.Colour(0,0,0,alpha= 100))
        

        ## Titulo
        self.fuente_titulo = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        self.titulo= wx.StaticText(self.pnl, label= 'GESTION ALMACEN')
        self.titulo.SetFont(self.fuente_titulo)
        self.titulo.SetForegroundColour(wx.Colour(255,255,255))
        self.sizer.Add(self.titulo, pos=(0, 2))
        ### Boton Cerrar ###
        self.closeButton = wx.Button(self.pnl, label='Cerrar')   
        self.closeButton.Bind(wx.EVT_BUTTON, self.OnClickedCerrar)
        self.closeButton.SetForegroundColour(wx.Colour(255,255,255))   
        self.closeButton.SetBackgroundColour(wx.Colour(0,0,0)) 
        self.sizer.Add(self.closeButton, pos=(1, 2))

        ## Listado 
        self.txt_listado= wx.StaticText(self.pnl, label= 'Listado')
        self.txt_listado.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_listado, pos=(3, 0))

        self.ctrl_buscar= wx.TextCtrl(self.pnl, size= (120,30),style = wx.TE_PROCESS_ENTER)
        self.ctrl_buscar.Bind(wx.EVT_TEXT_ENTER,self.OnEnterPressedBuscar) 
        self.sizer.Add(self.ctrl_buscar, pos=(5, 0))
        
        self.categoria =  u"electricidad|neumatica".split("|")
        self.cbbox_categoria = wx.ComboBox(self,-1,choices= self.categoria,size=(120,30))
        self.Bind(wx.EVT_COMBOBOX, self.OnSelect)
        #self.ctrl_categoria = wx.TextCtrl(self.pnl, size= (300,500),style = wx.TE_MULTILINE)
        self.sizer.Add(self.cbbox_categoria, pos=(4, 0))

        self.ctrl_resultado = wx.TextCtrl(self.pnl, size= (200,600),style = wx.TE_MULTILINE)
        self.sizer.Add(self.ctrl_resultado, pos=(6, 0))
        

        ## Referenciado
        self.txt_referenciado= wx.StaticText(self.pnl, label= 'Referenciado')
        self.txt_referenciado.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_referenciado, pos=(3, 3))

        self.ctrl_buscar_codigo= wx.TextCtrl(self.pnl, size= (120,30),style= wx.TE_PROCESS_ENTER)
        self.ctrl_buscar_codigo.Bind(wx.EVT_TEXT_ENTER,self.OnEnterPressedCodigo)
        self.ctrl_buscar_codigo.SetValue('Codigo') 
        self.sizer.Add(self.ctrl_buscar_codigo, pos=(4, 3))

        self.txt_codigo= wx.StaticText(self.pnl, label= 'Codigo')
        self.txt_codigo.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_codigo, pos=(5, 2))
        
        self.ctrl_codigo= wx.TextCtrl(self.pnl, size= (120,30),style = wx.TE_MULTILINE)
        self.sizer.Add(self.ctrl_codigo, pos=(6, 2))

        self.txt_categoria= wx.StaticText(self.pnl, label= 'Categoria')
        self.txt_categoria.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_categoria, pos=(5, 3))
        
        self.ctrl_categoria= wx.TextCtrl(self.pnl, size= (120,30),style = wx.TE_MULTILINE)
        self.sizer.Add(self.ctrl_categoria, pos=(6, 3))

        self.txt_modelo= wx.StaticText(self.pnl, label= 'Modelo')
        self.txt_modelo.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_modelo, pos=(5, 4))

        self.ctrl_modelo= wx.TextCtrl(self.pnl, size= (120,30),style = wx.TE_MULTILINE)
        self.sizer.Add(self.ctrl_modelo, pos=(6, 4))

        self.txt_stock= wx.StaticText(self.pnl, label= 'Stock')
        self.txt_stock.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_stock, pos=(7, 2))

        self.ctrl_stock= wx.TextCtrl(self.pnl, size= (120,30),style = wx.TE_MULTILINE)
        self.sizer.Add(self.ctrl_stock, pos=(8, 2))

        self.txt_fecha= wx.StaticText(self.pnl, label= 'Fecha')
        self.txt_fecha.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_fecha, pos=(7, 3))

        self.ctrl_fecha= wx.TextCtrl(self.pnl, size= (120,30),style = wx.TE_MULTILINE)
        self.sizer.Add(self.ctrl_fecha, pos=(8, 3))
        #Modificar y refrescar
        self.modificarButton = wx.Button(self.pnl, label='Modificar', size= (90,30))   
        self.modificarButton.Bind(wx.EVT_BUTTON, self.OnClickedModificar) 
        self.modificarButton.SetBackgroundColour(wx.Colour(0,0,0))
        self.modificarButton.SetForegroundColour(wx.Colour(255,255,255))
        self.sizer.Add(self.modificarButton, pos=(9, 3))

        self.refrescarButton = wx.Button(self.pnl, label='Refrescar', size= (90,30))   
        self.refrescarButton.Bind(wx.EVT_BUTTON, self.OnClickedRefrescar) 
        self.refrescarButton.SetBackgroundColour(wx.Colour(0,0,0))
        self.refrescarButton.SetForegroundColour(wx.Colour(255,255,255))
        self.sizer.Add(self.refrescarButton, pos=(10, 3))

        #Logo
        self.txt_logo1= wx.StaticText(self.pnl, label= 'Logo1')
        self.txt_logo1.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_logo1, pos=(0, 1))

        self.txt_logo2= wx.StaticText(self.pnl, label= 'Logo2')
        self.txt_logo2.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_logo2, pos=(0, 3))

        ## Imagen
        self.txt_imagen= wx.StaticText(self.pnl, label= 'Imagen')
        self.txt_imagen.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.sizer.Add(self.txt_imagen, pos=(11, 3))

        #self.sizer.AddGrowableCol(0)
        #self.sizer.AddGrowableRow(11)

        self.pnl.SetSizer(self.sizer)
        #self.sizer.Fit(self)
        
        
        


                                     
        
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
        self.busqueda_codigo = self.ctrl_buscar_codigo.GetValue()
        self.enviar(True)
    
    
    def enviar(self,e):
        self.envio = dict(
            cat= self.categoria_sel,
            busc= self.busqueda_codigo
            )

    def OnEnterPressedCodigo(self,event):
        print('Se ha introducido codigo para buscar')

    def OnClickedModificar(self,event):
        print('Se ha pulsado boton Modificar')

    def OnClickedRefrescar(self,event):
        print('Se ha pulsado boton Refrescar')




def main():

    app = wx.App()
    ex = interfaz(None, title= 'GESTION ALMACEN by Michel Alvarez')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()