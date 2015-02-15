from sys import argv
from PySide.QtGui import QDialog, QApplication, QListWidgetItem
from PySide.QtCore import Qt
import gui, right_item

class gui_interaction(QDialog, gui.Ui_main_window):
	"""
	A Class that handles the interactions between the GUI and the program. The GUI file [gui.py] is to be imported
	and handled here. All Signal Slot interactions are handled by this class.

	1. collecting keywords
	2. collecting all constraints
	3. voice based interactions
	4. display results
	5. options to export data, settings, etc.


	Class handled by Paul Jacob
	"""

	def __init__(self):
		super(gui_interaction, self).__init__()
		self.setupUi(self)
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.closebtn.clicked.connect(self.close)
		self.tasklist.setSpacing(3)
		self.selnav.setSpacing(3)
		self.initUi()
		self.show()
		self.tabs = ["File Management", "Navigation", "Selection", "", "Export"]

	def initUi(self):
		self.leftlist = self.stackedWidget
		self.rightlist = self.selnav
		for i in [x for x in range(0, 5)]:
			li = right_item.Item()
			myQListWidgetItem = QListWidgetItem(self.rightlist, i)
			myQListWidgetItem.setSizeHint(li.sizeHint())
			self.rightlist.addItem(myQListWidgetItem)
			self.rightlist.setItemWidget(myQListWidgetItem, li)

		self.prevbtn.clicked.connect(self.prev)
		self.nextbtn.clicked.connect(self.next)

	def next(self):
		self.stackedWidget.setCurrentIndex((self.stackedWidget.currentIndex()+1)%5)
		self.currentbtn.setText(self.tabs[self.stackedWidget.currentIndex()])
		self.prevbtn.setText(self.tabs[(self.stackedWidget.currentIndex()-1)%5])
		self.nextbtn.setText(self.tabs[(self.stackedWidget.currentIndex()+1)%5])


	def prev(self):
		self.stackedWidget.setCurrentIndex((self.stackedWidget.currentIndex()-1)%5)
		self.currentbtn.setText(self.tabs[self.stackedWidget.currentIndex()])
		self.prevbtn.setText(self.tabs[(self.stackedWidget.currentIndex()-1)%5])
		self.nextbtn.setText(self.tabs[(self.stackedWidget.currentIndex()+1)%5])

	def updateUi(self):
		pass

app = QApplication(argv)
mp = gui_interaction()
mp.show()
app.exec_()