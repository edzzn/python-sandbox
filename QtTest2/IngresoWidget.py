# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ingreso.ui'
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

class Ui_Ingreso_Widget(object):
    def setupUi(self, Ingreso_Widget):
        Ingreso_Widget.setObjectName(_fromUtf8("Ingreso_Widget"))
        Ingreso_Widget.resize(400, 300)
        self.txt_nombre = QtGui.QTextEdit(Ingreso_Widget)
        self.txt_nombre.setEnabled(True)
        self.txt_nombre.setGeometry(QtCore.QRect(170, 120, 141, 31))
        self.txt_nombre.setObjectName(_fromUtf8("txt_nombre"))
        self.txt_id = QtGui.QTextEdit(Ingreso_Widget)
        self.txt_id.setGeometry(QtCore.QRect(170, 80, 141, 31))
        self.txt_id.setObjectName(_fromUtf8("txt_id"))
        self.lb_apellido = QtGui.QLabel(Ingreso_Widget)
        self.lb_apellido.setGeometry(QtCore.QRect(100, 170, 59, 18))
        self.lb_apellido.setObjectName(_fromUtf8("lb_apellido"))
        self.txt_apellido = QtGui.QTextEdit(Ingreso_Widget)
        self.txt_apellido.setGeometry(QtCore.QRect(170, 160, 141, 31))
        self.txt_apellido.setObjectName(_fromUtf8("txt_apellido"))
        self.lb_nombre = QtGui.QLabel(Ingreso_Widget)
        self.lb_nombre.setGeometry(QtCore.QRect(100, 130, 59, 18))
        self.lb_nombre.setObjectName(_fromUtf8("lb_nombre"))
        self.lb_cedula = QtGui.QLabel(Ingreso_Widget)
        self.lb_cedula.setGeometry(QtCore.QRect(100, 90, 59, 18))
        self.lb_cedula.setObjectName(_fromUtf8("lb_cedula"))
        self.buttonBox = QtGui.QDialogButtonBox(Ingreso_Widget)
        self.buttonBox.setGeometry(QtCore.QRect(200, 230, 174, 34))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.lb_ingreso = QtGui.QLabel(Ingreso_Widget)
        self.lb_ingreso.setGeometry(QtCore.QRect(100, 30, 161, 20))
        self.lb_ingreso.setObjectName(_fromUtf8("lb_ingreso"))

        self.retranslateUi(Ingreso_Widget)
        QtCore.QMetaObject.connectSlotsByName(Ingreso_Widget)

    def retranslateUi(self, Ingreso_Widget):
        Ingreso_Widget.setWindowTitle(_translate("Ingreso_Widget", "Form", None))
        self.lb_apellido.setText(_translate("Ingreso_Widget", "Apellido", None))
        self.lb_nombre.setText(_translate("Ingreso_Widget", "Nombre", None))
        self.lb_cedula.setText(_translate("Ingreso_Widget", "Cédula", None))
        self.lb_ingreso.setText(_translate("Ingreso_Widget", "Ingrese un nuevo registro", None))

