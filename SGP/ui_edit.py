from PyQt4 import QtCore, QtGui
from ManejoPersonas import Persona
import data


class EditWindow(QtGui.QWidget):
    """
    Ventana basada en ui_edit, Interfaz similar. Esta NO permite editar el campo txt_id
    """
    def __init__(self, persona_id):
        super(EditWindow, self).__init__()
        self.persona_id = persona_id

        self.createForm()
        self.createButtons()

        self.setWindowIcon(QtGui.QIcon('images/edit.png'))
        self.setWindowTitle("Editar un usuario")
        self.setGeometry(650, 300, 350, 250)

    def edit_persona(self):
        id_persona = str(self.txt_id.text())
        nombre = str(self.txt_nombre.text())
        apellido = str(self.txt_apellido.text())
        persona = Persona(id_persona, nombre, apellido)

        data.registro.edit_persona(id_persona, persona)
        self.close()


    def clear_campos(self):
        self.txt_id.clear()
        self.txt_nombre.clear()
        self.txt_apellido.clear()

    def update_campos(self):
        persona = data.registro.encontrar_persona(self.persona_id)

        self.txt_id.setText(persona.get_id())
        self.txt_nombre.setText(persona.get_nombre())
        self.txt_apellido.setText(persona.get_apellido())

    def createForm(self):
        lbl_id = QtGui.QLabel('Id', self)
        lbl_nombre = QtGui.QLabel('Nombre', self)
        lbl_apellido = QtGui.QLabel('Apellido', self)
        self.txt_id = QtGui.QLineEdit(self)
        self.txt_nombre = QtGui.QLineEdit(self)
        self.txt_apellido = QtGui.QLineEdit(self)

        self.update_campos()

        lbl_id.move(50, 25)
        self.txt_id.setReadOnly(True)
        self.txt_id.move(150, 25)

        lbl_nombre.move(50, 75)
        self.txt_nombre.move(150, 75)

        lbl_apellido.move(50, 125)
        self.txt_apellido.move(150, 125)

    def createButtons(self):
        okBtn = QtGui.QPushButton('OK')
        okBtn.clicked.connect(self.edit_persona)
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
    mainWin = EditWindow(0)
    mainWin.show()
    sys.exit(app.exec_())
