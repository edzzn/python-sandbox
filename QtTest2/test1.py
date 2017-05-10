import sys
from PyQt4 import QtCore, QtGui
from testgui import Ui_Dialog

class MyForm(QtGui.QMainWindow):
    """docstring for __MyForm."""
    def _init__(self, arg, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.pushButton.clicked.connect(self.hola_mundo)

    def hola_mundo(arg):
        self.ui.textEdit.set('Hola Mundo!')
        print ('Hola Mundo')

if __name__ == 'main':
    app.QtGui.QApplication(sys.argv)
    myapp = MyFrom()
    myapp.show()
    sys.exit(app.exec_())
