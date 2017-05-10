from PyQt4 import QtCore, QtGui
import sys
from ingresoUI import Ui_Form
from MainWindow import *

class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        self.ui.btnAcercaDe.clicked.connect(self.mostrar_acerca_de)
        self.ui.btnIngresar.clicked.connect(self.ingresar_datos)
        self.ui.btnListar.clicked.connect(self.listar_datos)
        self.ui.actionListar_Datos.triggered.connect(self.listar_datos)
        self.ui.actionIngresar_Datos.triggered.connect(self.ingresar_datos)
        # self.ui.actionAcerca_de.triggered.connect(self.mostrar_acerca_de())

    def mostrar_acerca_de(self):
        print('Mostrando acerca de')

    def ingresar_datos(self):
        print('Ingresa Datos')
        ingreso = QtGui.QWidget()
        Form = QtGui.QWidget()
        ui = Ui_Form()
        # ui = ingreso.Ui_Form()
        ui.setupUi(Form)
        Form.show()
        # sys.exit(app.exec_())


    def listar_datos(self):
        print('Agregar Datos')


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())

