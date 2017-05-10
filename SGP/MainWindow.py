# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(630, 466)
        MainWindow.setMouseTracking(False)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAnimated(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(180, 110, 231, 101))
        self.label.setMinimumSize(QtCore.QSize(231, 71))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(120, 190, 341, 101))
        self.label_2.setMinimumSize(QtCore.QSize(231, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 10, 278, 36))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.btnIngresar = QtGui.QPushButton(self.widget)
        self.btnIngresar.setObjectName(_fromUtf8("btnIngresar"))
        self.gridLayout.addWidget(self.btnIngresar, 0, 0, 1, 1)
        self.btnListar = QtGui.QPushButton(self.widget)
        self.btnListar.setObjectName(_fromUtf8("btnListar"))
        self.gridLayout.addWidget(self.btnListar, 0, 1, 1, 1)
        self.btnAcercaDe = QtGui.QPushButton(self.widget)
        self.btnAcercaDe.setObjectName(_fromUtf8("btnAcercaDe"))
        self.gridLayout.addWidget(self.btnAcercaDe, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 630, 30))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        self.menuAyuda = QtGui.QMenu(self.menubar)
        self.menuAyuda.setObjectName(_fromUtf8("menuAyuda"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionIngresar_Datos = QtGui.QAction(MainWindow)
        self.actionIngresar_Datos.setObjectName(_fromUtf8("actionIngresar_Datos"))
        self.actionListar_Datos = QtGui.QAction(MainWindow)
        self.actionListar_Datos.setObjectName(_fromUtf8("actionListar_Datos"))
        self.actionSalir = QtGui.QAction(MainWindow)
        self.actionSalir.setObjectName(_fromUtf8("actionSalir"))
        self.actionAcerca_de = QtGui.QAction(MainWindow)
        self.actionAcerca_de.setObjectName(_fromUtf8("actionAcerca_de"))
        self.actionToolIngresar = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("list-add"))
        self.actionToolIngresar.setIcon(icon)
        self.actionToolIngresar.setObjectName(_fromUtf8("actionToolIngresar"))
        self.actionToolListar = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-print-preview"))
        self.actionToolListar.setIcon(icon)
        self.actionToolListar.setObjectName(_fromUtf8("actionToolListar"))
        self.actionToolAcercaDe = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("help-about"))
        self.actionToolAcercaDe.setIcon(icon)
        self.actionToolAcercaDe.setObjectName(_fromUtf8("actionToolAcercaDe"))
        self.menuMenu.addAction(self.actionIngresar_Datos)
        self.menuMenu.addAction(self.actionListar_Datos)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionSalir)
        self.menuAyuda.addAction(self.actionAcerca_de)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "SGP", None))
        self.label_2.setText(_translate("MainWindow", "Sistema para Gestion de Personas", None))
        self.btnIngresar.setText(_translate("MainWindow", "Ingresar", None))
        self.btnListar.setText(_translate("MainWindow", "Lsitar", None))
        self.btnAcercaDe.setText(_translate("MainWindow", "Acerca de", None))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu", None))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda", None))
        self.actionIngresar_Datos.setText(_translate("MainWindow", "Ingresar Datos", None))
        self.actionListar_Datos.setText(_translate("MainWindow", "Listar Datos", None))
        self.actionSalir.setText(_translate("MainWindow", "Salir", None))
        self.actionAcerca_de.setText(_translate("MainWindow", "Acerca de...", None))
        self.actionToolIngresar.setText(_translate("MainWindow", "ToolIngresar", None))
        self.actionToolListar.setText(_translate("MainWindow", "ToolListar", None))
        self.actionToolAcercaDe.setText(_translate("MainWindow", "AcercaDe", None))
        self.actionToolAcercaDe.setToolTip(_translate("MainWindow", "Acerca de", None))

