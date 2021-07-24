import wx


class interfaz(wx.Frame):

    def __init__(self, *args, **kw):
        super(interfaz, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        pnl = wx.Panel(self)

        ## VENTANA ##
        self.SetSize((1080, 720))       #defino tamaño de ventana
        self.SetTitle('Gestion Almacen')  #defino el nombre de la ventana
        self.SetBackgroundColour((0, 176, 246))
        self.Centre()

        ## Titulo
        fuente_titulo = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        titulo= wx.StaticText(pnl, label= 'GESTION ALMACEN', pos= (540,80), style= wx.ALIGN_CENTRE_HORIZONTAL)
        titulo.SetFont(fuente_titulo)

        ## Buscar material  
        fuente_titulo = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        titulo= wx.StaticText(pnl, label= 'Buscar Material', pos= (540,120), style= wx.ALIGN_CENTRE_HORIZONTAL)
        titulo.SetFont(fuente_titulo)

        ### Boton Cerrar ###
        closeButton = wx.Button(pnl, label='Cerrar', pos= (540, 25))   #defino boton con nombre, ventana asignada y situacion
        closeButton.Bind(wx.EVT_BUTTON, self.OnClicked)
        closeButton.SetForegroundColour(wx.Colour(255,255,255))   #defino color de letra del boton
        closeButton.SetBackgroundColour(wx.Colour(0,0,0))     #defino color de fondo del boton



    def OnClicked(self,e):                             #creo funcion de clickado
        print("El boton de CERRAR ha sido presionado")     #defino el texto para que aparezca en PyCharm
        self.OnClose(True)                                     #llamo a la funcion de CERRAR para que se cierre al pulsar
        
    def OnClose(self,e):                                   #defino la funcion de cerrar ventana
        self.Close(True)




def main():

    app = wx.App()
    ex = interfaz(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()