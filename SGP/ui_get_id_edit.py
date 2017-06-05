from PyQt4 import QtCore, QtGui
from ManejoPersonas import Persona
import data
from ui_edit import EditWindow


class GetIdEditWindow(QtGui.QWidget):
    def __init__(self):
        super(GetIdEditWindow, self).__init__()

        self.createForm()
        self.createButtons()

        self.setWindowIcon(QtGui.QIcon('images/edit.png'))
        self.setWindowTitle("Editar una Persona")
        self.setGeometry(650, 300, 350, 150)

    def createForm(self):
        lbl_id = QtGui.QLabel('Id', self)
        self.txt_id = QtGui.QLineEdit(self)

        self.lbl_info = QtGui.QLabel('', self)

        lbl_id.move(50, 25)
        self.txt_id.move(150, 25)

        self.lbl_info.move(150, 65)

    def check(self):
        registro = data.registro
        persona = registro.encontrar_persona(self.txt_id.text())

        if persona != None:
            self.open_edit_window()
        else:
            self.lbl_info.setText('No se encuentra a esa persona')

    def open_edit_window(self):
        persona_id = self.txt_id.text()
        self.edit_view = EditWindow(persona_id=persona_id)
        self.edit_view.show()
        self.close()

    def createButtons(self):
        okBtn = QtGui.QPushButton('OK')
        okBtn.clicked.connect(self.check)
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
    mainWin = GetIdEditWindow()
    mainWin.show()
    sys.exit(app.exec_())
