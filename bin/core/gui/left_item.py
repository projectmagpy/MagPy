from PySide.QtGui import *
import left_l_item

class Item(QFrame, left_l_item.Ui_Frame):

	def __init__(self):
		super(Item, self).__init__()
		self.setupUi(self)

	def initUi(self):
		pass

	def updateUi(self):
		pass