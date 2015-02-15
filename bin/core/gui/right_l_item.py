# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'right_l_item.ui'
#
# Created: Mon Feb 16 02:37:47 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(355, 82)
        Frame.setStyleSheet("QFrame#Frame{background-color: qlineargradient(spread:reflect, x1:0.48, y1:0, x2:0.486, y2:0.517045, stop:0.0621469 rgba(103, 103, 103, 255), stop:1 rgba(193, 193, 193, 255));}")
        Frame.setFrameShape(QtGui.QFrame.Box)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        Frame.setLineWidth(3)
        self.horizontalLayout = QtGui.QHBoxLayout(Frame)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtGui.QFrame(Frame)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.type = QtGui.QLabel(self.frame)
        self.type.setObjectName("type")
        self.verticalLayout.addWidget(self.type)
        self.label = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 1)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtGui.QFrame(Frame)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout.addWidget(self.frame_2)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QtGui.QApplication.translate("Frame", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.type.setText(QtGui.QApplication.translate("Frame", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Frame", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Frame", "Configure", None, QtGui.QApplication.UnicodeUTF8))

