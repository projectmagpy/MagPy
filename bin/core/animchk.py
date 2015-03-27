#!/usr/bin/env python
import sys

from PySide import QtGui, QtCore

application = QtGui.QApplication(sys.argv)


class Dashboard(QtGui.QWidget):
	""" Dashboard to slide up and down on request. """

	def __init__(self, parent):
		QtGui.QWidget.__init__(self, parent)

		self.pix = QtGui.QPixmap("images/add73.png")
		self.label = QtGui.QLabel(self)
		self.label.setPixmap(self.pix)

		self.layout = QtGui.QHBoxLayout(self)
		self.layout.addWidget(self.label)
		self.layout.setContentsMargins(1, 1, 1, 1)
		self.setLayout(self.layout)


class MainWindow(QtGui.QWidget):
	""" Main Window hosting button and dashboard"""

	def __init__(self):
		QtGui.QWidget.__init__(self)

		self.dashboard = Dashboard(self)
		self.toggleButton = QtGui.QPushButton("Close Dashboard")
		self.toggleButton.setMinimumHeight(27)

		self.layout = QtGui.QVBoxLayout(self)
		self.layout.addWidget(self.dashboard)
		self.layout.addWidget(self.toggleButton)
		self.layout.setContentsMargins(1, 1, 1, 1)

		self.setLayout(self.layout)

		self.connect(
			self.toggleButton, QtCore.SIGNAL('clicked()'), self.toggle)

	def toggle(self):
		self.hideAnimation = QtCore.QPropertyAnimation(self.dashboard, "geometry")
		self.hideAnimation.setDuration(300)
		self.dashboard.startGeometry = QtCore.QRect(self.dashboard.geometry())
		self.dashboard.endGeometry = QtCore.QRect(0,
												  self.dashboard.geometry().height(),
												  self.dashboard.geometry().width(),
												  0)
		self.hideAnimation.setStartValue(self.dashboard.startGeometry)
		self.hideAnimation.setEndValue(self.dashboard.endGeometry)
		self.dashboard.label.setSizePolicy(
			QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Ignored)
		self.hideAnimation.start()
		# self.parentHideAnimation = QtCore.QPropertyAnimation(self, "geometry")
		# self.parentHideAnimation.setDuration(300)
		# self.startGeometry = QtCore.QRect(self.geometry())
		# self.endGeometry = QtCore.QRect(self.geometry().x(),
		# 								self.geometry().y() +
		# 								self.dashboard.geometry().height(),
		# 								self.dashboard.width(),
		# 								self.toggleButton.geometry().height())
		# self.parentHideAnimation.setStartValue(self.startGeometry)
		# self.parentHideAnimation.setEndValue(self.endGeometry)
		# self.parentHideAnimation.start()


if __name__ == "__main__":
	main = MainWindow()
	main.show()
	sys.exit(application.exec_())
