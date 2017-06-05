from PyQt4 import QtCore, QtGui
from ManejoPersonas import Persona, Registro
import data


class ListWindow(QtGui.QWidget):
    """
        Lista todos las personas en el registro
    """
    def __init__(self):
        super(ListWindow, self).__init__()

        self.createForm()

        self.setWindowIcon(QtGui.QIcon('images/th-list.png'))
        self.setWindowTitle("Registro - Agrega una Persona")
        self.setGeometry(650, 300, 350, 250)

    def createForm(self):
        lbl_registro = QtGui.QLabel('Registro:', self)
        self.textBrowser = QtGui.QTextBrowser(self)

        lbl_registro.move(50, 25)
        self.textBrowser.move(50, 50)

        registros = data.registro.get_registro()
        text = ''
        for persona in registros:
            text = text + '\n' + persona.print_persona()

        self.textBrowser.setText(text)

if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    mainWin = ListWindow()
    mainWin.show()
    sys.exit(app.exec_())
