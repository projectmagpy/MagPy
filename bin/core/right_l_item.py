# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'right_l_item.ui'
#
# Created: Wed Apr 08 10:09:06 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(823, 300)
        Frame.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.48, y1:0, x2:0.486, y2:0.517045, stop:0.0621469 rgba(103, 103, 103, 255), stop:1 rgba(193, 193, 193, 255));")
        Frame.setFrameShape(QtGui.QFrame.Box)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        Frame.setLineWidth(2)
        self.horizontalLayout = QtGui.QHBoxLayout(Frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtGui.QFrame(Frame)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtGui.QFrame(self.frame)
        self.frame_3.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.frame_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_3.setLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.type = QtGui.QLabel(self.frame_3)
        self.type.setStyleSheet("color: rgb(255, 255, 255);")
        self.type.setObjectName("type")
        self.verticalLayout_3.addWidget(self.type)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtGui.QFrame(self.frame)
        self.frame_4.setStyleSheet("background-color: rgb(92, 92, 92);")
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout = QtGui.QVBoxLayout(self.frame_4)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_5 = QtGui.QFrame(self.frame)
        self.frame_5.setStyleSheet("color: rgb(224, 252, 255);\n"
"background-color: rgb(98, 98, 98);")
        self.frame_5.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_5.setLineWidth(0)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.desc = QtGui.QLabel(self.frame_5)
        self.desc.setObjectName("desc")
        self.verticalLayout_4.addWidget(self.desc)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.verticalLayout_2.setStretch(0, 5)
        self.verticalLayout_2.setStretch(1, 10)
        self.verticalLayout_2.setStretch(2, 30)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtGui.QFrame(Frame)
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtGui.QGridLayout(self.frame_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.addbtn = QtGui.QPushButton(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addbtn.sizePolicy().hasHeightForWidth())
        self.addbtn.setSizePolicy(sizePolicy)
        self.addbtn.setAutoFillBackground(False)
        self.addbtn.setStyleSheet("background-color: rgb(90, 90, 90);\n"
"")
        self.addbtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/add73.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addbtn.setIcon(icon)
        self.addbtn.setIconSize(QtCore.QSize(50, 50))
        self.addbtn.setDefault(False)
        self.addbtn.setFlat(False)
        self.addbtn.setObjectName("addbtn")
        self.gridLayout.addWidget(self.addbtn, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_2)
        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QtGui.QApplication.translate("Frame", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.type.setText(QtGui.QApplication.translate("Frame", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Frame", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.desc.setText(QtGui.QApplication.translate("Frame", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

