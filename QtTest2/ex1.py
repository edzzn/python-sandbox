#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
this is simple example, a window in PyQT4
"""

import sys
from PyQt4 import QtGui

def main():

    # se crea un objeto aplicación.
    app = QtGui.QApplication(sys.argv)

    # Clase basica de una interfaz de usuario, Un widget sin paremetros se conoce como
    # ventana
    w = QtGui.QWidget()

    w.resize(250,150)
    w.move(300,300)
    w.setWindowTitle('Sample')

    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()