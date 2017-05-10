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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(534, 300)
        self.btnAgregar = QtGui.QPushButton(Form)
        self.btnAgregar.setGeometry(QtCore.QRect(210, 210, 88, 34))
        self.btnAgregar.setObjectName(_fromUtf8("btnAgregar"))
        self.txtNombre = QtGui.QLineEdit(Form)
        self.txtNombre.setGeometry(QtCore.QRect(210, 80, 113, 32))
        self.txtNombre.setObjectName(_fromUtf8("txtNombre"))
        self.txtApellido = QtGui.QLineEdit(Form)
        self.txtApellido.setGeometry(QtCore.QRect(210, 130, 113, 32))
        self.txtApellido.setObjectName(_fromUtf8("txtApellido"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 90, 59, 18))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(120, 140, 59, 18))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(120, 50, 59, 18))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.mensaje = QtGui.QLabel(Form)
        self.mensaje.setGeometry(QtCore.QRect(220, 180, 59, 18))
        self.mensaje.setText(_fromUtf8(""))
        self.mensaje.setObjectName(_fromUtf8("mensaje"))
        self.txtId = QtGui.QLineEdit(Form)
        self.txtId.setGeometry(QtCore.QRect(210, 40, 113, 32))
        self.txtId.setObjectName(_fromUtf8("txtId"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.btnAgregar.setText(_translate("Form", "Agregar", None))
        self.label.setText(_translate("Form", "Nombre", None))
        self.label_2.setText(_translate("Form", "Apellido", None))
        self.label_3.setText(_translate("Form", "Id", None))

