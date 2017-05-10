import sys
from PrimeraAplicacion import *

class MiFormulario(QtGui.QDialog):

    # Iparent = None, Declara que el Widget es de alto nivel
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        # instanciamos Ui_Dialog, Clase que se encuentra en la template
        # Que se obtiene al trabajar con Qt designer
        self.ui = Ui_Dialog()
        # metodo setupUi() contiene todos los widgets de nuestra applicacion
        self.ui.setupUi(self)

        self.ui.pushButton.clicked(self.)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = MiFormulario()
    myapp.show()
    sys.exit(app.exec_())
    # para que se necesita el '_' de exec ?
