from PySide.QtCore import *
from PySide.QtGui import *
from sys import argv
import testui


class MyApp(QDialog, testui.Ui_MainWindow):
	def __init__(self):
		super(MyApp, self).__init__()
		self.setupUi(self)
		self.initUi()
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.closebtn.clicked.connect(self.close)


	def initUi(self):
		pass


app = QApplication(argv)
mp = MyApp()
mp.show()
app.exec_()