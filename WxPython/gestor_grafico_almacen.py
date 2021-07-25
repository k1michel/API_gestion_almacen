import wx


class interfaz(wx.Frame):

    def __init__(self, *args, **kw):
        super(interfaz, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        self.pnl = wx.Panel(self)

        ## VENTANA ##
        self.SetSize((1080, 720))       
        self.SetTitle('Gestion Almacen')  
        self.SetBackgroundColour((0, 176, 246))
        self.Centre()

        self.fgs = wx.FlexGridSizer(6, 2, 1,1)
        self.sizer = wx.BoxSizer()
 
        ## Huecos
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
        self.closeButton.Bind(wx.EVT_BUTTON, self.OnClicked)
        self.closeButton.SetForegroundColour(wx.Colour(255,255,255))   
        self.closeButton.SetBackgroundColour(wx.Colour(0,0,0))         ### Boton Cerrar ### 

        ## Buscar material  
        self.titulo_bucar= wx.StaticText(self.pnl, label= 'Buscar Material', pos= (540,120), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.titulo.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))

        self.ctrl_buscar= wx.TextCtrl(self.pnl)

        ## Resultado busqueda
        self.txt_resultado= wx.StaticText(self.pnl, label= 'Resultado Busqueda', pos= (540,120), style= wx.ALIGN_CENTRE_HORIZONTAL)
        self.txt_resultado.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        
        self.ctrl_resultado = wx.TextCtrl(self.pnl, size= (300,500),style = wx.TE_MULTILINE)
    

        self.fgs.AddMany([(self.titulo,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.hueco1,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.closeButton,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.hueco2,1,wx.ALIGN_CENTRE_HORIZONTAL),
        (self.hueco3,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.titulo_bucar,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.hueco4,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.ctrl_buscar,1,wx.ALIGN_CENTRE_HORIZONTAL),
         (self.hueco5,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.txt_resultado,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.hueco6,1,wx.ALIGN_CENTRE_HORIZONTAL),(self.ctrl_resultado,1,wx.ALIGN_CENTRE_HORIZONTAL)])
        self.fgs.AddGrowableRow(1, 0) 
        self.fgs.AddGrowableCol(0, 0)  
        self.sizer.Add(self.fgs, proportion = 2, flag = wx.ALL|wx.EXPAND, border = 15) 
        self.pnl.SetSizer(self.sizer) 
        self.pnl.SetSizerAndFit(self.sizer)
        

    def OnClicked(self,e):                             #creo funcion de clickado
        print("El boton de CERRAR ha sido presionado")     
        self.OnClose(True)                                     
        
    def OnClose(self,e):                                #defino la funcion de cerrar ventana
        self.Close(True)




def main():

    app = wx.App()
    ex = interfaz(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()