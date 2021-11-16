import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class gui_gestor_almacen(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUI("GUI_Gestor_almacen.ui",self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = gui_gestor_almacen()
    GUI.Show()
    sys.exit(app.exec_())
