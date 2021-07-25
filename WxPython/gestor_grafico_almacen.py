import wx


class interfaz(wx.Frame):

    def __init__(self, *args, **kw):
        super(interfaz, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        self.pnl = wx.Panel(self)
        self.categoria_sel = str
        self.busqueda_enter = str
        ## VENTANA ##
        self.SetSize((1080, 720))       
        self.SetTitle('Gestion Almacen')  
        self.SetBackgroundColour((0, 176, 246))
        self.Centre()

        self.fgs = wx.FlexGridSizer(12, 5, 1,1)
        
 
        ## Huecos matriz grafica
        self.hueco1= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco1.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco2= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco2.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco3= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco3.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco4= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco4.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco5= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco5.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco6= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco6.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco7= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco7.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco8= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco8.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco9= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco9.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco10= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco10.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco11= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco11.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco12= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco12.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco13= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco13.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco14= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco14.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco15= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco15.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco16= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco16.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco17= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco17.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco18= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco18.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco19= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco19.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco20= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco20.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco21= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco21.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco22= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco22.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco23= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco23.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco24= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco24.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco25= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco25.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco26= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco26.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco27= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco27.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco28= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco28.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco29= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco29.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco30= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco30.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco31= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco31.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco32= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco32.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco33= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco33.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco34= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco34.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco35= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco35.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco36= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco36.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.hueco37= wx.StaticText(self.pnl, label= ' ', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.hueco37.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        
        ## Cuadro titulo
        self.cuadro_titulo= wx.StaticBox(self.pnl, label="", pos=(200,2),size=(400,85), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.cuadro_titulo.SetBackgroundColour(wx.Colour(0,0,0,alpha= 100))
        

        ## Titulo
        self.fuente_titulo = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        self.titulo= wx.StaticText(self.pnl, label= 'GESTION ALMACEN', pos= (600,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.titulo.SetFont(self.fuente_titulo)
        self.titulo.SetForegroundColour(wx.Colour(255,255,255))

        ### Boton Cerrar ###
        self.closeButton = wx.Button(self.pnl, label='Cerrar', pos= (540, 5))   
        self.closeButton.Bind(wx.EVT_BUTTON, self.OnClickedCerrar)
        self.closeButton.SetForegroundColour(wx.Colour(255,255,255))   
        self.closeButton.SetBackgroundColour(wx.Colour(0,0,0)) 

        ## Listado 
        self.txt_listado= wx.StaticText(self.pnl, label= 'Listado', pos= (540,120), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.txt_listado.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))

        self.ctrl_buscar= wx.TextCtrl(self.pnl, style= wx.TE_PROCESS_ENTER)
        self.ctrl_buscar.Bind(wx.EVT_TEXT_ENTER,self.OnEnterPressedBuscar) 
        
        
        self.categoria =  u"electricidad|neumatica".split("|")
        self.cbbox_categoria = wx.ComboBox(self,-1,choices= self.categoria,size=(120,30))
        self.Bind(wx.EVT_COMBOBOX, self.OnSelect)
        #self.ctrl_categoria = wx.TextCtrl(self.pnl, size= (300,500),style = wx.TE_MULTILINE)

        self.ctrl_resultado = wx.TextCtrl(self.pnl, size= (200,600),style = wx.TE_MULTILINE)
         
        

        ## Referenciado
        self.txt_referenciado= wx.StaticText(self.pnl, label= 'Referenciado', pos= (540,120), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.txt_referenciado.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))

        self.ctrl_buscar_codigo= wx.TextCtrl(self.pnl, style= wx.TE_PROCESS_ENTER)
        self.ctrl_buscar_codigo.Bind(wx.EVT_TEXT_ENTER,self.OnEnterPressedCodigo)
        self.ctrl_buscar_codigo.SetValue('Codigo') 

        self.txt_codigo= wx.StaticText(self.pnl, label= 'Codigo', pos= (540,120), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.txt_codigo.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.ctrl_codigo= wx.TextCtrl(self.pnl)

        self.txt_categoria= wx.StaticText(self.pnl, label= 'Categoria', pos= (540,120), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.txt_categoria.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.ctrl_categoria= wx.TextCtrl(self.pnl)

        self.txt_modelo= wx.StaticText(self.pnl, label= 'Modelo', pos= (540,120), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.txt_modelo.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.ctrl_modelo= wx.TextCtrl(self.pnl)

        self.txt_stock= wx.StaticText(self.pnl, label= 'Stock', pos= (540,120), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.txt_stock.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.ctrl_stock= wx.TextCtrl(self.pnl)

        self.txt_fecha= wx.StaticText(self.pnl, label= 'Fecha', pos= (540,120), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.txt_fecha.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        self.ctrl_fecha= wx.TextCtrl(self.pnl)

        #Modificar y refrescar
        self.modificarButton = wx.Button(self.pnl, label='Modificar', pos= (540, 5))   
        self.modificarButton.Bind(wx.EVT_BUTTON, self.OnClickedModificar) 
        self.modificarButton.SetBackgroundColour(wx.Colour(0,0,0))
        self.modificarButton.SetForegroundColour(wx.Colour(255,255,255))

        self.refrescarButton = wx.Button(self.pnl, label='Refrescar', pos= (540, 5))   
        self.refrescarButton.Bind(wx.EVT_BUTTON, self.OnClickedRefrescar) 
        self.refrescarButton.SetBackgroundColour(wx.Colour(0,0,0))
        self.refrescarButton.SetForegroundColour(wx.Colour(255,255,255))

        #Logo
        self.txt_logo1= wx.StaticText(self.pnl, label= 'Logo1', pos= (540,120), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.txt_logo1.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))

        self.txt_logo2= wx.StaticText(self.pnl, label= 'Logo2', pos= (540,120), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.txt_logo2.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))

        ## Imagen
        self.txt_imagen= wx.StaticText(self.pnl, label= 'Imagen', pos= (540,120), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.txt_imagen.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))


        self.fgs.AddMany([(self.hueco1,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.txt_logo1,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.titulo,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.txt_logo2,1,wx.ALIGN_CENTRE_HORIZONTAL),
        (self.hueco2,1,wx.ALIGN_CENTRE_HORIZONTAL),
        (self.hueco13,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.hueco31,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.closeButton,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.hueco32,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.hueco33,1,wx.ALIGN_CENTRE_HORIZONTAL),
        (self.hueco3,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.hueco4,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.hueco5,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.hueco6,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.hueco7,1,wx.ALIGN_CENTRE_HORIZONTAL),
        (self.txt_listado,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.hueco8,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.hueco9,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.txt_referenciado,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.hueco10,1,wx.ALIGN_CENTRE_HORIZONTAL),
        (self.hueco34,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.hueco35,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.hueco36,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.ctrl_buscar_codigo,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.hueco37,1,wx.ALIGN_CENTRE_HORIZONTAL),
        (self.cbbox_categoria,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.hueco11,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.txt_codigo,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.txt_categoria,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.txt_modelo,1,wx.ALIGN_CENTRE_HORIZONTAL),
        (self.ctrl_buscar,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.hueco12,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.ctrl_codigo,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.ctrl_categoria,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.ctrl_modelo,1,wx.ALIGN_CENTRE_HORIZONTAL),
        (self.ctrl_resultado,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.hueco14,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.txt_stock,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.txt_fecha,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.hueco15,1,wx.ALIGN_CENTRE_HORIZONTAL),
        (self.hueco16,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.hueco17,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.ctrl_stock,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.ctrl_fecha,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.hueco18,1,wx.ALIGN_CENTRE_HORIZONTAL),
        (self.hueco19,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.hueco20,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.hueco21,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.modificarButton,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.hueco22,1,wx.ALIGN_CENTRE_HORIZONTAL),
        (self.hueco23,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.hueco24,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.hueco25,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.refrescarButton,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.hueco26,1,wx.ALIGN_CENTRE_HORIZONTAL),
        (self.hueco27,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.hueco28,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.hueco29,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.txt_imagen,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.hueco30,1,wx.ALIGN_CENTRE_HORIZONTAL)])
        
        self.fgs.AddGrowableRow(0, 1) 
        self.fgs.AddGrowableCol(1, 2)  
         
        self.SetSizer(self.fgs)
        self.Fit()
        
        


                                     
        
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
    ex = interfaz(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()