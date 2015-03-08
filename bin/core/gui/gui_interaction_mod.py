from sys import argv, path
import time
from threading import Thread

from PySide.QtGui import *
from PySide.QtCore import *

import gui
import right_item
import left_item
import guidata as data

import infoDialogs as d

path.append("..")
import tasks


class gui_interaction(QDialog, gui.Ui_main_window):
	"""
	A Class that handles the interactions between the GUI and the program. The GUI file [gui.py] is to be imported
	and handled here. All Signal Slot interactions are handled by this class.

	1. collecting keywords
	2. collecting all constraints
	3. voice based interactions
	4. display results
	5. options to export data, settings, etc.
	"""

	updateSig = Signal()

	def __init__(self):
		super(gui_interaction, self).__init__()

		self.tasks_display_list = []
		self.tasksAdded = []
		self.items, self.index, self.tabnum = [], 0, 0
		self.currentMainTab = [0, 'main']
		self.setupUi(self)
		# self.setWindowFlags(Qt.FramelessWindowHint)
		self.closebtn.clicked.connect(self.close)
		self.pause = False
		self.th = Thread(target=self.looper)
		self.th.start()
		self.initUi()

		self.show()

	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def initUi(self):
		self.center()
		self.startbtn.clicked.connect(self.start)
		self.statusbtn.clicked.connect(lambda: self.ChangeTab("log"))
		self.mvbtn.clicked.connect(lambda: self.ChangeTab("myvault"))
		self.settingsbtn.clicked.connect(lambda: self.ChangeTab("settings"))
		self.helpbtn.clicked.connect(lambda: self.ChangeTab("help"))
		self.updateSig.connect(self.updateUi)
		self.stackedWidget.setCurrentIndex(1)
		self.currentbtn.setText(data.tabHeadings[1])
		self.prevbtn.setText(data.tabHeadings[0])
		self.nextbtn.setText(data.tabHeadings[2])

		# log page
		self.savebtn.clicked.connect(self.savelog)
		self.clearbtn.clicked.connect(self.clearlog)
		self.backbtn.clicked.connect(self.start)

		tabWidgets = [self.filenavlist, self.navnavlist, self.selnavlist, self.constraintlist, self.exportnavlist]
		for tab in data.tabHeadings:
			tabWidgets[self.tabnum].setSpacing(3)
			for i in [i for i in data.btns[self.tabnum]]:
				li = right_item.Item()
				li.label.setText(i)
				li.type.setText(tab)
				listItem = QListWidgetItem(tabWidgets[self.tabnum])
				listItem.setSizeHint(li.sizeHint())
				li.addbtn.clicked.connect(lambda n=self.index: self.newTask(n))
				tabWidgets[self.tabnum].addItem(listItem)
				tabWidgets[self.tabnum].setItemWidget(listItem, li)
				self.items.append(li)
				self.index += 1
			self.tabnum += 1
		self.prevbtn.clicked.connect(self.prev)
		self.nextbtn.clicked.connect(self.next)


	def start(self):
		if self.mainTabs.currentIndex() == 0:
			if len(self.tasks_display_list) == 0:
				self.msg = QMessageBox()
				self.msg.setText("Unable to start, No Tasks added yet!!!")
				self.msg.setWindowTitle("Error!!!")
				self.msg.show()
			else:
				self.taskmanager = tasks.TaskManager(self.tasks_display_list)
				print self.tasksAdded
		else:
			self.ChangeTab("main")


	def newTask(self, i):
		self.mp = d.getInfo([self.items[i].type.text(), self.items[i].label.text()])
		if self.mp.num_ip == 0:
			self.addToTaskList(self.mp.retval())
		elif not self.mp.exec_():
			self.addToTaskList(self.mp.retval())

	def addToTaskList(self, i):
		if i:
			temp = []
			if i[0][2] != "NULLTXT":
				text = "Description:\n"
				for j in i:
					text += (j[2] + " : " + j[3] + "\n")
					temp.append([j[2], j[3]])
				self.tasks_display_list.append(
					[len(self.tasks_display_list), data.tabHeadings[i[0][0]], data.btns[i[0][0]][i[0][1]], text])
				self.tasksAdded.append(
					[len(self.tasksAdded), i[0][0], i[0][1], data.tabHeadings[i[0][0]], data.btns[i[0][0]][i[0][1]], temp])
			else:
				self.tasks_display_list.append(
					[len(self.tasks_display_list), data.tabHeadings[i[0][0]], data.btns[i[0][0]][i[0][1]],
					 "No Description"])

	def next(self):
		currentTabIndex = data.tabHeadings.index(self.currentbtn.text())
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
		if self.currentMainTab[1] == 'main':
			self.tasklist.clear()
			for task in self.tasks_display_list:
				li = left_item.Item()
				li.label.setText(task[2])
				li.type.setText(task[1])
				li.desc.setText(task[3])

				li.itemCloseBtn.clicked.connect(lambda x=self.tasks_display_list.index(task): self.removeItem(x))
				li.itemUpBtn.clicked.connect(lambda x=self.tasks_display_list.index(task): self.moveItem(x, "Up"))
				li.itemDwnBtn.clicked.connect(lambda x=self.tasks_display_list.index(task): self.moveItem(x, "Down"))

				listItem = QListWidgetItem(self.tasklist)
				listItem.setSizeHint(li.sizeHint())
				self.tasklist.addItem(listItem)
				self.tasklist.setItemWidget(listItem, li)
		elif self.currentMainTab[1] == 'log':
			txt = open('../../logs/tasklog.txt').read()
			self.console.setText(txt)


	def removeItem(self, itemNum):
		self.tasks_display_list.pop(itemNum)


	def moveItem(self, itemNum, dir):
		if dir == "Up":
			self.tasks_display_list[itemNum], self.tasks_display_list[itemNum - 1] = self.tasks_display_list[
																						 itemNum - 1], \
																					 self.tasks_display_list[
																						 itemNum]
		if dir == "Down":
			self.tasks_display_list[itemNum], self.tasks_display_list[itemNum + 1] = self.tasks_display_list[
																						 itemNum + 1], \
																					 self.tasks_display_list[
																						 itemNum]

	def ChangeTab(self, name, sec=0):
		tabNames = [self.MainUI, self.StatusPage, self.MyVault, self.SettingsPage, self.HelpPage]
		# tabfuncs = [0, self.status, self.myvault, self.settings, self.help]

		if sec == 0:
			self.mtabs = ['main', 'log', 'myvault', 'settings', 'help']
			self.newTabName = name
			self.anim()

		else:
			if self.mainTabs.currentIndex() == 0 and self.newTabName != "main":
				self.startbtn.setText("Home")
				self.mainTabs.setCurrentIndex(self.mtabs.index(self.newTabName))
			elif self.mainTabs.currentIndex() == 0 and self.newTabName == "main":
				self.mainTabs.setCurrentIndex(self.mtabs.index(self.newTabName))
			elif self.newTabName == "main":
				self.startbtn.setText("Start")
				self.mainTabs.setCurrentIndex(self.mtabs.index(self.newTabName))
			self.restore()

		self.currentMainTab = [self.mtabs.index(self.newTabName), self.newTabName]


	def anim(self):
		self.geo = self.mainTabs.geometry()
		self.hideAnimation = QPropertyAnimation(self.mainTabs, "geometry")
		self.hideAnimation.setDuration(150)
		self.mainTabs.startGeometry = QRect(self.mainTabs.geometry())
		self.mainTabs.endGeometry = QRect(self.mainTabs.geometry().getRect()[0], self.mainTabs.geometry().getRect()[1],
										  self.mainTabs.geometry().width(), 0)
		self.hideAnimation.setStartValue(self.mainTabs.startGeometry)
		self.hideAnimation.setEndValue(self.mainTabs.endGeometry)
		self.hideAnimation.start()
		self.hideAnimation.finished.connect(lambda: self.ChangeTab("", sec=1))


	def restore(self):
		self.hideAnimation1 = QPropertyAnimation(self.mainTabs, "geometry")
		self.hideAnimation1.setDuration(100)
		self.mainTabs.startGeometry = QRect(self.mainTabs.geometry())
		self.mainTabs.endGeometry = QRect(self.geo)
		self.hideAnimation1.setStartValue(self.mainTabs.startGeometry)
		self.hideAnimation1.setEndValue(self.mainTabs.endGeometry)
		self.hideAnimation1.start()

	# self.hideAnimation1.finished.connect(lambda: self.ChangeTab("", sec=1))



	def status(self):
		pass

	def myvault(self):
		pass

	def settings(self):
		pass

	def savelog(self):
		txt = open('../../logs/tasklog.txt').read()
		open('C://savedlog.txt', 'w').write(txt)
		open('../../logs/tasklog.txt', 'a').write("\n# Logs Saved to C://savedlog.txt")

	def clearlog(self):
		open('../../logs/tasklog.txt', 'w').write("\n# Logs Cleared")


	def looper(self):
		while True:
			time.sleep(1)
			self.updateSig.emit()


app = QApplication(argv)
mp = gui_interaction()
mp.show()
app.exec_()