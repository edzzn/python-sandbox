from PyQt4 import QtCore, QtGui
import sys
from ui_add import AddWindow
from ui_list import ListWindow
from ui_get_id_edit import GetIdEditWindow
from ui_get_id_delete import GetIdDeleteWindow

class MainWindow(QtGui.QMainWindow):
    """
        Main Interfaz de la aplicacion
    """
    def __init__(self):
        super(MainWindow, self).__init__()

        self.createActions()
        self.createMenus()
        self.createToolBars()
        self.createStatusBar()


        self.setWindowIcon(QtGui.QIcon('images/users.png'))
        self.setWindowTitle("SGP - Sistema de Gestion de Personas")
        self.setGeometry(300, 300, 350, 250)

    def open_list_window(self):
        self.list_view = ListWindow()
        self.list_view.show()

    def open_get_id_edit_window(self):
        self.get_id_edit_view = GetIdEditWindow()
        self.get_id_edit_view.show()

    def open_get_id_delete_window(self):
        self.get_id_delete_view = GetIdDeleteWindow()
        self.get_id_delete_view.show()

    def open_add_window(self):
        self.add_view = AddWindow()
        self.add_view.show()

    def addPersona(self):
        print('addPersona')
        self.open_add_window()

    def editarPersona(self):
        self.open_get_id_edit_window()

    def eliminarPersona(self):
        self.open_get_id_delete_window()

    def buscarPersona(self):
        print('buscarPersona')

    def listPersonas(self):
        self.open_list_window()

    def about(self):
        QtGui.QMessageBox.about(self, "Acerca de SGB - Sistema de Gestion de Personas",
                "<b>SGB</b> es una aplicacion realizada por <b>Edisson Reinozo</b>."  )

    def createActions(self):
        self.addPersonaAct = QtGui.QAction(QtGui.QIcon('images/user-plus.png'),
                "&Agregar Usuario", self, shortcut=QtGui.QKeySequence.New,
                                           statusTip="Agrega un usuario al registro",
                                           triggered=self.addPersona)

        self.listAct = QtGui.QAction(QtGui.QIcon('images/th-list.png'),
                "&Listar Usuarios", self, shortcut="Ctrl+L",
                                     statusTip="Muestra todos los usuarios del registro",
                                     triggered=self.listPersonas)

        self.editAct = QtGui.QAction(QtGui.QIcon('images/edit.png'),
                "&Editar un usuarios", self, shortcut="Ctrl+R",
                                     statusTip="Edita un usuario dado su Id.",
                                     triggered=self.editarPersona)

        self.deleteAct = QtGui.QAction(QtGui.QIcon('images/user-times.png'),
                                     "&Eliminar un usuarios", self,
                                     statusTip="Elimina un usuario dado su Id.",
                                     triggered=self.eliminarPersona)

        self.searchAct = QtGui.QAction(QtGui.QIcon('images/search.png'),
                "&Buscar...", self, shortcut=QtGui.QKeySequence.Find,
                                       statusTip="Buscar usuario por id",
                                       triggered=self.buscarPersona)

        self.quitAct = QtGui.QAction(QtGui.QIcon('images/close.png'),
                                     "&Salir", self, shortcut="Ctrl+Q",
                statusTip="Salir de la aplicacion", triggered=self.close)

        self.aboutAct = QtGui.QAction(QtGui.QIcon('images/info.png'),
                                      "&Acerca de", self,
                statusTip="Acerca de SGP",
                triggered=self.about)


    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&Archivo")
        self.fileMenu.addAction(self.addPersonaAct)
        self.fileMenu.addAction(self.listAct)
        self.fileMenu.addAction(self.editAct)
        self.fileMenu.addAction(self.deleteAct)
        # self.fileMenu.addAction(self.searchAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.quitAct)

        self.menuBar().addSeparator()

        self.helpMenu = self.menuBar().addMenu("&Ayuda")
        self.helpMenu.addAction(self.aboutAct)

    def createStatusBar(self):
        self.statusBar().showMessage("Ready")
        
    def createToolBars(self):
        self.fileToolBar = self.addToolBar("Archivo")
        self.fileToolBar.addAction(self.addPersonaAct)
        self.fileToolBar.addAction(self.listAct)
        self.fileToolBar.addAction(self.editAct)
        self.fileToolBar.addAction(self.deleteAct)
        # self.fileToolBar.addAction(self.searchAct)

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
