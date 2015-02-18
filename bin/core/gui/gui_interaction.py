from sys import argv
from PySide.QtGui import QDialog, QApplication, QListWidgetItem, QDesktopWidget
from PySide.QtCore import Qt
import gui, right_item, left_item
import guidata as data


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
		# self.setWindowFlags(Qt.FramelessWindowHint)
		self.closebtn.clicked.connect(self.close)
		self.initUi()
		self.show()

	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def initUi(self):
		self.center()
		self.stackedWidget.setCurrentIndex(1)
		self.currentbtn.setText(data.tabHeadings[1])
		self.prevbtn.setText(data.tabHeadings[0])
		self.nextbtn.setText(data.tabHeadings[2])
		self.items, index, tabnum = [], 0, 0
		tabWidgets = [self.filenavlist, self.navnavlist, self.selnavlist, self.constraintlist, self.exportnavlist]
		for tab in data.tabHeadings:
			tabWidgets[tabnum].setSpacing(3)
			for i in [i for i in data.btns[tabnum]]:
				li = right_item.Item()
				li.label.setText(i)
				li.type.setText(tab)
				listItem = QListWidgetItem(tabWidgets[tabnum])
				listItem.setSizeHint(li.sizeHint())
				li.addbtn.clicked.connect(lambda n=index: self.addToTaskList("nav", n))
				tabWidgets[tabnum].addItem(listItem)
				tabWidgets[tabnum].setItemWidget(listItem, li)
				self.items.append(li)
				index += 1
			tabnum += 1

		self.prevbtn.clicked.connect(self.prev)
		self.nextbtn.clicked.connect(self.next)

	def addToTaskList(self, type, i):
		li = left_item.Item()
		li.label.setText(self.items[i].label.text())
		li.type.setText(type)
		listItem = QListWidgetItem(self.tasklist)
		listItem.setSizeHint(li.sizeHint())
		self.tasklist.addItem(listItem)
		self.tasklist.setItemWidget(listItem, li)

	def next(self):
		currentTabIndex = data.tabHeadings.index(self.currentbtn.text())
		print currentTabIndex
		self.stackedWidget.setCurrentIndex((self.stackedWidget.currentIndex() + 1) % 5)
		self.currentbtn.setText(data.tabHeadings[(currentTabIndex + 1) % 5])
		self.prevbtn.setText(data.tabHeadings[currentTabIndex])
		self.nextbtn.setText(data.tabHeadings[(currentTabIndex + 2) % 5])


	def prev(self):
		currentTabIndex = data.tabHeadings.index(self.currentbtn.text())
		self.stackedWidget.setCurrentIndex((self.stackedWidget.currentIndex() - 1) % 5)
		self.currentbtn.setText(data.tabHeadings[(currentTabIndex - 1) % 5])
		self.prevbtn.setText(data.tabHeadings[currentTabIndex])
		self.nextbtn.setText(data.tabHeadings[(currentTabIndex - 2) % 5])

	def updateUi(self):
		pass


app = QApplication(argv)
mp = gui_interaction()
mp.show()
app.exec_()