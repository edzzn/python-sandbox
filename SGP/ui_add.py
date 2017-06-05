from PyQt4 import QtCore, QtGui
from ManejoPersonas import Persona
import data

class AddWindow(QtGui.QWidget):
    """
    Ventana para agregar registros
    """
    def __init__(self):
        super(AddWindow, self).__init__()

        self.createForm()
        self.createButtons()

        self.setWindowIcon(QtGui.QIcon('images/user-plus.png'))
        self.setWindowTitle("Agrega una Persona")
        self.setGeometry(650, 300, 350, 250)

    def addPersona(self):

        id_persona = str(self.txt_id.text())
        nombre = str(self.txt_nombre.text())
        apellido = str(self.txt_apellido.text())

        if id_persona == '' or nombre == '' or apellido == '':
            self.lbl_info.setText('Datos incorrectos')

        elif data.registro.encontrar_persona(id_persona) != None:
            self.lbl_info.setText('Datos duplicados')
        else:
            persona = Persona(id_persona, nombre, apellido)

            data.registro.add(persona)
            self.clear_campos()


    def clear_campos(self):
        self.txt_id.clear()
        self.txt_nombre.clear()
        self.txt_apellido.clear()

    def createForm(self):
        lbl_id = QtGui.QLabel('Id', self)
        lbl_nombre = QtGui.QLabel('Nombre', self)
        lbl_apellido = QtGui.QLabel('Apellido', self)
        self.txt_id = QtGui.QLineEdit(self)
        self.txt_nombre = QtGui.QLineEdit(self)
        self.txt_apellido = QtGui.QLineEdit(self)

        self.lbl_info = QtGui.QLabel(self)

        lbl_id.move(50, 25)
        self.txt_id.move(150, 25)

        lbl_nombre.move(50, 75)
        self.txt_nombre.move(150, 75)

        lbl_apellido.move(50, 125)
        self.txt_apellido.move(150, 125)

        self.lbl_info.move(150, 160)
        self.lbl_info.resize(200, 20)

    def createButtons(self):
        okBtn = QtGui.QPushButton('OK')
        okBtn.clicked.connect(self.addPersona)
        cancelBtn = QtGui.QPushButton('Cancel')
        cancelBtn.clicked.connect(self.close)
        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okBtn)
        hbox.addWidget(cancelBtn)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    mainWin = AddWindow()
    mainWin.show()
    sys.exit(app.exec_())
