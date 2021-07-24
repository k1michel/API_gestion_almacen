import wx


class interfaz(wx.Frame):

    def __init__(self, *args, **kw):
        super(interfaz, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        pnl = wx.Panel(self)

        closeButton = wx.Button(pnl, label='Cerrar', pos= (200, 75))   #defino boton con nombre, ventana asignada y situacion
        closeButton.Bind(wx.EVT_BUTTON, self.OnClicked)


        self.SetSize((1920, 1080))       #defino tamaño de ventana
        self.SetTitle('Gestion Almacen')  #defino el nombre de la ventana
        self.Centre()
        closeButton.SetForegroundColour(wx.Colour(0,255,0))   #defino color de letra del boton
        closeButton.SetBackgroundColour(wx.Colour(0,0,0))     #defino color de fondo del boton

    def OnClose(self):                                   #defino la funcion de cerrar ventana
        self.Close(True)

    def OnClicked(self):                             #creo funcion de clickado
        print("El boton de CERRAR ha sido presionado")     #defino el texto para que aparezca en PyCharm
        self.OnClose(True)                                     #llamo a la funcion de CERRAR para que se cierre al pulsar
        





def main():

    app = wx.App()
    ex = interfaz(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()