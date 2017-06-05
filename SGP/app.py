#! /urs/bin/python
# -*- coding: utf-8 -*-

"""
Descripcion: Aplicacion sencilla de manejo de datos

fecha ultima modificacion: 4 junio 2017
Autor: Edisson Reinozo

"""

import sys
from PyQt4 import QtGui, QtCore
from ManejoPersonas import Persona, Registro
from ui_main import MainWindow
from ui_add import AddWindow
import data

registro = Registro()

def main():
    app = QtGui.QApplication(sys.argv)
    data.init()
    main_view = MainWindow()
    main_view.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
