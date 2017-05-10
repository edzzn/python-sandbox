# .pyw indica que se va a llamar a "pythonw.exe"
# Previene que se abra la terminal al ejecutar el archivo

import sys
from PyQt4 import QtGui, QtCore

# QtGui.QWitget es la clase base de todos los objectos de interfaz de
# usuario
class VentanaEjemplo(QtGui.QWidget):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Vetana de ejemplo')

        # Muestra un boton de cerrar
        quit = QtGui.QPushButton('Cerrar', self)
        quit.setGeometry(10, 10, 70, 40)

        # Señales y Slots - Orientado a Eventos
        # 1) se produce una accion.  Ej. Se pulsa un boton
        # 2) Se realiza un metodo
        self.connect(quit, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT('quit()'))

# se crea un objeto aplicaciones
app = QtGui.QApplication(sys.argv)

ve = VentanaEjemplo()
ve.show()

# Loop de manejo de evento
# exec_ tiene el '_' por ser una palabra reservada de Python
sys.exit(app.exec_())