import sys
from PySide import QtGui

class Window(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.textEdit = QtGui.QTextEdit('Text Edit')
        self.listWidget = QtGui.QListWidget()
        self.listWidget.addItem('List Widget')
        self.label = QtGui.QLabel('Label')

        self.stackedLayout = QtGui.QStackedLayout()
        self.stackedLayout.addWidget(self.textEdit)
        self.stackedLayout.addWidget(self.listWidget)
        self.stackedLayout.addWidget(self.label)

        self.frame = QtGui.QFrame()
        self.frame.setLayout(self.stackedLayout)

        self.button1 = QtGui.QPushButton('Text Edit')
        self.button1.clicked.connect(lambda: self.stackedLayout.setCurrentIndex(0))
        self.button2 = QtGui.QPushButton('List Widget')
        self.button2.clicked.connect(lambda: self.stackedLayout.setCurrentIndex(1))
        self.button3 = QtGui.QPushButton('Label')
        self.button3.clicked.connect(lambda: self.stackedLayout.setCurrentIndex(2))

        buttonLayout = QtGui.QHBoxLayout()
        buttonLayout.addWidget(self.button1)
        buttonLayout.addWidget(self.button2)
        buttonLayout.addWidget(self.button3)

        layout = QtGui.QVBoxLayout(self)
        layout.addLayout(buttonLayout)
        layout.addWidget(self.frame)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    w = Window()
    w.show()

    sys.exit(app.exec_())