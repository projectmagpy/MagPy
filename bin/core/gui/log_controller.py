from PySide.QtCore import *
from PySide.QtGui import *
import console, time
from threading import Thread
from sys import argv


class MyApp(QDialog, console.Ui_Dialog):
	updateSig = Signal()
	def __init__(self):
		super(MyApp, self).__init__()
		self.setupUi(self)
		self.setModal = True
		self.initUi()

	def initUi(self):
		self.savebtn.clicked.connect(self.save)
		self.clearbtn.clicked.connect(self.clear)
		self.closebtn.clicked.connect(self.close)
		self.updateSig.connect(self.updateUi)
		Thread(target=self.looper).start()


	def updateUi(self):
		txt=open('../../logs/tasklog.txt').read()
		self.console.setText(txt)

	def save(self):
		txt=open('../../logs/tasklog.txt').read()
		open('C://savedlog.txt', 'w').write(txt)

	def clear(self):
		open('../../logs/tasklog.txt', 'w').write("")

	def looper(self):
		while True:
			self.updateSig.emit()
			time.sleep(1)
