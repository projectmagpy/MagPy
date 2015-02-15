from PySide.QtCore import *
from PySide.QtGui import *
from sys import argv


class MyWidget(QWidget):
	def __init__(self):
		super(MyWidget, self).__init__()
		self.setAcceptDrops(True)
		self.initUi()

	def initUi(self):
		self.lab = QLabel("hello")
		self.btn = QPushButton("btn")
		self.l = QHBoxLayout()
		self.setLayout(self.l)
		self.l.addWidget(self.lab)
		self.l.addWidget(self.btn)

	def dragMoveEvent(self, event):
		print "hello"

	def dragEnterEvent(self, e):
		if e.mimeData().hasFormat('text/plain'):
			e.accept()
			print e.mimeData().text()
		else:
			e.ignore()


	def dropEvent(self, e):
		print e.mimeData().text()


class MyApp(QWidget):
	def __init__(self):
		super(MyApp, self).__init__()
		self.initUi()

	def initUi(self):
		self.l = QVBoxLayout()
		self.setLayout(self.l)
		mw = MyWidget()
		self.l.addWidget(mw)
		mw2 = MyWidget()
		self.l.addWidget(mw2)
		mw3 = MyWidget()
		self.l.addWidget(mw3)


app = QApplication(argv)
mp = MyApp()
mp.show()
app.exec_()