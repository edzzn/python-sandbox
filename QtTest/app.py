import sys
# QtCore allow us to make buttons
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        # Super return a QtGui
        super(Window, self).__init__()

        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQt Tut")
        self.setWindowIcon(QtGui.QIcon('imgs/logo.png'))

        # main menu
        extractAction = QtGui.QAction("&Exit ", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        self.home()


    def home(self):
        btn = QtGui.QPushButton("Quit",self)
        btn.clicked.connect(self.close_application)
        btn.resize(50, 25)
        btn.move(500-50, 300-25)

        extractAction = QtGui.QAction(QtGui.QIcon('imgs/WindowsPhone/light/appbar.close.png'),'Exit Application', self)
        extractAction.triggered.connect(self.close_application)

        self.toolbar = self.addToolBar("Extraction")
        self.toolbar.addAction(extractAction)


        fontChoice = QtGui.QAction('Font', self)
        fontChoice.triggered.connect(self.font_choice)

        self.toolbar = self.addToolBar("Font")
        self.toolbar.addAction(fontChoice)



        checkBox = QtGui.QCheckBox('Enlarge Window', self)
        checkBox.move(10, 75)
        checkBox.stateChanged.connect(self.enlarge_Window)

        self.progess = QtGui.QProgressBar(self)
        self.progess.setGeometry(200, 80, 250, 20)

        self.btn = QtGui.QPushButton("Download", self)

        self.btn.move(200, 120)
        self.btn.clicked.connect(self.download)


        # Drop-down button and Qstyles
        self.styleChoice = QtGui.QLabel("kde's", self)
        self.styleChoice.move(50, 150)

        comboBox = QtGui.QComboBox(self)
        comboBox.addItem("")
        comboBox.addItem("windows")
        comboBox.addItem("motif")
        comboBox.addItem("cde")
        comboBox.addItem("plastique")
        comboBox.addItem("cleanlooks")
        comboBox.move(50, 250)

        comboBox.activated[str].connect(self.style_choice)
        self.show()

    def font_choice(self):
        font, valid = QtGui.QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)

    def style_choice(self, text):
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))

    def download(self):
        self.completed = 0;

        while self.completed < 100:
            self.completed += 0.0001
            self.progess.setValue(self.completed)

    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Extract!',
                                            "Do you want to close?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

        if choice == QtGui.QMessageBox.Yes:
            print("Closing")
            sys.exit()
        else:
            pass

    def enlarge_Window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()
